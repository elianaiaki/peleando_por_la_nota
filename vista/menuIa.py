import pygame
import os

def menu_Ia(pantalla, ancho, alto):
    """
    Menú de modo historia con imágenes de botones y fondo,
    igual al menú principal.
    """

    # Cargar fondo
    ruta = os.path.join("recursos", "menu03.png")
    imagen = pygame.image.load(ruta).convert()
    fondo = pygame.transform.scale(imagen, (ancho, alto))

    # Cargar imágenes de botones
    img_nueva    = pygame.image.load("recursos/nuevaPartida.png").convert_alpha()
    img_continuar = pygame.image.load("recursos/continuarPartida.png").convert_alpha()
    img_volver   = pygame.image.load("recursos/volver.png").convert_alpha()

    # Escalar botones
    img_nueva     = pygame.transform.scale(img_nueva,     (400, 25))
    img_continuar = pygame.transform.scale(img_continuar, (400, 25))
    img_volver    = pygame.transform.scale(img_volver,    (100, 23))

    # Posiciones de los botones
    rect_nueva     = pygame.Rect(150, 430, 500, 25)
    rect_continuar = pygame.Rect(150, 460, 500, 25)
    rect_volver    = pygame.Rect(350, 500, 100, 15)

    while True:
        # Dibujar fondo
        pantalla.blit(fondo, (0, 0))

        # Dibujar botones
        pantalla.blit(img_nueva,     (rect_nueva.x,     rect_nueva.y))
        pantalla.blit(img_continuar, (rect_continuar.x, rect_continuar.y))
        pantalla.blit(img_volver,    (rect_volver.x,    rect_volver.y))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if rect_nueva.collidepoint(pos):
                    return "nueva"

                if rect_continuar.collidepoint(pos):
                    return "continuar"

                if rect_volver.collidepoint(pos):
                    return "volver"