import pygame

class JugadorGrafico:
    # def __init__(self, x, y, ancho, alto, color,modelo):
    def __init__(self, x, y, color,modelo):
        """ Inicializa el jugador gráfico. """
        # self.rect = pygame.Rect(x, y, ancho, alto)
        self.rect = pygame.Rect(x, y, 60,60)
        self.color = color
        self.modelo = modelo

    def dibujar(self, pantalla):
        """ Dibuja el jugador en la pantalla. """
        pygame.draw.rect(pantalla, self.color, self.rect)

    
    # def mover(self, dx, dy):
    #     self.rect.x += dx
    #     self.rect.y += dy

    def mover(self, direccion, cantidad, ANCHO, ALTO):
        """
        Mueve el personaje en una dirección dada.

        direccion: 'arriba', 'abajo', 'izquierda' o 'derecha'.
        cantidad: desplazamiento en píxeles.
        ANCHO, ALTO: límites de la pantalla para evitar salir.
        """
        if direccion == "arriba":
            self.rect.y -= cantidad
        elif direccion == "abajo":
            self.rect.y += cantidad
        elif direccion == "izquierda":
            self.rect.x -= cantidad
        elif direccion == "derecha":
            self.rect.x += cantidad
    
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO

    def colisiona_con(self, otro):
        """ Verifica si este jugador colisiona con otro jugador. """
        return self.rect.colliderect(otro.rect)

    def atacar_a(self, otro):
        """ Lógica de ataque: Si están colisionando, el jugador ataca al otro. """
        #distancia = self.rect.centerx - otro.rect.centerx
        #if abs(distancia) <= self.modelo.alcance:
        self.modelo.atacar(otro.modelo)