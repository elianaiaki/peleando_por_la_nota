import pygame

def menu_principal(pantalla, ancho, alto):

    fuente = pygame.font.SysFont("Arial", 40)

    while True:

        pantalla.fill((0, 0, 0))

        versus = pygame.Rect(250, 180, 300, 60)
        historia = pygame.Rect(250, 280, 300, 60)
        salir = pygame.Rect(250, 380, 300, 60)

        pygame.draw.rect(pantalla, (80, 80, 80), versus)
        pygame.draw.rect(pantalla, (80, 80, 80), historia)
        pygame.draw.rect(pantalla, (80, 80, 80), salir)

        pantalla.blit(
            fuente.render("1 VS 1", True, (255,255,255)),
            (340,195)
        )

        pantalla.blit(
            fuente.render("MODO HISTORIA", True, (255,255,255)),
            (250,295)
        )

        pantalla.blit(
            fuente.render("SALIR", True, (255,255,255)),
            (340,395)
        )

        pygame.display.flip()

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:

                pos = pygame.mouse.get_pos()

                if versus.collidepoint(pos):
                    return "1vs1"

                if historia.collidepoint(pos):
                    return "historia"

                if salir.collidepoint(pos):
                    pygame.quit()
                    exit()