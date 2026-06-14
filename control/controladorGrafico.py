import pygame

class controladorGrafico:

    def __init__(self, pantalla, fuente):
        self.pantalla = pantalla
        self.fuente = fuente

        # ANIMACIÓN MUERTE
        self.animacion_muerte = False
        self.alpha = 0
        self.zoom = 2.0
        self.superficie_negra = pygame.Surface((800, 600))
        self.superficie_negra.fill((0, 0, 0))

        # FASE FESTEJO
        self.fase_festejo = False
        self.ganador_grafico = None   # JugadorGrafico del ganador
        self.perdedor_grafico = None  # JugadorGrafico del perdedor
        

    def dibujar(self, jugadores, graficos, fondo=None):
        # Fondo: color negro si no hay imagen
        if fondo is not None:
            self.pantalla.blit(fondo, (0, 0))
        else:
            self.pantalla.fill((0, 0, 0))

        for grafico in graficos:
            grafico.dibujar(self.pantalla)
      

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
            

    def cargar_escenarios(self, ancho, alto, modo="1vs1"):
        if modo == "historia":
            self.escenarios = {
                1: pygame.transform.scale(pygame.image.load("recursos/escenarios/escenario_1.png").convert(), (ancho, alto)),
                2: pygame.transform.scale(pygame.image.load("recursos/escenarios/escenario_2.png").convert(), (ancho, alto)),
                3: pygame.transform.scale(pygame.image.load("recursos/escenarios/escenario_3.png").convert(), (ancho, alto)),
                4: pygame.transform.scale(pygame.image.load("recursos/escenarios/escenario_4.png").convert(), (ancho, alto)),
                5: pygame.transform.scale(pygame.image.load("recursos/escenarios/escenario_5.png").convert(), (ancho, alto)),
            }
            
        else:
            self.escenarios = {
                1: pygame.transform.scale(pygame.image.load("recursos/escenarios/escenario_1vs1.png").convert(), (ancho, alto)),
            }

    def obtener_escenario(self, nivel):
        """Devuelve el escenario correspondiente al nivel"""
        return self.escenarios.get(nivel, self.escenarios[1])
    

        
    def resetear_graficos(self, graficos):
        """Resetea el estado y posición de todos los gráficos al inicio de un nuevo nivel"""
        posiciones_x = [300, 480]
        for i, grafico in enumerate(graficos):
            grafico.estado = "quieto"
            grafico.movimiento = "adelante"
            grafico.sprite.indice_frame = 0
            grafico.sprite.contador_frame = 0
            grafico.sprite.imagen_actual = grafico.sprite.quieto[0]
            grafico.rect.x = posiciones_x[i]
            grafico.col_rect.center = grafico.rect.center