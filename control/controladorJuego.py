from modelo.Jugador import Jugador
from modelo.persistencia import Persistencia
from modelo.fabricaEnemigo import FabricaEnemigos

class ControladorJuego:
    def __init__(self):
        self.persistencia = Persistencia()
        self.persistencia.crear_tablas()

        self.jugador = None
        self.enemigo = None

        self.nivel_actual = 1
        self.id_partida = None

    def nueva_partida(self):
        self.jugador = Jugador("alan", 100, 8, 6)
        self.nivel_actual = 1

        self.id_partida = self.persistencia.guardar_partida(
            self.jugador.nombre,
            self.nivel_actual,
            self.jugador.vida_maxima,
            self.jugador.fuerza,
            self.jugador.ataque
        )

        self.enemigo = FabricaEnemigos.crear_enemigo(self.nivel_actual)

    def guardar_estado(self):

        if self.id_partida is None:
            return

        self.persistencia.actualizar_partida(
            self.id_partida,
            self.nivel_actual,
            self.jugador.vida_maxima,
            self.jugador.fuerza,
            self.jugador.ataque
        )

    def continuar_partida(self):
        fila = self.persistencia.cargar_ultima_partida()

        if fila is None:
            return False

        self.id_partida = fila[0]
        self.jugador = Jugador(
            fila[1],
            fila[3],  # vida_maxima
            fila[4],  # fuerza
            fila[5]   # ataque
        )

        #self.jugador.vida = fila[3]
        self.nivel_actual = fila[2]

        self.enemigo = FabricaEnemigos.crear_enemigo(self.nivel_actual)
        return True
    
    def siguiente_nivel(self):
        self.nivel_actual += 1
        enemigo = FabricaEnemigos.crear_enemigo(self.nivel_actual)
        if enemigo is None:
            return False

        self.jugador.vida = self.jugador.vida_maxima  # ← agregar esta línea

        self.enemigo = enemigo
        self.guardar_estado()
        return True

