import pygame
import os
from modelo.Jugador import Jugador

def seleccionar_personajes(pantalla, ancho, alto):

    fuente = pygame.font.SysFont("Arial", 30)
    blanco = (255, 255, 255)

    # Fondo
    ruta = os.path.join("recursos", "menu.png")
    imagen_original = pygame.image.load(ruta).convert()
    fondo = pygame.transform.scale(imagen_original, (ancho, alto))

    # Crear personajes
    opciones = {
        "eliana": Jugador("eliana", 100, 10, 5),
        "alan": Jugador("alan", 100, 8, 6),
        "gabriel": Jugador("gabriel", 100, 12, 4),
        "gabo": Jugador("gabo", 100, 15, 3),
        "yiyo": Jugador("yiyo", 100, 11, 5)
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
    # Lista de personajes bloqueados, se llena cuando el jugador 1 elige
    bloqueados = []

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


            if personaje.nombre in bloqueados:
                # Si está bloqueado, lo dibujamos oscurecido y con un texto encima
                imagen_oscura = imagenes[personaje.nombre].copy()
                imagen_oscura.set_alpha(80)  # ← transparencia para que se vea gris
                pantalla.blit(imagen_oscura, (rect.x, rect.y))
                texto_bloqueado = fuente.render("Ya seleccionado.", True, (255, 0, 0))
                pantalla.blit(texto_bloqueado, (rect.x + 20, rect.y + 60))
            else:
                # Si no está bloqueado, se dibuja normal
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
                # Solo permite seleccionar si no está bloqueado
                    if rect.collidepoint(pos) and personaje.nombre not in bloqueados:
                        seleccionado.append(personaje)
                        # Bloquea el personaje para que el siguiente jugador no lo pueda elegir
                        bloqueados.append(personaje.nombre) 

    return seleccionado[0], seleccionado[1]