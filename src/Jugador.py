from src.Personaje import Personaje
from src.Ulti import Ulti

class Jugador(Personaje):
    """Clase que representa al jugador, hereda de personaje"""
    def __init__(self, nombre, vida, fuerza, ataque, Ulti):
        """constructor de la clase jugador, recibe un parametro de nombre, vida, fuerza, ataque"""
        super().__init__(nombre, vida, fuerza, ataque, Ulti)

    def mostrar_estado(self):
        """Muestra la información completa del jugador"""
        super().mostrar_estado()
        return f"{self.nombre}: Vida = {self.vida}/{self.vida_maxima}, Fuerza={self.fuerza}, Ataque={self.ataque}, Ulti={self.Ulti}"

