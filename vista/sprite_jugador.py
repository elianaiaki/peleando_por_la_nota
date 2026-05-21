import pygame
import os

class SpriteJugador(pygame.sprite.Sprite):

    def __init__(self, ancho, alto):
        super().__init__()

        # ANIMACIONES
        self.quieto = []
        self.caminar = []
        self.atacar = []
        self.bloquear = []
        self.bloquear_caminando = []
        self.muriendo = []
        self.muerto = []
        self.golpeado = []

        # DIRECCIONES
        self.izquierda_caminando = []
        self.derecha_caminando = []

        self.ancho = ancho
        self.alto = alto

        self.imagen_actual = None

        self.contador_frame = 0
        self.indice_frame = 0
        self.velocidad_animacion = 10

        self.estado = "quieto"

    def cargar_imagenes(self, ruta, ancho_sprite, alto_sprite, columnas, tipo_animacion, escala=2.5, mirar_derecha=True):

        if not os.path.isfile(ruta):
             raise FileNotFoundError(
                 f"No se encontró el sprite: {ruta}"
             )

        imagen = pygame.image.load(ruta).convert_alpha()

        for col in range(columnas):

            x = col * ancho_sprite
            y = 0

            frame = imagen.subsurface(
                (x, y, ancho_sprite, alto_sprite)
            )

            frame = pygame.transform.scale(
                frame,
                (
                    int(ancho_sprite * escala),
                    int(alto_sprite * escala)
                )
            )


            # Girar sprite
            if not mirar_derecha:
                frame = pygame.transform.flip(frame, True, False)

            # GUARDAR FRAMES
            if tipo_animacion == "quieto":
                self.quieto.append(frame)

            elif tipo_animacion == "caminar":
                self.caminar.append(frame)

                self.izquierda_caminando.append(frame)
                self.derecha_caminando.append(frame)

            elif tipo_animacion == "atacar":
                self.atacar.append(frame)

            elif tipo_animacion == "bloquear":
                self.bloquear.append(frame)

            elif tipo_animacion == "muriendo":
                self.muriendo.append(frame)

            elif tipo_animacion == "muerto":
                self.muerto.append(frame)

    def actualizar(self, caminando=False, atacando=False, bloqueando=False, muriendo=False):

        # --------------------------------
        # SI YA ESTA MUERTO
        # --------------------------------
        if self.estado == "muerto":

            # frame fijo final
            if len(self.muerto) > 0:
                self.imagen_actual = self.muerto[0]

            return True

        # --------------------------------
        # CONTADOR DE VELOCIDAD
        # --------------------------------
        self.contador_frame += 1

        # --------------------------------
        # ELEGIR ANIMACION
        # --------------------------------

        if muriendo:

            self.estado = "muriendo"
            lista = self.muriendo

        elif atacando:

            self.estado = "atacar"
            lista = self.atacar

        elif bloqueando:

            self.estado = "bloquear"
            lista = self.bloquear

        elif caminando:

            self.estado = "caminar"
            lista = self.caminar

        else:

            self.estado = "quieto"
            lista = self.quieto

        # --------------------------------
        # VALIDAR QUE HAYA FRAMES
        # --------------------------------
        if len(lista) == 0:
            return False

        # --------------------------------
        # CAMBIAR FRAME
        # --------------------------------
        if self.contador_frame >= self.velocidad_animacion:

            self.indice_frame += 1
            self.contador_frame = 0

            # --------------------------------
            # TERMINO LA ANIMACION
            # --------------------------------
            if self.indice_frame >= len(lista):

                # MUERTE
                if muriendo:

                    self.estado = "muerto"

                    if len(self.muerto) > 0:
                        self.imagen_actual = self.muerto[0]

                    return True

                # ATAQUE / BLOQUEO
                elif atacando or bloqueando:

                    self.indice_frame = 0
                    return True

                # CAMINAR / QUIETO
                else:

                    self.indice_frame = 0

        # --------------------------------
        # FRAME ACTUAL
        # --------------------------------
        self.imagen_actual = lista[self.indice_frame]

        return False