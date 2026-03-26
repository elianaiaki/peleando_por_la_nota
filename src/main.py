#main hecho con ia
from Jugador import Jugador
from Personaje import Personaje

def main():
    # Crear jugadores
    jugador1 = Jugador("Jugador 1", fuerza=10, ataque=5)
    jugador2 = Jugador("Jugador 2", fuerza=8, ataque=6)

    print("\n--- ESTADO INICIAL ---")
    jugador1.mostrar_estado()
    jugador2.mostrar_estado()

    # -------- ATAQUE NORMAL --------
    print("\n--- JUGADOR 1 ATACA A JUGADOR 2 ---")
    jugador1.atacar(jugador2)

    jugador1.mostrar_estado()
    jugador2.mostrar_estado()

    # -------- BLOQUEO --------
    print("\n--- JUGADOR 2 BLOQUEA ---")
    jugador2.bloqueo()

    # Jugador 1 vuelve a atacar
    print("\n--- JUGADOR 1 ATACA (JUGADOR 2 BLOQUEA) ---")
    jugador1.atacar(jugador2)

    jugador1.mostrar_estado()
    jugador2.mostrar_estado()

    # Resetear estados
    #jugador1.resetearEstado()
    #jugador2.resetearEstado()

    # -------- ATAQUE HASTA MORIR --------
    print("\n--- ATAQUES HASTA QUE UNO MUERA ---")
    jugador1.atacar(jugador2)
    jugador1.atacar(jugador2)
    jugador1.atacar(jugador2)

    jugador2.mostrar_estado()

    # Verificar si sigue vivo
    if not jugador2.estoy_vivo():
        print(f"{jugador2.nombre} está muerto")

    print("\n--- FIN DE PRUEBA ---")


if __name__ == "__main__":
    main()