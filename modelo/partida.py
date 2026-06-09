class Partida:

    def __init__(
        self,
        nombre_jugador,
        nivel_actual,
        vida,
        vida_maxima,
        fuerza,
        ataque
    ):

        self.nombre_jugador = nombre_jugador
        self.nivel_actual = nivel_actual

        self.vida = vida
        self.vida_maxima = vida_maxima
        self.fuerza = fuerza
        self.ataque = ataque