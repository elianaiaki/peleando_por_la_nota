import pygame
from vista.sprite_jugador import SpriteJugador


class JugadorGrafico:
    def __init__(self, x, y, color, modelo, imagen_derrota):
        """ Inicializa el jugador gráfico. """
        # self.rect = pygame.Rect(x, y, 60,60)
        self.rect = pygame.Rect(x, y, 60, 60)
        #self.rect1 = pygame.Rect(x, y, 60, 60)

        self.col_rect = pygame.Rect(
            self.rect.x,
            self.rect.y,
            40,
            60
        )

        self.col_rect.center = self.rect.center

        self.vel_x = 0
        self.color = color
        self.modelo = modelo
        self.direccion_actual = "derecha"  # Por defecto mirando a la derecha
        self.modelo.esta_caminando = False  # Agregamos atributo para saber si camina
        self.imagen_derrota = imagen_derrota
        self.sprite = SpriteJugador(250, 250)
        # ALTURA_PISO representa el nivel del suelo (ALTO - 110)
        ALTURA_PISO = y  # y será el valor del suelo al inicializar

        self.estado = "quieto"  # Estado inicial
        self.movimiento = "adelante"


    def dibujar(self, pantalla):
        """ Dibuja el jugador en la pantalla. """
        if self.sprite.imagen_actual:
            imagen = self.sprite.imagen_actual
            imagen_rect = imagen.get_rect(center= self.rect.center)
            pantalla.blit(imagen, imagen_rect.topleft)
        else:
            pygame.draw.rect(pantalla, self.color, self.rect)

    # def mover(self, direccion, cantidad, ANCHO, ALTO, enemigo=None):
    def mover(self,
    direccion,
    cantidad,
    ANCHO,
    ALTO,
    enemigo=None,
    paredes=[]
    ):

        # alannn
        original = self.rect.copy()  # Guardamos la posición original antes de movernos
        # ---
        """
        Mueve el personaje en una dirección dada.

        direccion: 'arriba', 'abajo', 'izquierda' o 'derecha'.
        cantidad: desplazamiento en píxeles.
        ANCHO, ALTO: límites de la pantalla para evitar salir.
        """

        if direccion == "izquierda":

            self.rect.x -= cantidad

            # Si mira a la derecha y va a la izquierda = retrocede
            if self.direccion_actual == "derecha":
                self.movimiento = "atras"
            else:
                self.movimiento = "adelante"

        elif direccion == "derecha":

            self.rect.x += cantidad

            # Si mira a la derecha y va a la derecha = avanza
            if self.direccion_actual == "derecha":
                self.movimiento = "adelante"
            else:
                self.movimiento = "atras"
    
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO

        # -----------------------------------
        # COLISIONES CON PAREDES
        # -----------------------------------
        for pared in paredes:

            if self.rect.colliderect(pared):

                self.rect = original
                break

        # ALANNNNNNNN

         # Actualizamos hit-box secundaria
            self.col_rect.center = self.rect.center

            # Si hay enemigo y colisionamos, lo empujamos
            if enemigo and self.col_rect.colliderect(enemigo.col_rect):
                desplazamiento = self.rect.x - original.x  # cuanto intentamos movernos
                # enemigo.rect.x += desplazamiento  # empujamos al enemigo en la misma dirección
                enemigo_original = enemigo.rect.copy()

                enemigo.rect.x += desplazamiento

                # -----------------------------------
                # COLISIONES ENEMIGO VS PAREDES
                # -----------------------------------
                for pared in paredes:

                    if enemigo.rect.colliderect(pared):

                        enemigo.rect = enemigo_original

                        # también cancelar movimiento propio
                        self.rect = original

                        return
                # Prevenir que el enemigo salga de pantalla
                if enemigo.rect.left < 0:
                    enemigo.rect.left = 0
                if enemigo.rect.right > ANCHO:
                    enemigo.rect.right = ANCHO

                # También mover su col_rect/ actualizar hitbox
                enemigo.col_rect.center = enemigo.rect.center
                
                # Verificar si todavía colisionan después del empuje
                if self.col_rect.colliderect(enemigo.col_rect):
                    # Si se sigue superponiendo, alinear los bordes
                    self.rect = original
                    # Actualizar hitbox del jugador
                    self.col_rect.center = self.rect.center
                    # Resetear velocidad en X para evitar que se siga moviendo en esa dirección
                    self.vel_x = 0

    def colisiona_con(self, otro):
        """ Verifica si este jugador colisiona con otro jugador. """
        return self.rect.colliderect(otro.rect)

    def atacar_a(self, otro):
        """ Lógica de ataque: Si están colisionando, el jugador ataca al otro. """
        self.modelo.atacar(otro.modelo)

    def actualizar_direccion(self, rival):
        mirando_derecha = self.rect.centerx < rival.rect.centerx
        nueva_direccion = "derecha" if mirando_derecha else "izquierda"

        if nueva_direccion != self.direccion_actual:
            self.direccion_actual = nueva_direccion

            # Voltea todos los frames cargados de cada animación
            for lista_nombre in [
                "quieto",
                "caminar01",
                "caminar02",
                "atacar",
                "bloquear00",
                "bloquear01",
                "bloquear02",
                "muriendo",
                "muerto",
                "golpeado"
            ]:
                lista = getattr(self.sprite, lista_nombre)
                for i in range(len(lista)):
                    lista[i] = pygame.transform.flip(lista[i], True, False)

    def obtener_hitbox_ataque(self):

        if self.direccion_actual == "derecha":

            return pygame.Rect(
                self.rect.right - 20,
                self.rect.y + 20,
                70,
                80
            )

        else:

            return pygame.Rect(
                self.rect.left - 50,
                self.rect.y + 20,
                70,
                80
            )
            