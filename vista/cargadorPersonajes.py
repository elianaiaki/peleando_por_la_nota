# =====================================================================
# cargadorPersonajes.py — Crea JugadorGrafico con sus sprites cargados
# Ubicación: vista/cargadorPersonajes.py
# =====================================================================

import pygame
from vista.jugador_grafico import JugadorGrafico
from config import SPRITES_CONFIG, ROJO, AZUL

def crear_graficos(jugadores, indices=None):
    """
    Crea los JugadorGrafico para cada jugador sin cargar sprites.

    jugadores -- lista de jugadores
    indices   -- lista de índices reales (0=j1, 1=j2). Por defecto [0, 1].
    Retorna   -- lista de graficos
    """
    # Si no me pasan indices, asumo que es el caso normal:
    # jugadores[0] es el j1 (índice 0) y jugadores[1] es el j2 (índice 1).
    # range(len(jugadores)) genera 0, 1, ..., uno por cada jugador de la lista.
    if indices is None:
        indices = list(range(len(jugadores)))

    colores = [ROJO, AZUL]
    posiciones = [(300, 300), (480, 300)]

    graficos = []

    # zip(jugadores, indices) empareja cada jugador con su índice real.
    # Ejemplo normal:   jugadores=[j1, j2]      indices=[0, 1]
    #                   → (j1, 0), (j2, 1)
    # Ejemplo cambio de nivel: jugadores=[jugador2]  indices=[1]
    #                   → (jugador2, 1)
    # "i" siempre es el índice REAL (0=jugador1, 1=jugador2),
    # no depende de en qué posición esté dentro de la lista que pasamos.
    for jugador, i in zip(jugadores, indices):
        # Uso "i" (no la posición en la lista) para buscar la posición
        # en pantalla y el color que le corresponde a ese jugador.
        x, y = posiciones[i]

        if jugador.nombre == "profe":
            y -= 20

        imagen_derrota = pygame.image.load(
            f"recursos/{jugador.nombre}/derrota.png"
        ).convert_alpha()

        # colores[i] también usa el índice real, así jugador2 siempre
        # es AZUL aunque venga solo en una lista de un elemento.
        grafico = JugadorGrafico(x, y, colores[i], jugador, imagen_derrota)
        graficos.append(grafico)

        # Si el índice real es 1 (jugador2), arranca mirando a la izquierda.
        # Esto funciona tanto si jugadores tiene 2 elementos como si tiene 1.
        if i == 1:
            grafico.direccion_actual = "izquierda"

    return graficos

def cargar_sprites(graficos, jugadores, indices=None, indices_festejo=None):
    """
    ...
    indices_festejo -- lista de índices (0=j1, 1=j2) a los que SÍ hay que
                        cargarles el festejo. Por defecto None significa
                        "a todos" (caso normal del 1vs1, donde cualquiera
                        de los dos puede ganar y festejar).
    """
    if indices is None:
        indices = list(range(len(jugadores)))

    # Si no nos dicen lo contrario, cargamos festejo para todos los índices
    if indices_festejo is None:
        indices_festejo = indices

    for grafico, jugador, i in zip(graficos, jugadores, indices):
        animaciones = SPRITES_CONFIG[jugador.nombre]
        for tipo_animacion, (ruta, ancho, alto, columnas, escala) in animaciones.items():

            # NUEVO: si esta animación es el festejo y este personaje (índice i)
            # no está en la lista de los que necesitan festejo, nos la saltamos.
            # Así evitamos cargar spritesheets de festejo rotos/incompletos
            # de personajes que nunca van a festejar (los enemigos de la IA).
            if tipo_animacion == "festejo01" and i not in indices_festejo:
                print(f"SALTEANDO festejo de {jugador.nombre} (i={i}, indices_festejo={indices_festejo})")
                continue

            grafico.sprite.cargar_imagenes(
                ruta,
                ancho,
                alto,
                columnas,
                tipo_animacion,
                escala=escala,
                mirar_derecha=(i == 0)
            )
            if grafico.sprite.quieto:
                grafico.sprite.imagen_actual = grafico.sprite.quieto[0]