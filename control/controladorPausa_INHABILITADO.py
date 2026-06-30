# =====================================================================
# controladorPausa.py
#
# Controla el menú que aparece al presionar ESC durante la partida.
#
# Opciones:
#   - Continuar
#   - Volver al menú principal
#   - Salir del juego

# De momento esta INHABILITADO ya que se añadio un sistema mas simple para volver al menu principal o salir del juego. Este controlador no se elimino por si a futuro se deciden añadir mejoras en cuanto a configuraciones del mismo.
# =====================================================================

import pygame


class ControladorPausa:

    def __init__(self, pantalla, fuente):

        # ------------------------------------------------------------
        # Guarda la pantalla y la fuente para poder dibujar el menú.
        # ------------------------------------------------------------
        self.pantalla = pantalla
        self.fuente = fuente

        # ------------------------------------------------------------
        # Indica cuál opción está seleccionada.
        #
        # 0 = Continuar
        # 1 = Menú Principal
        # 2 = Salir
        # ------------------------------------------------------------
        self.seleccion = 0

        # ------------------------------------------------------------
        # Lista de opciones que aparecerán en pantalla.
        # ------------------------------------------------------------
        self.opciones = [
            "Continuar",
            "Menu Principal",
            "Salir"
        ]

        # ------------------------------------------------------------
        # Colores
        # ------------------------------------------------------------
        self.color_normal = (255, 255, 255)
        self.color_seleccion = (255, 220, 0)

    # ================================================================
    # DIBUJAR MENÚ
    # ================================================================
    def dibujar(self):

        # ------------------------------------------------------------
        # Crea una superficie negra con transparencia.
        #
        # Esto produce el efecto de "oscurecer" la pelea sin borrarla.
        # ------------------------------------------------------------
        fondo = pygame.Surface(self.pantalla.get_size())

        fondo.set_alpha(170)

        fondo.fill((0, 0, 0))

        self.pantalla.blit(fondo, (0, 0))

        # ------------------------------------------------------------
        # Título
        # ------------------------------------------------------------
        titulo = self.fuente.render("PAUSA", True, (255, 255, 255))

        self.pantalla.blit(
            titulo,
            (
                self.pantalla.get_width() // 2 - titulo.get_width() // 2,
                120
            )
        )

        # ------------------------------------------------------------
        # Dibuja las opciones.
        # ------------------------------------------------------------
        for i, opcion in enumerate(self.opciones):

            # La opción seleccionada cambia de color.
            if i == self.seleccion:
                color = self.color_seleccion
            else:
                color = self.color_normal

            texto = self.fuente.render(opcion, True, color)

            self.pantalla.blit(
                texto,
                (
                    self.pantalla.get_width() // 2 - texto.get_width() // 2,
                    230 + i * 60
                )
            )

    # ================================================================
    # MANEJO DE EVENTOS
    # ================================================================
    def manejar_eventos(self, eventos):    # Recibe la lista de eventos del menú de pausa.
        # ------------------------------------------------------------
        # Recorre todos los eventos enviados por pygame.
        # ------------------------------------------------------------
        for evento in eventos:             # Recorre todos los eventos enviados por el bucle del menú.

            # --------------------------------------------------------
            # Si el jugador cerró la ventana.
            # --------------------------------------------------------
            if evento.type == pygame.QUIT:
                return "salir"

            # --------------------------------------------------------
            # Solo reaccionamos cuando se presiona una tecla.
            # --------------------------------------------------------
            if evento.type == pygame.KEYDOWN:

                # ----------------------------------------------------
                # Flecha arriba.
                # ----------------------------------------------------
                if evento.key == pygame.K_UP:

                    self.seleccion -= 1

                    # Si se pasa del comienzo,
                    # vuelve a la última opción.
                    if self.seleccion < 0:
                        self.seleccion = len(self.opciones) - 1

                # ----------------------------------------------------
                # Flecha abajo.
                # ----------------------------------------------------
                elif evento.key == pygame.K_DOWN:

                    self.seleccion += 1

                    # Si se pasa del final,
                    # vuelve al comienzo.
                    if self.seleccion >= len(self.opciones):
                        self.seleccion = 0

                # ----------------------------------------------------
                # ENTER confirma la opción elegida.
                # ----------------------------------------------------
                elif evento.key == pygame.K_RETURN:

                    if self.seleccion == 0:
                        return "continuar"

                    elif self.seleccion == 1:
                        return "menu"

                    elif self.seleccion == 2:
                        return "salir"

                # ----------------------------------------------------
                # Si vuelve a presionar ESC,
                # simplemente continúa la pelea.
                # ----------------------------------------------------
                elif evento.key == pygame.K_ESCAPE:

                    return "continuar"

        # ------------------------------------------------------------
        # Si todavía no eligió ninguna opción,
        # seguimos mostrando el menú.
        # ------------------------------------------------------------
        return None