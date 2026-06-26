# =====================================================================
# main.py — Punto de entrada del juego
# =====================================================================

import pygame
import sys
import os
sys.path.append(".")

from moviepy import VideoFileClip

from config import ANCHO, ALTO, AZUL
from vista.menuPrincipal import menu_principal
from control.inicializadorModo import inicializar_modo
from vista.cargadorPersonajes import crear_graficos, cargar_sprites
from control.controlador import Controlador
from control.controladorGrafico import controladorGrafico
from control.controladorMusica import ControladorMusica
from control.controladorSonido import ControladorSonido
from control.controladorTemp import ControladorTemp #Controlador del temporalizador de la partida
from control.transicionNivel import ejecutar_transicion_nivel
from control.bucleJuego import ejecutar_juego


# -----------------------------
# VIDEO
# -----------------------------

def reproducir_video(ruta_video, pantalla):
    """Reproduce un video frame a frame sobre la pantalla de pygame."""
    clip = VideoFileClip(ruta_video)
    reloj = pygame.time.Clock()
    for frame in clip.iter_frames(fps=clip.fps, dtype="uint8"):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                clip.close()
                pygame.quit()
                sys.exit()
        superficie = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
        superficie = pygame.transform.scale(superficie, pantalla.get_size())
        pantalla.blit(superficie, (0, 0))
        pygame.display.flip()
        reloj.tick(clip.fps)
    clip.close()


# INICIO
# -----------------------------

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("PELEANDO POR LA NOTA")
    fuente = pygame.font.SysFont(None, 36)

    # Menú principal
    modo = menu_principal(pantalla, ANCHO, ALTO)

    # Inicializar jugadores según el modo elegido
    jugadores, controlador_juego = inicializar_modo(modo, pantalla, ANCHO, ALTO)

    if jugadores is None:
        # El usuario eligió "volver" desde el menú de historia
        pygame.quit()
        sys.exit()

    # Crear gráficos
    graficos = crear_graficos(jugadores)
    graficos = crear_graficos(jugadores)

    # En historia solo Alan (índice 0) puede festejar; en 1vs1 cualquiera de los dos
    if modo == "historia":
        cargar_sprites(graficos, jugadores, indices_festejo=[0])
    else:
        cargar_sprites(graficos, jugadores)


    # Paredes
    paredes = [
        pygame.Rect(0, 0, 160, ALTO),
        pygame.Rect(ANCHO - 170, 0, 30, ALTO),
    ]

    # Controladores
    sonidos = ControladorSonido()
    controlador = Controlador(graficos[0], graficos[1], ANCHO, ALTO, paredes, sonidos)
    ctrl_grafico = controladorGrafico(pantalla, fuente)
    ctrl_grafico.cargar_escenarios(ANCHO, ALTO, modo)
    # Si el modo NO es historia (o sea, es 1vs1), siempre hay festejo.
    # Si es historia, solo hay festejo cuando el rival es "profe"
    # (porque profe es el último nivel del modo historia).
    ctrl_grafico.mostrar_festejo = (modo != "historia") or (jugadores[1].nombre == "profe")
    ctrl_grafico.solo_jugador1_festeja = (modo == "historia")


    musica = ControladorMusica()
    temporizador = ControladorTemp(60) # Crea el temporizador con una duración de 60 segundos

    # Transición de inicio y música
    nivel = controlador_juego.nivel_actual if modo == "historia" else 1
    escenario_actual = ctrl_grafico.obtener_escenario(nivel)

    if modo == "historia":
        ejecutar_transicion_nivel(nivel, pantalla, jugadores, graficos, ctrl_grafico, escenario_actual, temporizador, reproducir_video)
        musica.cambiar_pelea_nivel(nivel)
        temporizador.reiniciar() # Reinicia el temporizador al terminar la introducción del nivel
    else:
        ctrl_grafico.dibujar(jugadores, graficos, fondo=escenario_actual,  temporizador=temporizador)
        ctrl_grafico.dibujar_barras_vida(pantalla, jugadores, 100)
        pygame.display.flip()
        musica.cambiar(ControladorMusica.PELEA)
        temporizador.reiniciar() # Reinicia el temporizador al comenzar una partida 1 vs 1

    # Bucle principal
    ejecutar_juego(
        modo=modo,
        jugadores=jugadores,
        graficos=graficos,
        controlador=controlador,
        controlador_grafico=ctrl_grafico,
        controlador_juego=controlador_juego,
        musica=musica,
        sonidos=sonidos,
        temporizador=temporizador,
        paredes=paredes,
        pantalla=pantalla,
        fuente=fuente,
        reproducir_video=reproducir_video,
    )

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()