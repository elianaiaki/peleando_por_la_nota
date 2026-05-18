import pygame

class ultiGraficos:
    def __init__(self, x, y, color, modelo, ancho_pantalla):
        self.rect = pygame.Rect(x, y, 200, 200)
        self.color = color
        self.modelo = modelo  # Objeto Ulti
        self.activa = False
        self.velocidad = 10
        self.direccion = 1
        self.ancho_pantalla = ancho_pantalla

    def activar(self, x, y, direccion=1):
        self.rect.x = x
        self.rect.y = y
        self.direccion = direccion
        self.activa = True

    def actualizar(self, ancho_pantalla):
        if self.activa:
            self.rect.x += self.velocidad * self.direccion

            # Si sale de pantalla
            if self.rect.right < 0 or self.rect.left > ancho_pantalla:
                self.activa = False

    def dibujar(self, pantalla):
        if self.activa:
            pygame.draw.rect(pantalla, self.color, self.rect)