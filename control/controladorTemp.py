import pygame

class ControladorTemp:

    def __init__(self, duracion=60):

        self.duracion = duracion
        self.inicio = pygame.time.get_ticks()

        self.terminado = False
        self.resultado = None

    def reiniciar(self):

        self.inicio = pygame.time.get_ticks()
        self.terminado = False
        self.resultado = None

    def tiempo_restante(self):

        transcurrido = (
            pygame.time.get_ticks() - self.inicio
        ) // 1000

        return max(
            0,
            self.duracion - transcurrido
        )

    def actualizar(self, jugador1, jugador2):

        if self.terminado:
            return

        if self.tiempo_restante() > 0:
            return

        self.terminado = True

        vida1 = jugador1.vida
        vida2 = jugador2.vida

        if vida1 > vida2:

            self.resultado = "jugador1"

            jugador2.vida = 0
            jugador2.morir()

        elif vida2 > vida1:

            self.resultado = "jugador2"

            jugador1.vida = 0
            jugador1.morir()

        else:

            self.resultado = "empate"