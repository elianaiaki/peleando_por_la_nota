import pygame
import os
from modelo.Jugador import Jugador

def menu_1vs1(pantalla, ancho, alto):

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
        "yiyo": Jugador("yiyo", 100, 11, 5),
        "cliver": Jugador("cliver", 100, 11, 5),
        "cami": Jugador("cami", 100, 11, 5),
        "lean": Jugador("lean", 100, 11, 5)
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
        texto = fuente.render(f"Selecciona el personaje para el Jugador {len(seleccionado)+1}", True, blanco)

        pantalla.blit(texto, (150, 50))

        botones = []
        columnas = 4
        espacio_x = 200
        espacio_y = 220

        ancho_grilla = columnas * espacio_x
        inicio_x = (ancho - ancho_grilla) // 2 + (espacio_x - 150) // 2
        inicio_y = 150

        for i, personaje in enumerate(opciones.values()):

            fila = i // columnas
            col = i % columnas

            x = inicio_x + col * espacio_x
            y = inicio_y + fila * espacio_y

            rect = pygame.Rect(x, y, 150, 150)
            botones.append((rect, personaje))


            if personaje.nombre in bloqueados:
                # Si está bloqueado, lo dibujamos oscurecido y con un texto encima
                imagen_oscura = imagenes[personaje.nombre].copy()
                imagen_oscura.set_alpha(80)  # ← transparencia para que se vea gris
                pantalla.blit(imagen_oscura, (rect.x, rect.y))
                texto_bloqueado = fuente.render("Seleccionado", True, (255, 0, 0))
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