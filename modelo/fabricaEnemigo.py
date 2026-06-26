from modelo.Jugador import Jugador

class FabricaEnemigos:

    @staticmethod
    def crear_enemigo(nivel):

        enemigos = {
            1: Jugador("yiyo", 100, 12, 4),
            2: Jugador("gabo", 100, 15, 3),
            3: Jugador("eliana", 100, 10, 5),
            4: Jugador("lean", 100, 12, 4),
            5: Jugador("cami", 100, 12, 4),
            6: Jugador("gabriel", 100, 12, 4),
            7: Jugador("cliver", 100, 12, 4),
            8: Jugador("profe", 200, 12, 4)
        }

        return enemigos.get(nivel)