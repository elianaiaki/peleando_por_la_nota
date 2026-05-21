import pygame

class controladorGrafico:

    def __init__(self, pantalla, fuente, jugador1, jugador2):
        self.pantalla = pantalla
        self.fuente = fuente
        self.jugador1 = jugador1
        self.jugador2 = jugador2

        # ANIMACIÓN MUERTE
        self.animacion_muerte = False
        self.alpha = 0
        self.zoom = 2.0

        self.superficie_negra = pygame.Surface((800, 600))
        self.superficie_negra.fill((0, 0, 0))
        

    def dibujar(self, jugador1, jugador2, grafico1, grafico2, fondo=None):
        # Fondo: color negro si no hay imagen
        if fondo is not None:
            self.pantalla.blit(fondo, (0, 0))
        else:
            self.pantalla.fill((0, 0, 0))

        # Dibujar jugadores
        grafico1.dibujar(self.pantalla)
        grafico2.dibujar(self.pantalla)

        # Estado de jugadores
        estado1 = self.fuente.render(jugador1.mostrar_estado(), True, (255,255,255))
        estado2 = self.fuente.render(jugador2.mostrar_estado(), True, (255,255,255))

        self.pantalla.blit(estado1, (10, 10))
        self.pantalla.blit(estado2, (10, 40))

        # Colisión (visual)
        if grafico1.colisiona_con(grafico2):
            texto = self.fuente.render("¡COLISIÓN!", True, (255,255,255))
            self.pantalla.blit(texto, (300, 80))

        # ------------------------------------------------------------------------------------------------------
        # Animación de muerte
        self.animacion_de_muerte(jugador1, jugador2, grafico1, grafico2)

    def animacion_de_muerte(self, jugador1, jugador2, grafico1, grafico2):

        # DETECTAR MUERTE
        if jugador1.vida <= 0 or jugador2.vida <= 0:
            self.animacion_muerte = True

        # ANIMACIÓN DE MUERTE
        if self.animacion_muerte: # Si un jugador murió se activa la animación

            self.alpha += 3  # Aumenta la transicion hasta que sea negra

            # El alpha no puede pasar de 255
            if self.alpha > 255:
                self.alpha = 255

            self.superficie_negra.set_alpha(self.alpha)# Aplica transparencia a la superficie negra
            self.pantalla.blit(self.superficie_negra, (0, 0))# Dibuja la superficie negra encima de toda la pantalla


        # Cuando la pantalla ya está completamente negra
        if self.alpha >= 255:

            # Cambia el tamaño de la imagen usando zoom
            ancho = int(800 * self.zoom)
            alto = int(600 * self.zoom)
            
            # imagen dependiendo de quién murió
            if jugador1.estado == "muerto":
                imagen = grafico1.imagen_derrota

            elif jugador2.estado == "muerto":
                imagen = grafico2.imagen_derrota

            # Escala la imagen
            imagen_escalada = pygame.transform.scale(
                imagen,
                (ancho, alto)
            )

            # Centra la imagen en pantalla
            x = (800 - ancho) // 2
            y = (600 - alto) // 2

            # Dibuja la imagen escalada
            self.pantalla.blit(imagen_escalada, (x, y))

            # Va alejando la cámara poco a poco
            if self.zoom > 1:
                self.zoom -= 0.002
                
    #def animacion_ulti(self, jugador1, jugador2, grafico1, grafico2):