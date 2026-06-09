# import pygame
# import os

# class SpriteJugador(pygame.sprite.Sprite):

#     def __init__(self, ancho, alto):
#         super().__init__()


#         # ANIMACIONES
#         self.quieto = []
#         self.caminar1= []
#         self.caminar2 = []
#         self.atacar = []
#         self.bloquear00 = []
#         self.bloquear01 = []
#         self.bloquear02 = []
#         self.muriendo = []
#         self.muerto = []
#         self.golpeado = []

#         # # DIRECCIONES
#         # self.izquierda_caminando = []
#         # self.derecha_caminando = []

#         self.ancho = ancho
#         self.alto = alto
#         self.imagen_actual = None
#         self.contador_frame = 0
#         self.indice_frame = 0
#         self.velocidad_animacion = 10
#         self.estado = "quieto"

#     def cargar_imagenes(self, ruta, ancho_sprite, alto_sprite, columnas, tipo_animacion, escala=2.5, mirar_derecha=True):

#         if not os.path.isfile(ruta):
#              raise FileNotFoundError(
#                  f"No se encontró el sprite: {ruta}"
#              )
#         print(f"\nCargando: {ruta}")
#         imagen = pygame.image.load(ruta).convert_alpha()

#         for col in range(columnas):

#             x = col * ancho_sprite
#             y = 0

#             frame = imagen.subsurface(
#                 (x, y, ancho_sprite, alto_sprite)
#             )

#             frame = pygame.transform.scale(
#                 frame,
#                 (
#                     int(ancho_sprite * escala),
#                     int(alto_sprite * escala)
#                 )
#             )

#             print(f"Frame {col} cargado para animación '{tipo_animacion}'")
#             print(f" - Tamaño original: ({ancho_sprite}, {alto_sprite})")
#             print(f" - Tamaño escalado: ({frame.get_width()}, {frame.get_height()})")
#             print(f" - Mirar derecha: {mirar_derecha}")

#             # Girar sprite
#             if not mirar_derecha:
#                 frame = pygame.transform.flip(frame, True, False)

#             # GUARDAR FRAMES
#             if tipo_animacion == "quieto":
#                 self.quieto.append(frame)

#             elif tipo_animacion == "caminar":
#                 self.caminar0.append(frame)
#                 self.caminar2.append(frame)
#                 self.caminar1.append(frame)

#             elif tipo_animacion == "atacar":
#                 self.atacar.append(frame)

#             elif tipo_animacion == "bloquear":
#                 self.bloquear00.append(frame)
#                 self.bloquear01.append(frame)
#                 self.bloquear02.append(frame)


#             elif tipo_animacion == "muriendo":
#                 self.muriendo.append(frame)

#             elif tipo_animacion == "muerto":
#                 self.muerto.append(frame)

#     # def actualizar(self, caminando=False, atacando=False, bloqueando=False, muriendo=False):

#     #     # --------------------------------
#     #     # SI YA ESTA MUERTO
#     #     # --------------------------------
#     #     if self.estado == "muerto":

#     #         # frame fijo final
#     #         if len(self.muerto) > 0:
#     #             self.imagen_actual = self.muerto[0]

#     #         return True

#     #     # --------------------------------
#     #     # CONTADOR DE VELOCIDAD
#     #     # --------------------------------
#     #     self.contador_frame += 1

#     #     # --------------------------------
#     #     # ELEGIR ANIMACION
#     #     # --------------------------------

#     #     if muriendo:

#     #         self.estado = "muriendo"
#     #         lista = self.muriendo

#     #     elif atacando:

#     #         self.estado = "atacar"
#     #         lista = self.atacar

#     #     elif bloqueando:

#     #         self.estado = "bloquear"
#     #         lista = self.bloquear

#     #     elif caminando:

#     #         self.estado = "caminar"
#     #         lista = self.caminar

#     #     else:

#     #         self.estado = "quieto"
#     #         lista = self.quieto

#     #     # --------------------------------
#     #     # VALIDAR QUE HAYA FRAMES
#     #     # --------------------------------
#     #     if len(lista) == 0:
#     #         return False

#     #     # --------------------------------
#     #     # CAMBIAR FRAME
#     #     # --------------------------------
#     #     if self.contador_frame >= self.velocidad_animacion:

#     #         self.indice_frame += 1
#     #         self.contador_frame = 0

#     #         # --------------------------------
#     #         # TERMINO LA ANIMACION
#     #         # --------------------------------
#     #         if self.indice_frame >= len(lista):

#     #             # MUERTE
#     #             if muriendo:

#     #                 self.estado = "muerto"

#     #                 if len(self.muerto) > 0:
#     #                     self.imagen_actual = self.muerto[0]

#     #                 return True

#     #             # ATAQUE / BLOQUEO
#     #             elif atacando or bloqueando:

#     #                 self.indice_frame = 0
#     #                 return True

#     #             # CAMINAR / QUIETO
#     #             else:

#     #                 self.indice_frame = 0

#     #     # --------------------------------
#     #     # FRAME ACTUAL
#     #     # --------------------------------
#     #     self.imagen_actual = lista[self.indice_frame]

#     #     return False

#     def actualizar(
#     self,
#     caminando=False,
#     atacando=False,
#     bloquear=False,
#     muriendo=False):

#         # Si ya murió completamente
#         if self.estado == "muerto":
#             if len(self.muerto) > 0:
#                 self.imagen_actual = self.muerto[0]
#             return True

#         self.contador_frame += 1

#         # =========================
#         # ELEGIR ANIMACIÓN
#         # =========================
#         if muriendo:
#             lista = self.muriendo

#         elif atacando:
#             lista = self.atacar

#         elif bloquear:
#             # Elegí una de las listas de bloqueo
#             lista = self.bloquear00

#         elif caminando:
#             # Dependiendo dirección
#             if self.direccion == 0:
#                 lista = self.caminar0

#             elif self.direccion == 1:
#                 lista = self.caminar1

#             elif self.direccion == 2:
#                 lista = self.caminar2

#         else:
#             lista = self.quieto

#         # =========================
#         # SI NO HAY FRAMES
#         # =========================
#         if len(lista) == 0:
#             return False

#         # =========================
#         # CONTROL DE FRAMES
#         # =========================
#         if self.contador_frame >= self.velocidad_animacion:

#             self.indice_frame += 1

#             # TERMINÓ LA ANIMACIÓN
#             if self.indice_frame >= len(lista):

#                 if muriendo:
#                     self.indice_frame = len(lista) - 1
#                     self.estado = "muerto"

#                     if len(self.muerto) > 0:
#                         self.imagen_actual = self.muerto[0]

#                     return True

#                 elif atacando or bloquear:
#                     self.indice_frame = 0
#                     self.contador_frame = 0
#                     return True

#                 else:
#                     self.indice_frame = 0

#             self.contador_frame = 0

#         # Seguridad
#         if self.indice_frame >= len(lista):
#             self.indice_frame = 0

#         # =========================
#         # ACTUALIZAR IMAGEN
#         # =========================
#         self.imagen_actual = lista[self.indice_frame]

#         return False


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