import pygame
from vista.sprite_jugador import SpriteJugador


class JugadorGrafico:
    def __init__(self, x, y, color, modelo, imagen_derrota):
        """ Inicializa el jugador gráfico. """
        self.rect = pygame.Rect(x, y, 60,60)
        self.color = color
        self.modelo = modelo

        self.imagen_derrota = imagen_derrota

        self.sprite = SpriteJugador(250, 250)

    def dibujar(self, pantalla):
        """ Dibuja el jugador en la pantalla. """
        if self.sprite.imagen_actual:
            imagen = self.sprite.imagen_actual
            imagen_rect = imagen.get_rect(center= self.rect.center)
            pantalla.blit(imagen, imagen_rect.topleft)
        else:
            pygame.draw.rect(pantalla, self.color, self.rect)

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
        self.modelo.atacar(otro.modelo)

    def actualizar_direccion(self, enemigo):
        mirando_derecha = self.rect.centerx < enemigo.rect.centerx
        nueva_direccion = "derecha" if mirando_derecha else "izquierda"
        if nueva_direccion != self.direccion_actual:
            self.direccion_actual = nueva_direccion
            for lista_nombre in ["quieto", "caminar", "atacar", "bloquear", "bloquear_caminando", "muriendo", "muerto", "golpeado"]:
                lista = getattr(self.sprite, lista_nombre)
                for i in range(len(lista)):
                    lista[i]= pygame.transform.flip(lista[i], True, False)