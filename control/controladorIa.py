import random

_cooldown_ia = 0

def ia_basica(grafico_ia, grafico_jugador, controlador_juego, ANCHO, ALTO, paredes, controlador, cooldown_frames=45):
    global _cooldown_ia

    # No actuar si está en animación
    if grafico_ia.estado in ["atacar", "bloquear", "golpeado", "muriendo", "muerto"]:
        return

    nivel = controlador_juego.nivel_actual
    dx = grafico_jugador.rect.centerx - grafico_ia.rect.centerx
    distancia = abs(dx)

    # Movimiento sin cooldown
    if distancia > 150:
        if dx > 0:
            grafico_ia.mover("derecha", 3, ANCHO, ALTO, grafico_jugador, paredes)
        else:
            grafico_ia.mover("izquierda", 3, ANCHO, ALTO, grafico_jugador, paredes)
        return

    # Cooldown solo para atacar/bloquear
    _cooldown_ia += 1
    if _cooldown_ia < cooldown_frames:
        return

    probabilidad_actuar = min(0.4 + (nivel - 1) * 0.1, 0.9)
    if random.random() > probabilidad_actuar:
        return

    _cooldown_ia = 0

    probabilidad_atacar = min(0.5 + (nivel - 1) * 0.05, 0.85)
    if random.random() < probabilidad_atacar:
        controlador.ia_atacar()
    else:
        grafico_ia.modelo.esta_bloqueando = True
        grafico_ia.estado = "bloquear"