import random

_cooldown_ia = 0      # cuenta frames para el cooldown de decisión
_bloqueando = False   # indica si la IA está en medio de un bloqueo sostenido 
_frames_bloqueo = 0   # cuántos frames le quedan al bloqueo actual
_nivel_anterior = 0   # guarda el último nivel visto, para detectar cuando sube
_velocidad_extra = 0  # contador que se incrementa cada vez que sube de nivel


def ia_basica(grafico_ia, grafico_jugador, controlador_juego, ANCHO, ALTO, paredes, controlador, cooldown_frames=45):
    global _cooldown_ia
    global _bloqueando
    global _frames_bloqueo
    global _nivel_anterior
    global _velocidad_extra

    # No actuar si está en animación de ataque, golpe o muerte

    if grafico_ia.estado in ["atacar", "golpeado", "muriendo", "muerto"]:
        return

    nivel = controlador_juego.nivel_actual
    dx = grafico_jugador.rect.centerx - grafico_ia.rect.centerx
    distancia = abs(dx)


    # CONTADOR DE VELOCIDAD POR NIVEL
    # Cada vez que el nivel sube, se incrementa el contador de velocidad extra.
    # que la IA vaya quedando más rápida de forma acumulativa,
    if nivel > _nivel_anterior:
        _velocidad_extra += 1
        _nivel_anterior = nivel

    # BLOQUEO MANTENIDO
    # el bloqueo dure varios frames en vez de ser instantáneo 
    if _bloqueando:
        grafico_ia.modelo.esta_bloqueando = True

        if grafico_ia.estado != "bloquear":
            grafico_ia.estado = "bloquear"

        _frames_bloqueo -= 1  # descuenta un frame de bloqueo

        if _frames_bloqueo <= 0:
            # se terminó el tiempo de bloqueo, vuelve a estado normal
            _bloqueando = False
            grafico_ia.modelo.esta_bloqueando = False
            grafico_ia.estado = "quieto"

        return  # mientras bloquea, no hace nada más

    # Velocidad base + el extra acumulado por el contador de nivel,
    # con un tope máximo para que no se vuelva imposible de jugar
    velocidad = min(2 + _velocidad_extra, 10)

    # ACERCARSE
    # Lógica de movimiento hacia el jugador cuando está lejos
    if distancia > 150:
        grafico_ia.estado = "caminar"

        if dx > 0:
            grafico_ia.mover("derecha", velocidad, ANCHO, ALTO, grafico_jugador, paredes)
        else:
            grafico_ia.mover("izquierda", velocidad, ANCHO, ALTO, grafico_jugador, paredes)

        return

    # RETROCEDER A VECES
    # si está muy pegado al jugador, a veces retrocede en vez de quedarse ahí
    if distancia < 60:
        if random.random() < 0.25:  # 25% de probabilidad de retroceder
            grafico_ia.estado = "caminar"

            if dx > 0:
                grafico_ia.mover("izquierda", velocidad, ANCHO, ALTO, grafico_jugador, paredes)
            else:
                grafico_ia.mover("derecha", velocidad, ANCHO, ALTO, grafico_jugador, paredes)

            return

    # COOLDOWN PARA DECIDIR
    # usa un cooldown configurable por parámetro
    # El cooldown también baja con _velocidad_extra, usando el mismo
    # contador que la velocidad de movimiento. Así la IA "piensa" más rápido
    # a medida que sube de nivel, en vez de quedarse con el cooldown fijo.
    # Le pongo un piso (cooldown_minimo) para que nunca sea instantáneo.
    cooldown_minimo = 15
    cooldown_actual = max(cooldown_frames - _velocidad_extra * 4, cooldown_minimo)

    _cooldown_ia += 1
    if _cooldown_ia < cooldown_actual:
        return

    # Probabilidad de que la IA decida actuar (atacar o bloquear) en este ciclo
    # primero decide SI actúa, y recién después decidir QUÉ hace
    probabilidad_actuar = min(0.4 + (nivel - 1) * 0.1, 0.9)
    if random.random() > probabilidad_actuar:
        return  # esta vez no hace nada, sigue "pensando"

    _cooldown_ia = 0  # reinicia el cooldown porque ya va a actuar

    # -------------------------
    # ATAQUE O BLOQUEO
    # -------------------------
    # Probabilidad de atacar vs bloquear, escalada por nivel
    probabilidad_atacar = min(0.5 + (nivel - 1) * 0.05, 0.85)

    if random.random() < probabilidad_atacar:
        controlador.ia_atacar()
    else:
        # Si decide bloquear, activa el bloqueo sostenido (sección de arriba) con duración aleatoria
        _bloqueando = True
        _frames_bloqueo = random.randint(30, 90)

        grafico_ia.modelo.esta_bloqueando = True
        grafico_ia.estado = "bloquear"