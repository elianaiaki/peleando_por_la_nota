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

    # Este while es el "corazón" del juego: se repite muchas veces por segundo
    # (60 veces, por el reloj.tick(60) de más abajo) hasta que el jugador
    # pierde, gana, o cierra la ventana.
    while controlador.corriendo:

        # Lee el teclado y los eventos de pygame (cerrar ventana, etc.)
        controlador.procesar_eventos()
        controlador.procesar_teclas()

        #Actualiza el temporalizador
        temporizador.actualizar(
            jugadores[0],
            jugadores[1]
        )

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
        nivel = controlador_juego.nivel_actual if modo == "historia" else 1
        escenario_actual = controlador_grafico.obtener_escenario(nivel)

        # Dibuja el fondo, los personajes y las barras de vida en pantalla
        controlador_grafico.dibujar(jugadores, graficos, fondo=escenario_actual)
        controlador_grafico.dibujar_barras_vida(pantalla, jugadores, 100)
        controlador_grafico.dibujar_temporizador(pantalla, temporizador) #Dibuja el temporalizador

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
        if temporizador.resultado == "empate":

            texto = fuente.render("EMPATE", True, (255,255,255))
            pantalla.blit(texto, (340,250))

            pygame.display.flip()
            pygame.time.wait(3000)
            
            # Restaura la vida de los personajes
            jugadores[0].vida = 100
            jugadores[1].vida = 100

            # Reinicia los estados
            jugadores[0].estado = "quieto"
            jugadores[1].estado = "quieto"

            # Reinicia los gráficos
            controlador_grafico.resetear_graficos(graficos)

            # Reinicia el temporizador
            temporizador.reiniciar()
        # ---------------------------
        # VICTORIA / DERROTA
        # ---------------------------
        if modo == "historia":
            # En historia, el jugador humano es siempre jugadores[0]
            if not jugadores[0].estoy_vivo():
                # Si muere el jugador humano, perdió la partida
                musica.cambiar(ControladorMusica.DERROTA)
            elif not jugadores[1].estoy_vivo() and not esperando_cambio:
                # Si muere el enemigo (jugadores[1]), arrancamos el temporizador
                # para pasar al siguiente nivel después de un segundo
                esperando_cambio = True
                timer_cambio = pygame.time.get_ticks()
        else:
            # En 1vs1 no importa cuál de los dos pierde, el resultado es el mismo
            if not jugadores[0].estoy_vivo() or not jugadores[1].estoy_vivo():
                musica.cambiar(ControladorMusica.DERROTA)

        # ---------------------------
        # CAMBIO DE NIVEL (historia)
        # ---------------------------
        if esperando_cambio:
            # pygame.time.get_ticks() devuelve los milisegundos desde que
            # arrancó pygame. Si pasó más de 1000 ms (1 segundo) desde que
            # murió el enemigo, recién ahí cambiamos de nivel.
            if pygame.time.get_ticks() - timer_cambio > 1000:
                esperando_cambio = False

                # _cambiar_nivel(...) ahora devuelve DOS valores en vez de uno:
                # 1) continua -> True si hay más niveles, False si ya no quedan
                # 2) controlador_grafico -> el controlador gráfico NUEVO, ya
                #    preparado para el nivel que sigue
                #
                # Por eso del lado izquierdo ponemos dos variables separadas
                # por una coma: Python las "desempaqueta" automáticamente.
                continua, controlador_grafico = _cambiar_nivel(
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
                )

                if not continua:
                    # Ya no hay más niveles: el jugador completó el modo historia
                    print("GANASTE EL JUEGO")
                    controlador.corriendo = False

        # Muestra todo lo dibujado en esta vuelta del bucle
        pygame.display.flip()
        # Limita el juego a 60 actualizaciones por segundo (FPS)
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
    """
    Avanza al siguiente nivel: crea el nuevo enemigo, recarga gráficos,
    ejecuta la transición y reinicia el controlador.

    Esta función ahora devuelve SIEMPRE dos valores (una tupla), nunca uno
    solo. Eso es obligatorio porque en bucleJuego.py la recibimos así:

        continua, controlador_grafico = _cambiar_nivel(...)

    Si alguna de las líneas "return" de aquí abajo devolviera un solo valor,
    Python tiraría un error al intentar repartirlo en dos variables.

    Retorna:
        (True, nuevo_controlador_grafico)  -- si hay un siguiente nivel
        (False, None)                      -- si ya no quedan niveles (fin del juego)
    """

    # Le preguntamos al controlador de juego si hay un siguiente nivel.
    # Si no hay más niveles, terminamos la función ACÁ.
    continua = controlador_juego.siguiente_nivel()
    if not continua:
        # Importante: aunque no haya nada útil para devolver en el segundo
        # valor, ponemos None como "relleno", porque la otra punta del
        # código siempre espera recibir DOS valores, no uno.
        return False, None

    # A partir de acá sabemos que sí hay un nivel siguiente.

    # El nuevo enemigo del nivel que viene
    jugador2 = controlador_juego.enemigo
    jugadores[1] = jugador2

    # Creamos el gráfico (sprite, posición, etc.) para el nuevo enemigo.
    # jugador2 siempre debe ser tratado como el "jugador 2"
    # (posición derecha, color azul, mirando a la izquierda),
    # aunque acá venga solo en una lista de un elemento.
    nuevo_grafico = crear_graficos([jugador2], indices=[1])[0]
    cargar_sprites([nuevo_grafico], [jugador2], indices=[1])
    graficos[1] = nuevo_grafico

    # Creamos un controladorGrafico totalmente NUEVO para este nivel,
    # con su propio escenario cargado.
    #
    # Ojo: antes esta función mutaba el controlador_grafico VIEJO usando
    # controlador_grafico.__dict__.update(nuevo_controlador_grafico.__dict__),
    # un truco para "copiarle por dentro" los atributos del nuevo al viejo.
    # Ahora en cambio NO tocamos el viejo para nada: directamente seguimos
    # trabajando con nuevo_controlador_grafico, y al final de la función
    # lo devolvemos, para que bucleJuego.py lo reciba y lo use de ahí en más.
    nuevo_controlador_grafico = controladorGrafico(pantalla, fuente)
    nuevo_controlador_grafico.cargar_escenarios(ANCHO, ALTO, "historia")
    nuevo_controlador_grafico.resetear_graficos(graficos)

    # Reiniciamos el controlador de input/colisiones con los gráficos
    # actualizados (el del jugador 1 sigue igual, el del jugador 2 es el nuevo)
    controlador.__init__(
        graficos[0],
        graficos[1],
        ANCHO,
        ALTO,
        paredes,
        sonidos
    )

    # Mostramos la animación/video de transición hacia el nuevo nivel.
    # Usamos nuevo_controlador_grafico (no el viejo) porque es el que ya
    # tiene cargado el escenario correcto para este nivel.
    nivel = controlador_juego.nivel_actual
    escenario = nuevo_controlador_grafico.obtener_escenario(nivel)
    ejecutar_transicion_nivel(
        nivel,
        pantalla,
        jugadores,
        graficos,
        nuevo_controlador_grafico,
        escenario,
        reproducir_video
    )

    # Cambiamos la música al tema de pelea correspondiente a este nivel
    musica.cambiar_pelea_nivel(nivel)
    temporizador.reiniciar()
    print("NIVEL:", nivel)

    # Devolvemos True (sí hay nivel siguiente) junto con el controlador
    # gráfico nuevo, para que bucleJuego.py lo use de ahora en adelante
    return True, nuevo_controlador_grafico