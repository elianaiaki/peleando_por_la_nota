import random

def ia_basica(grafico_ia, grafico_jugador, controlador, ANCHO, ALTO, paredes):
    """
    Controla al jugador 2 de forma automática usando lógica básica con ifs.
    Persigue al jugador 1 si está lejos, y ataca o bloquea aleatoriamente
    cuando está cerca. No actúa si está en medio de una animación.
    """

    # Si la IA está atacando, golpeada, muriendo o muerta, no hace nada
    if grafico_ia.estado in ["atacar", "golpeado", "muriendo", "muerto"]:
        return

    # Calcula la distancia horizontal entre la IA y el jugador
    dx = grafico_jugador.rect.centerx - grafico_ia.rect.centerx
    distancia = abs(dx)

    # Si está lejos, se acerca al jugador
    if distancia > 150:
        if dx > 0:
            grafico_ia.mover("derecha", 3, ANCHO, ALTO, grafico_jugador, paredes)