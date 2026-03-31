from src.Jugador import Jugador
from src.Personaje import Personaje


def main():
    print("\n===== INICIO DE PRUEBAS =====")

    # -------- CREACIÓN DE PERSONAJES --------
    try:
        jugador1 = Jugador("Jugador 1", 100, fuerza=10, ataque=5)
        jugador2 = Jugador("Jugador 2", 100, fuerza=8, ataque=6)

        npc = Personaje("Enemigo Base", 80, fuerza=6, ataque=4)

    except (TypeError, ValueError) as e:
        print(f"Error al crear personajes: {e}")
        return

    # -------- ESTADO INICIAL --------
    print("\n--- ESTADO INICIAL ---")
    print(jugador1.mostrar_estado())
    print(jugador2.mostrar_estado())
    print(npc.mostrar_estado())

    # -------- ATAQUE ENTRE JUGADORES --------
    print("\n--- JUGADOR 1 ATACA A JUGADOR 2 ---")
    jugador1.atacar(jugador2)

    print(jugador1.mostrar_estado())
    print(jugador2.mostrar_estado())

    # -------- ATAQUE A PERSONAJE BASE --------
    print("\n--- JUGADOR 2 ATACA A NPC ---")
    jugador2.atacar(npc)

    print(npc.mostrar_estado())

    # -------- BLOQUEO --------
    print("\n--- NPC BLOQUEA ---")
    npc.bloqueo()

    print("\nJugador 1 ataca al NPC (bloqueando)...")
    jugador1.atacar(npc)

    print(npc.mostrar_estado())

    # -------- COMBATE HASTA MORIR --------
    print("\n--- COMBATE HASTA LA MUERTE (NPC) ---")
    while npc.estoy_vivo():
        jugador1.atacar(npc)

    print(npc.mostrar_estado())

    # -------- PRUEBA DE ERRORES --------
    print("\n--- PRUEBA DE ERRORES ---")

    try:
        jugador1.recibir_danio(-5)
    except ValueError as e:
        print(f"Error capturado: {e}")

    try:
        jugador_fake = Jugador(123, -10, fuerza="mucho", ataque=5)
    except (TypeError, ValueError) as e:
        print(f"Error capturado: {e}")

    try:
        jugador1.atacar("no soy un personaje")
    except AttributeError as e:
        print(f"Error capturado: {e}")

    print("\n===== FIN DE PRUEBAS =====")


if __name__ == "__main__":
    main()