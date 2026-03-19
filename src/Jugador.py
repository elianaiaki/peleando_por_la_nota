from Personaje import Personaje

class Jugador(Personaje):
    def __init__(self, nombre, fuerza, ataque):
        Personaje.__init__(self, vida_maxima=100)
        self.nombre = nombre
        self.posicion_x = 0
        self.fuerza = fuerza
        self.ataque = ataque

    def atacar(self, enemigo):
        self.esta_atacando = True
        danio = self.calcularDanio()
        print(f"{self.nombre} ataca por {danio} daño!")
        enemigo.recibir_Danio(danio)

    def calcularDanio(self):
        return self.fuerza + self.ataque
    
    def bloquear(self):
        self.esta_bloqueando = True
        print(f"{self.nombre} está bloqueando!")

    def actualizar(self):  # Corregido
        if self.vida <= 0:
            self.morir()
        self.resetearEstado()

    def resetearEstado(self):
        self.esta_atacando = False
        self.esta_bloqueando = False

    def mostrar_estado(self):
        super().mostrar_estado()
        print(f"{self.nombre}: Vida = {self.vida}/{self.vida_maxima}, Fuerza={self.fuerza}, Ataque={self.ataque}")

