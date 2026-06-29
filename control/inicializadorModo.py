# =====================================================================
# Inicializa el modo de juego elegido en el menú
# =====================================================================

from vista.menu1vs1 import menu_1vs1
from vista.menuIa import menu_Ia
from control.controladorJuego import ControladorJuego


def inicializar_modo(modo, pantalla, ancho, alto):
    """
    Según el modo elegido en el menú principal, inicializa los jugadores
    y (si aplica) el controlador de juego para el modo historia.

    modo     -- "1vs1" o "historia"
    pantalla -- superficie de pygame
    ancho    -- ancho de la pantalla
    alto     -- alto de la pantalla

    Retorna una tupla (jugadores, controlador_juego) donde:
      - jugadores         -- lista [jugador1, jugador2]
      - controlador_juego -- instancia de ControladorJuego o None si es 1vs1
    """
    if modo == "1vs1":
        return _inicializar_1vs1(pantalla, ancho, alto)

    if modo == "historia":
        return _inicializar_historia(pantalla, ancho, alto)

    raise ValueError(f"Modo desconocido: {modo}")


# -----------------------------
# PRIVADAS
# -----------------------------

def _inicializar_1vs1(pantalla, ancho, alto):
    """Deja que los dos jugadores elijan su personaje y retorna la lista."""
    resultado = menu_1vs1(pantalla, ancho, alto)
    if resultado == (None, None):
        return None, None
    jugador1, jugador2 = resultado
    return [jugador1, jugador2], None


def _inicializar_historia(pantalla, ancho, alto):
    """Muestra el menú de historia, crea o carga la partida y retorna la lista."""
    controlador_juego = ControladorJuego()

    opcion = menu_Ia(pantalla, ancho, alto)

    if opcion == "nueva":
        controlador_juego.nueva_partida()
    elif opcion == "continuar":
        # Si no hay partida guardada, arranca una nueva
        if not controlador_juego.continuar_partida():
            controlador_juego.nueva_partida()
    elif opcion == "volver":
        # Señal para que main vuelva al menú principal
        return None, None

    jugadores = [controlador_juego.jugador, controlador_juego.enemigo]
    return jugadores, controlador_juego