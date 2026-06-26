# =====================================================================
# bucleJuego.py — Bucle principal de la pelea
# =====================================================================

import pygame
from config import ANCHO, ALTO, AZUL
from control.controlador import Controlador
from control.controladorGrafico import controladorGrafico
from control.controladorMusica import ControladorMusica
from vista.cargadorPersonajes import crear_graficos, cargar_sprites
from config import SPRITES_CONFIG
from control.transicionNivel import ejecutar_transicion_nivel
from control.controladorIa import ia_basica


def ejecutar_juego(
    modo,
    jugadores,
    graficos,
    controlador,
    controlador_grafico,
    controlador_juego,
    musica,
    sonidos,
    temporizador,
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

    # Estado de la transición de nivel (solo se usa en modo historia)
    esperando_cambio = False
    timer_cambio = 0
    juego_ganado = False

    # Este while es el "corazón" del juego: se repite muchas veces por segundo
    # (60 veces, por el reloj.tick(60) de más abajo) hasta que el jugador
    # pierde, gana, o cierra la ventana.
    while controlador.corriendo:

        # Lee el teclado y los eventos de pygame (cerrar ventana, etc.)
        controlador.procesar_eventos()
        controlador.procesar_teclas()

        # Actualiza el estado del temporizador durante la pelea
        temporizador.actualizar(jugadores[0], jugadores[1])

        # Sincronizar muerte del modelo con el gráfico
        if jugadores[0].estado == "muerto" and graficos[0].estado not in ["muriendo", "muerto"]:
            graficos[0].estado = "muriendo"

        if jugadores[1].estado == "muerto" and graficos[1].estado not in ["muriendo", "muerto"]:
            graficos[1].estado = "muriendo"

        # Hace que cada personaje mire hacia el otro
        graficos[0].actualizar_direccion(graficos[1])
        graficos[1].actualizar_direccion(graficos[0])

        # Hace que cada personaje mire hacia el otro (para que el sprite
        # se voltee según donde esté el rival)
        graficos[0].actualizar_direccion(graficos[1])
        graficos[1].actualizar_direccion(graficos[0])

        # La IA solo debe manejar al jugador 2 cuando estamos en modo
        # historia. En 1vs1 NO se llama a ia_basica, porque ahí el jugador 2
        # lo controla una persona con el teclado (si la llamáramos siempre,
        # la IA y el teclado pelearían por mover al mismo personaje).
        if modo == "historia":
            ia_basica(graficos[1], graficos[0], controlador_juego, ANCHO, ALTO, paredes, controlador)

        # En modo historia el escenario depende del nivel actual.
        # En 1vs1 no hay "niveles", así que usamos siempre el nivel 1.
        if not juego_ganado:
            nivel = controlador_juego.nivel_actual if modo == "historia" else 1
            escenario_actual = controlador_grafico.obtener_escenario(nivel)

        # Dibuja el fondo, los personajes y las barras de vida en pantalla
        controlador_grafico.dibujar(jugadores, graficos, temporizador, fondo=escenario_actual)

        # musica.cambiar() ya se encarga de no repetir la canción si ya está sonando
        if controlador_grafico.fase_festejo:
            musica.cambiar(ControladorMusica.VICTORIA)

        # Actualiza la animación (sprite) de cada personaje.
        # sprite.actualizar(...) devuelve True cuando la animación actual
        # ya terminó de reproducirse, y ahí decidimos a qué estado pasar.
        for grafico in graficos:
            termino = grafico.sprite.actualizar(grafico.estado, grafico.movimiento)
            if termino:
                if grafico.estado in ("atacar", "bloquear", "golpeado"):
                    # Terminó de atacar/bloquear/recibir un golpe -> vuelve a quieto
                    grafico.estado = "quieto"
                elif grafico.estado == "muriendo":
                    # Terminó la animación de morir -> queda muerto definitivamente
                    grafico.estado = "muerto"

        #METODO TEMPORALIZADOR
        if temporizador.resultado == "empate":  # Si el tiempo terminó en empate, reinicia la pelea.

            texto = fuente.render("EMPATE", True, (255,255,255))
            pantalla.blit(texto, (340,250))

            pygame.display.flip()
            pygame.time.wait(3000)
            
            # Restaura la vida de ambos jugadores
            jugadores[0].vida = 100
            jugadores[1].vida = 100

            # Reinicia los estados de los personajes
            jugadores[0].estado = "quieto"
            jugadores[1].estado = "quieto"

            # Reinicia los gráficos de los personajes
            controlador_grafico.resetear_graficos(graficos)

            # Reinicia el temporizador para una nueva ronda
            temporizador.reiniciar()
        # ---------------------------
        # VICTORIA / DERROTA
        # ---------------------------
        if modo == "historia":
            # En historia, el jugador humano es siempre jugadores[0]
            if not jugadores[0].estoy_vivo():
                # Si muere el jugador humano, perdió la partida
                # (pero no la cortamos si justo se está festejando)
                if not controlador_grafico.fase_festejo:
                    musica.cambiar(ControladorMusica.DERROTA)
            elif not jugadores[1].estoy_vivo() and not esperando_cambio:
                temporizador.detener()
                # Si muere el enemigo (jugadores[1]), arrancamos el temporizador
                # para pasar al siguiente nivel después de un segundo
                esperando_cambio = True
                timer_cambio = pygame.time.get_ticks()
        else:
            # En 1vs1 no importa cuál de los dos pierde, el resultado es el mismo
            if not jugadores[0].estoy_vivo() or not jugadores[1].estoy_vivo():
                temporizador.detener()
                # Mismo cuidado: no pisar la música de victoria mientras dura el festejo
                if not controlador_grafico.fase_festejo:
                    musica.cambiar(ControladorMusica.DERROTA)

        # ---------------------------
        # CAMBIO DE NIVEL (historia)
        # ---------------------------
        if esperando_cambio:
            if pygame.time.get_ticks() - timer_cambio > 1000:
                esperando_cambio = False
                continua, nuevo_controlador_grafico = _cambiar_nivel(
                    controlador_juego, jugadores,
                    graficos,
                    controlador,
                    controlador_grafico,
                    musica,
                    sonidos,
                    temporizador,
                    paredes,
                    pantalla,
                    fuente,
                    reproducir_video
                )
                if not continua:
                    print("GANASTE EL JUEGO")
                    juego_ganado = True  # no cortamos todavía, esperamos el festejo
                else:
                    controlador_grafico = nuevo_controlador_grafico

        # Cuando el festejo del profe termina, cerramos el juego
        #if juego_ganado and controlador_grafico.festejo_termino:
        #    controlador.corriendo = False

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
    temporizador,
    paredes,
    pantalla,
    fuente,
    reproducir_video
):
    continua = controlador_juego.siguiente_nivel()
    if not continua:
        return False, None

    jugador2 = controlador_juego.enemigo
    jugadores[1] = jugador2

    nuevo_grafico = crear_graficos([jugador2], indices=[1])[0]
    cargar_sprites([nuevo_grafico], [jugador2], indices=[1], indices_festejo=[])
    graficos[1] = nuevo_grafico

    nuevo_controlador_grafico = controladorGrafico(pantalla, fuente)
    nuevo_controlador_grafico.cargar_escenarios(ANCHO, ALTO, "historia")
    nuevo_controlador_grafico.mostrar_festejo = (jugador2.nombre == "profe")
    nuevo_controlador_grafico.solo_jugador1_festeja = True

    nuevo_controlador_grafico.resetear_graficos(graficos)

    controlador.__init__(
        graficos[0],
        graficos[1],
        ANCHO,
        ALTO,
        paredes,
        sonidos
    )

    nivel = controlador_juego.nivel_actual
    escenario = nuevo_controlador_grafico.obtener_escenario(nivel)
    temporizador.detener()   # Oculta el conteo y muestra 60 durante la intro
    ejecutar_transicion_nivel(
        nivel,
        pantalla,
        jugadores,
        graficos,
        nuevo_controlador_grafico,
        escenario,
        temporizador,
        reproducir_video
    )

    musica.cambiar_pelea_nivel(nivel)
    temporizador.reiniciar() # Reinicia el temporizador al comenzar un nuevo nivel
    print("NIVEL:", nivel)

    return True, nuevo_controlador_grafico