# =====================================================================
# transicionNivel.py — Ejecuta la transición audiovisual entre niveles
# Ubicación: control/transicionNivel.py
# =====================================================================

import os
import pygame


def ejecutar_transicion_nivel(
    nivel,
    pantalla,
    jugadores,
    graficos,
    controlador_grafico,
    escenario,
    temporizador,
    reproducir_video
):
    """
    Reproduce el video y el audio de intro para el nivel dado,
    luego muestra la escena con los personajes y espera el sonido de round.

    nivel               -- número de nivel actual
    pantalla            -- superficie de pygame
    jugadores           -- lista [jugador1, jugador2] (modelos)
    graficos            -- lista [grafico1, grafico2]
    controlador_grafico -- instancia de controladorGrafico
    escenario           -- Surface del escenario actual
    reproducir_video    -- función reproducir_video(ruta, pantalla)
    """
    # Audio de intro en loop mientras dura el video
    pygame.mixer.music.stop()
    pygame.mixer.music.load("recursos/Sonidos/intro_pelea.wav")
    pygame.mixer.music.play(-1)

    reproducir_video(f"recursos/videos/intro_{nivel}.mp4", pantalla)

    pygame.mixer.music.stop()

    # Muestra el escenario con el HUD antes de comenzar la pelea
    controlador_grafico.dibujar(jugadores, graficos, temporizador, fondo=escenario)
    pygame.display.flip()

    # Sonido del round
    ruta_round = f"recursos/Sonidos/round_{nivel}.wav"
    ruta_round_img = f"recursos/rounds/round_{nivel}.png"

    if os.path.isfile(ruta_round_img):
        img_round = pygame.image.load(ruta_round_img).convert_alpha()
        img_round = pygame.transform.scale(img_round, (400, 100))
        controlador_grafico.dibujar(jugadores, graficos, temporizador, fondo=escenario)
        pantalla.blit(img_round, (800//2 - 200, 600//2 - 50))
        pygame.display.flip()

    if os.path.isfile(ruta_round):
        sonido_round = pygame.mixer.Sound(ruta_round)
        sonido_round.play()
        pygame.time.wait(int(sonido_round.get_length() * 1000))


    # Pausa adicional antes de habilitar controles
    pygame.time.wait(1000)