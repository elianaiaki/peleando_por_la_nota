import pygame

def menu_Ia(pantalla, ancho, alto):

    fuente = pygame.font.SysFont("Arial", 40)

    while True:

        pantalla.fill((0, 0, 0))

        nueva = pygame.Rect(250, 150, 300, 60)
        continuar = pygame.Rect(250, 250, 300, 60)
        volver = pygame.Rect(250, 350, 300, 60)

        pygame.draw.rect(pantalla, (80,80,80), nueva)
        pygame.draw.rect(pantalla, (80,80,80), continuar)
        pygame.draw.rect(pantalla, (80,80,80), volver)

        pantalla.blit(
            fuente.render("Nueva Partida", True, (255,255,255)),
            (270,165)
        )

        pantalla.blit(
            fuente.render("Continuar", True, (255,255,255)),
            (310,265)
        )

        pantalla.blit(
            fuente.render("Volver", True, (255,255,255)),
            (330,365)
        )

        pygame.display.flip()

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:

                pos = pygame.mouse.get_pos()

                if nueva.collidepoint(pos):
                    return "nueva"

                if continuar.collidepoint(pos):
                    return "continuar"

                if volver.collidepoint(pos):
                    return "volver"