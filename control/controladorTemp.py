import pygame

class ControladorTemp:

    def __init__(self, duracion=60):
        self.duracion = duracion # Tiempo máximo de la pelea en segundos
        self.inicio = None # Guarda el instante en que comienza el conteo
        self.terminado = False  # Indica si el tiempo ya terminó
        self.resultado = None   # Guarda el resultado cuando termina el tiempo

    def reiniciar(self):
        # Reinicia el conteo desde cero
        self.inicio = pygame.time.get_ticks()
        self.terminado = False
        self.resultado = None

    def detener(self):
        # Detiene el temporizador y vuelve a mostrar el tiempo inicial
        self.inicio = None
        self.terminado = False
        self.resultado = None

    def tiempo_restante(self):
        # Calcula cuántos segundos pasaron
        if self.inicio is None:
            return self.duracion
        transcurrido = (pygame.time.get_ticks() - self.inicio) // 1000
        return max(0,self.duracion - transcurrido) # Devuelve el tiempo restante

    def actualizar(self, jugador1, jugador2):
        # Si el temporizador ya terminó no vuelve a evaluarse
        if self.terminado:
            return
        # Espera hasta que el tiempo llegue a cero
        if self.tiempo_restante() > 0:
            return
        # Marca el temporizador como finalizado
        self.terminado = True
         # Gana quien tenga más vida restante
        vida1 = jugador1.vida
        vida2 = jugador2.vida
        if vida1 > vida2:
            jugador2.recibir_danio(9999)
        elif vida2 > vida1:
            jugador1.recibir_danio(9999)
        # Si ambos tienen la misma vida se declara empate
        else:
            self.resultado = "empate"