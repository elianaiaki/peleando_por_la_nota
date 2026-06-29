import pygame

class PantallaFinControlador:

    def __init__(self):
        self.seleccion = 0
        self.opciones = ["Volver", "Salir"]
        self.inicio = pygame.time.get_ticks()
        self.mostrar_opciones = False

    def actualizar_tiempo(self):
        if not self.mostrar_opciones:
            if pygame.time.get_ticks() - self.inicio >= 3000:
                self.mostrar_opciones = True

    def manejar_eventos(self, eventos):
        for evento in eventos:

            if evento.type == pygame.QUIT:
                return "salir"

            if not self.mostrar_opciones:
                continue

            if evento.type == pygame.KEYDOWN:

                if evento.key in (pygame.K_UP, pygame.K_DOWN):
                    self.seleccion = 1 - self.seleccion

                elif evento.key == pygame.K_RETURN:
                    return "menu" if self.seleccion == 0 else "salir"

            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                for i in range(len(self.opciones)):
                    rect = pygame.Rect(100, 480 + i * 50, 240, 40)
                    if rect.collidepoint(pos):
                        return "menu" if i == 0 else "salir"
                    