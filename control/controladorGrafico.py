import pygame

class controladorGrafico:

    # def __init__(self, pantalla, fuente, jugador1, jugador2):
    #     self.pantalla = pantalla
    #     self.fuente = fuente
    #     self.jugador1 = jugador1
    #     self.jugador2 = jugador2

    #     self.jug1 = jugador1
    #     self.jug2 = jugador2

    def __init__(self, pantalla, fuente):
        self.pantalla = pantalla
        self.fuente = fuente
        # ANIMACIÓN MUERTE
        self.animacion_muerte = False
        self.alpha = 0
        self.zoom = 2.0

        self.superficie_negra = pygame.Surface((800, 600))
        self.superficie_negra.fill((0, 0, 0))
        

    def dibujar(self, jugadores, graficos, fondo=None):
        # Fondo: color negro si no hay imagen
        if fondo is not None:
            self.pantalla.blit(fondo, (0, 0))
        else:
            self.pantalla.fill((0, 0, 0))

        for grafico in graficos:
            grafico.dibujar(self.pantalla)
        # # Dibujar jugadores
        # grafico1.dibujar(self.pantalla)
        # grafico2.dibujar(self.pantalla)

        # # Estado de jugadores
        # estado1 = self.fuente.render(jugador1.mostrar_estado(), True, (255,255,255))
        # estado2 = self.fuente.render(jugador2.mostrar_estado(), True, (255,255,255))

        # self.pantalla.blit(estado1, (10, 10))
        # self.pantalla.blit(estado2, (10, 40))

        # Colisión (visual)
        for i in range(len(graficos)):
            for j in range(i + 1, len(graficos)):
                if graficos[i].colisiona_con(graficos[j]):
                    texto = self.fuente.render("¡COLISIÓN!", True, (255,255,255))
                    self.pantalla.blit(texto, (300, 80))

        # ------------------------------------------------------------------------------------------------------
        # Animación de muerte
        self.animacion_de_muerte(jugadores, graficos)
    
    def animacion_de_muerte(self, jugadores, graficos):

        # Detectar muerte
        for jugador in jugadores:
            if jugador.vida <= 0:
                self.animacion_muerte = True

        # Fade a negro
        if self.animacion_muerte:

            self.alpha += 3

            if self.alpha > 255:
                self.alpha = 255

            self.superficie_negra.set_alpha(self.alpha)
            self.pantalla.blit(self.superficie_negra, (0, 0))

        # Pantalla negra completa
        if self.alpha >= 255:

            imagen = None

            # Buscar quién murió
            for jugador, grafico in zip(jugadores, graficos):

                if jugador.estado == "muerto":
                    imagen = grafico.imagen_derrota
                    break

            if imagen is None:
                return

            # Zoom
            ancho = int(800 * self.zoom)
            alto = int(600 * self.zoom)

            imagen_escalada = pygame.transform.scale(
                imagen,
                (ancho, alto)
            )

            x = (800 - ancho) // 2
            y = (600 - alto) // 2

            self.pantalla.blit(imagen_escalada, (x, y))

            # Alejar cámara
            if self.zoom > 1:
                self.zoom -= 0.002

    # def animacion_de_muerte(self, jugadores, graficos):

    #     # DETECTAR MUERTE
    #     for jugador in jugadores:
    #         if jugador.vida <= 0:
    #             self.animacion_muerte = True

    #     # ANIMACIÓN DE MUERTE
    #     if self.animacion_muerte: # Si un jugador murió se activa la animación

    #         self.alpha += 3  # Aumenta la transicion hasta que sea negra

    #         # El alpha no puede pasar de 255
    #         if self.alpha > 255:
    #             self.alpha = 255

    #         self.superficie_negra.set_alpha(self.alpha)# Aplica transparencia a la superficie negra
    #         self.pantalla.blit(self.superficie_negra, (0, 0))# Dibuja la superficie negra encima de toda la pantalla


    #     # Cuando la pantalla ya está completamente negra
    #     if self.alpha >= 255:

    #         # Cambia el tamaño de la imagen usando zoom
    #         ancho = int(800 * self.zoom)
    #         alto = int(600 * self.zoom)
            
    #         # imagen dependiendo de quién murió
    #         if self.jug1.estado == "muerto":
    #             imagen = grafico1.imagen_derrota

    #         elif self.jug2.estado == "muerto":
    #             imagen = grafico2.imagen_derrota

    #         # Escala la imagen
    #         imagen_escalada = pygame.transform.scale(
    #             imagen,
    #             (ancho, alto)
    #         )

    #         # Centra la imagen en pantalla
    #         x = (800 - ancho) // 2
    #         y = (600 - alto) // 2

    #         # Dibuja la imagen escalada
    #         self.pantalla.blit(imagen_escalada, (x, y))

    #         # Va alejando la cámara poco a poco
    #         if self.zoom > 1:
    #             self.zoom -= 0.002
                
    #def animacion_ulti(self, jugador1, jugador2, grafico1, grafico2):

    # def dibujar_barras_vida(self,pantalla,vida_maxima):
    #     """Metodo que dibuja la barra de vida ,con el nombre y la vida del jugador.
    #     recibe por parametros la pantalla_principal, y la vida maxima ."""
    #     FUENTE = pygame.font.SysFont("Arial", 18)#define la fuente y el tamanio
    #     ancho = 100 #para el rectangulo de la barra
    #     alto = 10#para el rectangulo de la barra
        
    #     # Colores
    #     rojo = (255, 0, 0)
    #     verde = (0, 255, 0)
    #     negro = (0, 0, 0)
    #     blanco = (255, 255, 255)

    #     # Posiciones de las barras
    #     x_jugador1 = 20 #posicion en el ancho de la pantalla
    #     y_jugador1 = 20 #ALTURA EN PANTALLA
    #     x_jugador2 = 630 #posicion del lado derecho de la pantalla
    #     y_jugador2 = 20 #ALTURA

    #     # Jugador 1
    #     porcentaje_j1 = max(0, self.jug1.vida / vida_maxima) #calculo del porcentaje de vida que le queda al jugador1
    #     ancho_vida_j1 = int(ancho * porcentaje_j1) #determina cuanto va a ocupar de ancho en la barra dependiendo el porcentaje
    #     """
    #     pygame.draw.rect(...) = dibuja un rectangulo en una pantalla, con un color y una posicion especifica.
    #     pantalla= es el lugar donde se va a dibujar.
    #     color (negro,rojo,verde)= es el color que va a tener el rectangulo.
    #     (x,y,ancho,alto)= indica la posicion y el tamanio del rectangulo
    #     """
    #     pygame.draw.rect(pantalla, negro, (x_jugador1 - 1, y_jugador1 - 1, ancho + 2, alto + 2))  # va a dar un Borde color negro alrededor de la barra roja
    #     pygame.draw.rect(pantalla, rojo, (x_jugador1, y_jugador1, ancho, alto))  # Fondo rojo,va a representar la vida maxima
    #     pygame.draw.rect(pantalla, verde, (x_jugador1, y_jugador1, ancho_vida_j1, alto))  # barra verde,Vida restante o actual del jugador
        
    #     texto_j1 = FUENTE.render(f"{self.jug1.nombre}:{self.jug1.vida}/{vida_maxima}", True, blanco)#guarda en una variable los datos del personaje que apareceran por pantalla.
    #     pantalla.blit(texto_j1, (x_jugador1 + ancho // 2 - texto_j1.get_width() // 2, y_jugador1 + alto + 5)) #muestra el texto en pantalla y lo centra sobre la barra | .get_width() obtiene el ancho del texto, para centrarlo.

    #     # Jugador 2
    #     porcentaje_j2 = max(0, self.jug2.vida / vida_maxima)#calculo del porcentaje de vida que tiene
    #     ancho_vida_j2 = int(ancho * porcentaje_j2) #determina cuanto va a ocupar de ancho en la barra dependiendo el porcentaje
    #     pygame.draw.rect(pantalla, negro, (x_jugador2 - 1, y_jugador2 - 1, ancho + 2, alto + 2))  # Borde
    #     pygame.draw.rect(pantalla, rojo, (x_jugador2, y_jugador2, ancho, alto))  # Fondo rojo
    #     pygame.draw.rect(pantalla, verde, (x_jugador2, y_jugador2, ancho_vida_j2, alto))  # Vida restante
        
    #     texto_j2 = FUENTE.render(f"{self.jug2.nombre}:{self.jug2.vida}/{vida_maxima}", True, blanco)
    #     pantalla.blit(texto_j2, (x_jugador2 + ancho // 2 - texto_j2.get_width() // 2, y_jugador2 + alto + 5))

    def dibujar_barras_vida(self, pantalla, jugadores, vida_maxima):

        posiciones = [
            (20, 20),
            (630, 20),
            (20, 60),
            (630, 60),
            (325, 20)
        ]

        for jugador, (x, y) in zip(jugadores, posiciones):

            porcentaje = max(0, jugador.vida / vida_maxima)
            ancho_vida = int(100 * porcentaje)

            pygame.draw.rect(pantalla, (0,0,0), (x-1, y-1, 102, 12))
            pygame.draw.rect(pantalla, (255,0,0), (x, y, 100, 10))
            pygame.draw.rect(pantalla, (0,255,0), (x, y, ancho_vida, 10))

            texto = self.fuente.render(
                f"{jugador.nombre}: {jugador.vida}",
                True,
                (255,255,255)
            )

            pantalla.blit(texto, (x, y + 15))