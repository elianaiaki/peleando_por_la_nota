from Jugador import Jugador

def main():
    print("=== URBAN CHAMPION PYTHON EDITION ===")

    jugador1 = Jugador("Jugador 1", fuerza=5, ataque=3)
    jugador2 = Jugador("Jugador 2", fuerza=4, ataque=4)

    turno = 1

    while jugador1.estoy_Vivo() and jugador2.estoy_Vivo():

        print("\n--- ESTADO ---")
        print(f"{jugador1.nombre}: {jugador1.vida} HP")
        print(f"{jugador2.nombre}: {jugador2.vida} HP")

        if turno == 1:
            actual = jugador1
            enemigo = jugador2
        else:
            actual = jugador2
            enemigo = jugador1

        print(f"\nTurno de {actual.nombre}")
        print("1. Atacar")
        print("2. Bloquear")

        accion = input("Elegí una opción: ")

        if accion == "1":
            actual.atacar(enemigo)

        elif accion == "2":
            actual.bloquear()

        else:
            print("Acción inválida")
            continue  # vuelve a pedir acción

        # 👇 IMPORTANTE: después de la acción, se resuelven estados
        # (el daño ya se aplicó dentro de atacar)

        # Resetear estados de ambos jugadores
        jugador1.resetearEstado()
        jugador2.resetearEstado()

        # Cambiar turno
        turno = 2 if turno == 1 else 1

    print("\n=== FIN DEL JUEGO ===")

    if jugador1.estoy_Vivo():
        print(f"Ganó {jugador1.nombre}")
    else:
        print(f"Ganó {jugador2.nombre}")


main()