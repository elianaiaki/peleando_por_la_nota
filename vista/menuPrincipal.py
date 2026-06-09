import pygame
import os

def menu_principal(pantalla, ancho, alto):
    ruta = os.path.join("recursos", "menu01.png")
    imagen = pygame.image.load(ruta).convert()
    fondo = pygame.transform.scale(imagen, (ancho, alto))

    # Cargar imágenes de botones
    img_ia      = pygame.image.load("recursos/unoVSia.png").convert_alpha()
    img_1vs1    = pygame.image.load("recursos/unoVSuno.png").convert_alpha()
    img_salir   = pygame.image.load("recursos/salir.png").convert_alpha()

    # Mismo tamaño para todos
    img_ia    = pygame.transform.scale(img_ia,    (400, 25))
    img_1vs1  = pygame.transform.scale(img_1vs1,  (400, 25))
    img_salir = pygame.transform.scale(img_salir, (100, 23))  # salir más chico


    # Centrado: (800 - ancho) // 2
    rect_1vs1  = pygame.Rect(150, 430, 500, 25)
    rect_ia    = pygame.Rect(150, 460, 500, 25)
    rect_salir = pygame.Rect(350, 500, 100, 15)


    while True:
        pantalla.blit(fondo, (0, 0))

        pantalla.blit(img_1vs1,  (rect_1vs1.x,  rect_1vs1.y))
        pantalla.blit(img_ia,    (rect_ia.x,    rect_ia.y))
        pantalla.blit(img_salir, (rect_salir.x, rect_salir.y))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if rect_1vs1.collidepoint(pos):
                    return "1vs1"
                if rect_ia.collidepoint(pos):
                    return "historia"
                if rect_salir.collidepoint(pos):
                    pygame.quit()
                    exit()