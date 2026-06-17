# =====================================================================
# bucleJuego.py — Bucle principal de la pelea
# Ubicación: control/bucleJuego.py
# =====================================================================

import pygame
from config import ANCHO, ALTO, AZUL
from control.controlador import Controlador
from control.controladorGrafico import controladorGrafico
from control.controladorMusica import ControladorMusica
from vista.cargadorPersonajes import crear_graficos, cargar_sprites
from config import SPRITES_CONFIG
from control.transicionNivel import ejecutar_transicion_nivel


def ejecutar_juego(
    modo,
    jugadores,
    graficos,
    controlador,
    controlador_grafico,
    controlador_juego,
    musica,
    sonidos,
    paredes,
    pantalla,
    fuente,
    reproducir_video
):
    """
    Ejecuta el bucle principal de la pelea hasta que el juego termina.

    modo               -- "1vs1" o "historia"
    jugadores          -- lista [jugador1, jugador2] (modelos)
    graficos           -- lista [grafico1, grafico2]
    controlador        -- instancia de Controlador
    controlador_grafico-- instancia de controladorGrafico
    controlador_juego  -- instancia de ControladorJuego (None si es 1vs1)
    musica             -- instancia de ControladorMusica
    sonidos            -- instancia de ControladorSonido
    paredes            -- lista de pygame.Rect con las paredes
    pantalla           -- superficie de pygame
    fuente             -- fuente de pygame para texto
    reproducir_video   -- función reproducir_video(ruta, pantalla)
    """
    reloj = pygame.time.Clock()

    # Estado de la transición de nivel (solo historia)
    esperando_cambio = False
    timer_cambio = 0

    while controlador.corriendo:
        controlador.procesar_eventos()
        controlador.procesar_teclas()

        graficos[0].actualizar_direccion(graficos[1])
        graficos[1].actualizar_direccion(graficos[0])

        # Escenario según nivel actual
        nivel = controlador_juego.nivel_actual if modo == "historia" else 1
        escenario_actual = controlador_grafico.obtener_escenario(nivel)

        controlador_grafico.dibujar(jugadores, graficos, fondo=escenario_actual)
        controlador_grafico.dibujar_barras_vida(pantalla, jugadores, 100)

        # Actualizar animaciones
        for grafico in graficos:
            termino = grafico.sprite.actualizar(grafico.estado, grafico.movimiento)
            if termino:
                if grafico.estado in ("atacar", "bloquear", "golpeado"):
                    grafico.estado = "quieto"
                elif grafico.estado == "muriendo":
                    grafico.estado = "muerto"

        # ---------------------------
        # VICTORIA / DERROTA
        # ---------------------------
        if modo == "historia":
            if not jugadores[0].estoy_vivo():
                musica.cambiar(ControladorMusica.DERROTA)
            elif not jugadores[1].estoy_vivo() and not esperando_cambio:
                esperando_cambio = True
                timer_cambio = pygame.time.get_ticks()
        else:
            if not jugadores[0].estoy_vivo() or not jugadores[1].estoy_vivo():
                musica.cambiar(ControladorMusica.DERROTA)

        # ---------------------------
        # CAMBIO DE NIVEL (historia)
        # ---------------------------
        if esperando_cambio:
            if pygame.time.get_ticks() - timer_cambio > 1000:
                esperando_cambio = False
                continua = _cambiar_nivel(
                    controlador_juego,
                    jugadores,
                    graficos,
                    controlador,
                    controlador_grafico,
                    musica,
                    sonidos,
                    paredes,
                    pantalla,
                    fuente,
                    reproducir_video
                )
                if not continua:
                    print("GANASTE EL JUEGO")
                    controlador.corriendo = False

        pygame.display.flip()
        reloj.tick(60)


# -----------------------------
# PRIVADA
# -----------------------------

def _cambiar_nivel(
    controlador_juego,
    jugadores,
    graficos,
    controlador,
    controlador_grafico,
    musica,
    sonidos,
    paredes,
    pantalla,
    fuente,
    reproducir_video
):
    """
    Avanza al siguiente nivel: crea el nuevo enemigo, recarga gráficos,
    ejecuta la transición y reinicia el controlador.

    Retorna True si hay siguiente nivel, False si el juego terminó.
    """
    continua = controlador_juego.siguiente_nivel()
    if not continua:
        return False

    jugador2 = controlador_juego.enemigo
    jugadores[1] = jugador2

    # Crear nuevo gráfico para el enemigo

    # jugador2 siempre debe ser tratado como el "jugador 2"
    # (posición derecha, color azul, mirando a la izquierda),
    # aunque acá venga solo en una lista de un elemento.
    nuevo_grafico = crear_graficos([jugador2], indices=[1])[0]
    cargar_sprites([nuevo_grafico], [jugador2], indices=[1])
    graficos[1] = nuevo_grafico

    # Recrear controladores para el nuevo nivel
    nuevo_controlador_grafico = controladorGrafico(pantalla, fuente)
    nuevo_controlador_grafico.cargar_escenarios(ANCHO, ALTO, "historia")
    nuevo_controlador_grafico.resetear_graficos(graficos)

    # Reemplazar in-place para que bucleJuego use la nueva instancia
    controlador_grafico.__dict__.update(nuevo_controlador_grafico.__dict__)

    controlador.__init__(
        graficos[0],
        graficos[1],
        ANCHO,
        ALTO,
        paredes,
        sonidos
    )

    # Transición audiovisual del nuevo nivel
    nivel = controlador_juego.nivel_actual
    escenario = controlador_grafico.obtener_escenario(nivel)
    ejecutar_transicion_nivel(
        nivel,
        pantalla,
        jugadores,
        graficos,
        controlador_grafico,
        escenario,
        reproducir_video
    )

    musica.cambiar_pelea_nivel(nivel)
    print("NIVEL:", nivel)
    return True