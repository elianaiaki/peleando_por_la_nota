import pygame
import os

class SpriteJugador(pygame.sprite.Sprite):

    def __init__(self, ancho, alto):
        super().__init__()

        # -------------------------
        # ANIMACIONES
        # -------------------------
        self.quieto = []

        self.caminar01 = []
        self.caminar02 = []

        self.atacar = []

        self.bloquear00 = []
        self.bloquear01 = []
        self.bloquear02 = []

        self.muriendo = []
        self.muerto = []

        self.golpeado = []
        self.festejo01 = []

        # -------------------------
        # CONFIG
        # -------------------------
        self.ancho = ancho
        self.alto = alto

        self.imagen_actual = None

        self.contador_frame = 0
        self.indice_frame = 0

        self.velocidad_animacion = 8

        self.estado = "quieto"

    # ======================================================
    # CARGAR IMÁGENES
    # ======================================================
    def cargar_imagenes(
        self,
        ruta,
        ancho_sprite,
        alto_sprite,
        columnas,
        tipo_animacion,
        escala=2.5,
        mirar_derecha=True
    ):
    
        print("\n==============================")
        print("CARGANDO SPRITESHEET")
        print("==============================")
        print(f"Ruta: {ruta}")

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
                frame = pygame.transform.flip(
                    frame,
                    True,
                    False
                )

            # ======================================================
            # GUARDAR FRAMES
            # ======================================================

            if tipo_animacion == "quieto":
                self.quieto.append(frame)

            elif tipo_animacion == "caminar01":
                self.caminar01.append(frame)

            elif tipo_animacion == "caminar02":
                self.caminar02.append(frame)

            elif tipo_animacion == "atacar":
                self.atacar.append(frame)

            elif tipo_animacion == "bloquear00":
                self.bloquear00.append(frame)

            elif tipo_animacion == "bloquear01":
                self.bloquear01.append(frame)

            elif tipo_animacion == "bloquear02":
                self.bloquear02.append(frame)

            elif tipo_animacion == "muriendo":
                self.muriendo.append(frame)

            elif tipo_animacion == "muerto":
                self.muerto.append(frame)

            elif tipo_animacion == "golpeado":
                self.golpeado.append(frame)

            elif tipo_animacion == "festejo01":          # nuevo
                self.festejo01.append(frame)

    # ======================================================
    # ACTUALIZAR ANIMACIÓN
    # ======================================================

    def actualizar(self, estado="quieto", movimiento = "adelante"):
        animacion_terminada = False

        # ---------------------------------
        # SI CAMBIA EL ESTADO
        # ---------------------------------
        if estado != self.estado:

            self.estado = estado

            self.indice_frame = 0
            self.contador_frame = 0

        # ---------------------------------
        # ELEGIR ANIMACIÓN
        # ---------------------------------
        if estado == "quieto":
            lista = self.quieto

        # elif estado == "caminar":
        #     lista = self.caminar01
        elif estado == "caminar":

            if movimiento == "adelante":
                lista = self.caminar01

            else:
                lista = self.caminar02
        

        elif estado == "atacar":
            lista = self.atacar


        elif estado == "bloquear":

            if movimiento == "bloquear00":
                lista = self.bloquear00

            elif movimiento == "bloquear01":
                lista = self.bloquear01

            elif movimiento == "bloquear02":
                lista = self.bloquear02

            else:
                lista = self.bloquear00

        elif estado == "muriendo":
            lista = self.muriendo

        elif estado == "muerto":
            lista = self.muerto

        elif estado == "golpeado":
            lista = self.golpeado

        elif estado == "festejo":
            lista = self.festejo01
        else:
            lista = self.quieto

        # ---------------------------------
        # VALIDAR
        # ---------------------------------
        if len(lista) == 0:
            return False

        # ---------------------------------
        # ASEGURAR ÍNDICE VÁLIDO
        # ---------------------------------
        if self.indice_frame >= len(lista):
            self.indice_frame = 0

        # ---------------------------------
        # CONTROL FPS
        # ---------------------------------
        self.contador_frame += 1

        if self.contador_frame >= self.velocidad_animacion:

            self.contador_frame = 0

            self.indice_frame += 1

            # if self.indice_frame >= len(lista):
            #     self.indice_frame = 0

            if self.indice_frame >= len(lista):

                animacion_terminada = True

                self.indice_frame = 0

        
        # ---------------------------------
        # FRAME ACTUAL
        # ---------------------------------
        self.imagen_actual = lista[self.indice_frame]
        return animacion_terminada