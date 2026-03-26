#main hecho con ia
from Jugador import Jugador
from Personaje import Personaje

def main():
    # Crear jugadores
    jugador1 = Jugador("Jugador 1", fuerza=10, ataque=5)
    jugador2 = Jugador("Jugador 2", fuerza=8, ataque=6)

    # Bucle de pelea
    while jugador1.estoy_Vivo() and jugador2.estoy_Vivo():
        
        # Turno jugador 1
        print("\n--- Turno Jugador 1 ---")
        jugador1.atacar(jugador2)
        jugador1.resetearEstado()
        jugador1.mostrar_estado()
        jugador2.mostrar_estado()

        if not jugador2.estoy_Vivo():
            break

        # Turno jugador 2
        print("\n--- Turno Jugador 2 ---")
        jugador2.atacar(jugador1)
        jugador2.resetearEstado()
        jugador1.mostrar_estado()
        jugador2.mostrar_estado()

    # Resultado final
    print("\n--- FIN DEL JUEGO ---")
    if jugador1.estoy_Vivo():
        print(f"Ganador: {jugador1.nombre}")
    else:
        print(f"Ganador: {jugador2.nombre}")


if __name__ == "__main__":
    main()