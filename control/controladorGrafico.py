import pygame

class controladorGrafico:

    def __init__(self, pantalla, fuente, jugador1, jugador2):
        self.pantalla = pantalla
        self.fuente = fuente
        self.jugador1 = jugador1
        self.jugador2 = jugador2

    def dibujar(self, jugador1, jugador2, grafico1, grafico2, fondo=None):
            # Fondo: imagen o color negro si no hay imagen
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

    #def animacion_ulti(self, jugador1, jugador2, grafico1, grafico2):