import pygame
import os
from modelo.Jugador import Jugador

def seleccionar_personajes(pantalla, ancho, alto):

    fuente = pygame.font.SysFont("Arial", 30)
    blanco = (255, 255, 255)

    # Fondo
    ruta = os.path.join("recursos", "menu.jpg")
    imagen_original = pygame.image.load(ruta).convert()
    fondo = pygame.transform.scale(imagen_original, (ancho, alto))

    # Crear personajes
    opciones = {
        "eliana": Jugador("eliana", 100, 10, 5),
        "alan": Jugador("alan", 100, 8, 6),
        "gabriel": Jugador("gabriel", 120, 12, 4),
        "gabo": Jugador("gabo", 80, 15, 3),
        "yiyo": Jugador("yiyo", 90, 11, 5)
    }

    # Cargar imágenes
    imagenes = {}

    for nombre in opciones:

        ruta_imagen = os.path.join(
            "recursos",
            "personajes",
            f"{nombre}.png"
        )

        imagen = pygame.image.load(ruta_imagen).convert_alpha()

        imagen = pygame.transform.scale(imagen, (150, 150))

        imagenes[nombre] = imagen

    seleccionado = []

    while len(seleccionado) < 2:

        pantalla.blit(fondo, (0, 0))

        texto = fuente.render(
            f"Selecciona el personaje para el Jugador {len(seleccionado)+1}",
            True,
            blanco
        )

        pantalla.blit(texto, (150, 50))

        botones = []

        for i, personaje in enumerate(opciones.values()):

            # FILA DE ARRIBA (3 personajes)
            if i < 3:
                x = 120 + i * 220
                y = 150

            # FILA DE ABAJO (2 personajes)
            else:
                x = 230 + (i - 3) * 220
                y = 350

            rect = pygame.Rect(x, y, 150, 150)

            botones.append((rect, personaje))

            # Dibujar imagen
            pantalla.blit(imagenes[personaje.nombre], (rect.x, rect.y))

            # # Opcional: borde
            # pygame.draw.rect(pantalla, blanco, rect, 3)

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                pos = pygame.mouse.get_pos()

                for rect, personaje in botones:

                    if rect.collidepoint(pos):

                        seleccionado.append(personaje)

    return seleccionado[0], seleccionado[1]