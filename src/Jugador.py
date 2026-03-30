from src.Personaje import Personaje

class Jugador(Personaje):
    """Clase que representa al jugador, hereda de personaje"""
    def __init__(self, nombre, vida, fuerza, ataque):
        """constructor de la clase jugador, recibe un parametro de nombre, vida, fuerza, ataque"""
        super().__init__(nombre, vida, fuerza, ataque)
        # CORRECCIÓN: Se eliminó self.vida = vida porque ya lo hace super().__init__()
        # era una línea redundante que pisaba innecesariamente el valor
        # self.vida = vida


    #def resetearEstado(self):
     #   "Reinicia los estados de ataque y bloqueo"
      #  self.esta_atacando = False
       # self.esta_bloqueando = False

    def mostrar_estado(self):
        """Muestra la información completa del jugador"""
        super().mostrar_estado()
        return f"{self.nombre}: Vida = {self.vida}/{self.vida_maxima}, Fuerza={self.fuerza}, Ataque={self.ataque}"

