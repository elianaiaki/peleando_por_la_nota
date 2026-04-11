import pygame

class JugadorGrafico:
    def __init__(self, x, y, ancho, alto, color):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.color = color

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, self.rect)

    def mover(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def limitar_pantalla(self, ancho, alto):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > ancho:
            self.rect.right = ancho
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > alto:
            self.rect.bottom = alto

    def colisiona_con(self, otro):
        return self.rect.colliderect(otro.rect)