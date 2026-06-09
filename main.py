import pygame
import sys

sys.path.append(".")

from modelo import Jugador
from modelo.fabricaEnemigo import FabricaEnemigos
from vista.jugador_grafico import JugadorGrafico
from control.controlador import Controlador
from control.controladorGrafico import controladorGrafico
from control.controladorMusica import ControladorMusica
from control.controladorJuego import ControladorJuego
from control.controladorSonido import ControladorSonido  # ← agregado
from vista.menuPrincipal import menu_principal
from vista.menuIa import menu_Ia
from vista.menu1vs1 import menu_1vs1

pygame.init()

# -----------------------------
# CONFIGURACIÓN
# -----------------------------
ANCHO, ALTO = 800, 600

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("PELEANDO POR LA NOTA")

ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

# -----------------------------
# ESCENARIO
# -----------------------------
escenario = pygame.image.load(
    "recursos/escenario_5.png"
).convert()

escenario = pygame.transform.scale(
    escenario,
    (ANCHO, ALTO)
)

fuente = pygame.font.SysFont(None, 36)

# -----------------------------
# MENÚ PRINCIPAL
# -----------------------------
modo = menu_principal(
    pantalla,
    ANCHO,
    ALTO
)

# -----------------------------
# MODO 1 VS 1
# -----------------------------
if modo == "1vs1":

    jugador1, jugador2 = menu_1vs1(
        pantalla,
        ANCHO,
        ALTO
    )

    jugadores = [jugador1, jugador2]

# -----------------------------
# MODO HISTORIA
# -----------------------------
elif modo == "historia":

    from vista.menuIa import menu_Ia

    controlador_juego = ControladorJuego()

    opcion = menu_Ia(
        pantalla,
        ANCHO,
        ALTO
    )

    if opcion == "nueva":
        controlador_juego.nueva_partida()

    elif opcion == "continuar":
        if not controlador_juego.continuar_partida():
            controlador_juego.nueva_partida()

    jugador1 = controlador_juego.jugador
    jugador2 = controlador_juego.enemigo

    jugadores = [jugador1, jugador2]

# -----------------------------
# CONFIG SPRITES
# -----------------------------
sprites_config = {

    "alan": {
        "quieto":     ("recursos/alan/quieto.png",     512, 512, 12, 1.0),
        "caminar01":  ("recursos/alan/caminar01.png",  512, 512,  8, 1.0),
        "caminar02":  ("recursos/alan/caminar02.png",  512, 512,  8, 1.0),
        "atacar":     ("recursos/alan/atacar.png",     512, 512,  7, 1.0),
        "bloquear00": ("recursos/alan/bloquear00.png", 512, 512,  1, 1.0),
        "bloquear01": ("recursos/alan/bloquear01.png", 512, 512,  8, 1.0),
        "bloquear02": ("recursos/alan/bloquear02.png", 512, 512,  8, 1.0),
        "muriendo":   ("recursos/alan/muriendo.png",   512, 512,  6, 1.0),
        "muerto":     ("recursos/alan/muerto.png",     512, 512,  1, 1.0),
        "golpeado":   ("recursos/alan/golpeado.png",   512, 512,  3, 1.0)
    },

    "eliana": {
        "quieto":     ("recursos/eliana/quieto.png",     512, 512, 12, 1.0),
        "caminar01":  ("recursos/eliana/caminar01.png",  512, 512,  8, 1.0),
        "caminar02":  ("recursos/eliana/caminar02.png",  512, 512,  8, 1.0),
        "atacar":     ("recursos/eliana/atacar.png",     512, 512,  7, 1.0),
        "bloquear00": ("recursos/eliana/bloquear00.png", 512, 512,  1, 1.0),
        "bloquear01": ("recursos/eliana/bloquear01.png", 512, 512,  8, 1.0),
        "bloquear02": ("recursos/eliana/bloquear02.png", 512, 512,  8, 1.0),
        "muriendo":   ("recursos/eliana/muriendo.png",   512, 512,  7, 1.0),
        "muerto":     ("recursos/eliana/muerto.png",     512, 512,  1, 1.0),
        "golpeado":   ("recursos/eliana/golpeado.png",   512, 512,  3, 1.0)
    },

    "gabriel": {
        "quieto":     ("recursos/gabriel/quieto.png",     512, 512, 12, 1.0),
        "caminar01":  ("recursos/gabriel/caminar01.png",  512, 512,  8, 1.0),
        "caminar02":  ("recursos/gabriel/caminar02.png",  512, 512,  8, 1.0),
        "atacar":     ("recursos/gabriel/atacar.png",     512, 512,  7, 1.0),
        "bloquear00": ("recursos/gabriel/bloquear00.png", 512, 512,  1, 1.0),
        "bloquear01": ("recursos/gabriel/bloquear01.png", 512, 512,  8, 1.0),
        "bloquear02": ("recursos/gabriel/bloquear02.png", 512, 512,  8, 1.0),
        "muriendo":   ("recursos/gabriel/muriendo.png",   512, 512,  6, 1.0),
        "muerto":     ("recursos/gabriel/muerto.png",     512, 512,  1, 1.0),
        "golpeado":   ("recursos/gabriel/golpeado.png",   512, 512,  3, 1.0)
    },

    "gabo": {
        "quieto":     ("recursos/gabo/quieto.png",     512, 512, 12, 1.0),
        "caminar01":  ("recursos/gabo/caminar01.png",  512, 512,  8, 1.0),
        "caminar02":  ("recursos/gabo/caminar02.png",  512, 512,  8, 1.0),
        "atacar":     ("recursos/gabo/atacar.png",     512, 512,  8, 1.0),
        "bloquear00": ("recursos/gabo/bloquear00.png", 512, 512,  1, 1.0),
        "bloquear01": ("recursos/gabo/bloquear01.png", 512, 512,  8, 1.0),
        "bloquear02": ("recursos/gabo/bloquear02.png", 512, 512,  8, 1.0),
        "muriendo":   ("recursos/gabo/muriendo.png",   512, 512,  6, 1.0),
        "muerto":     ("recursos/gabo/muerto.png",     512, 512,  1, 1.0),
        "golpeado":   ("recursos/gabo/golpeado.png",   512, 512,  3, 1.0)
    },

    "yiyo": {
        "quieto":     ("recursos/yiyo/quieto.png",     512, 512, 12, 1.0),
        "caminar01":  ("recursos/yiyo/caminar01.png",  512, 512,  8, 1.0),
        "caminar02":  ("recursos/yiyo/caminar02.png",  512, 512,  8, 1.0),
        "atacar":     ("recursos/yiyo/atacar.png",     512, 512,  7, 1.0),
        "bloquear00": ("recursos/yiyo/bloquear00.png", 512, 512,  1, 1.0),
        "bloquear01": ("recursos/yiyo/bloquear01.png", 512, 512,  8, 1.0),
        "bloquear02": ("recursos/yiyo/bloquear02.png", 512, 512,  8, 1.0),
        "muriendo":   ("recursos/yiyo/muriendo.png",   512, 512,  7, 1.0),
        "muerto":     ("recursos/yiyo/muerto.png",     512, 512,  1, 1.0),
        "golpeado":   ("recursos/yiyo/golpeado.png",   512, 512,  3, 1.0)
    },

    "profe": {
        "quieto":     ("recursos/profe/quieto.png",     512, 512, 12, 1.2),
        "caminar01":  ("recursos/profe/caminar01.png",  512, 512,  8, 1.2),
        "caminar02":  ("recursos/profe/caminar02.png",  512, 512,  8, 1.2),
        "atacar":     ("recursos/profe/atacar.png",     512, 512,  7, 1.2),
        "bloquear00": ("recursos/profe/bloquear00.png", 512, 512,  1, 1.2),
        "bloquear01": ("recursos/profe/bloquear01.png", 512, 512,  8, 1.2),
        "bloquear02": ("recursos/profe/bloquear02.png", 512, 512,  8, 1.2),
        "muriendo":   ("recursos/profe/muriendo.png",   512, 512,  6, 1.2),
        "muerto":     ("recursos/profe/muerto.png",     512, 512,  1, 1.2),
        "golpeado":   ("recursos/profe/golpeado.png",   512, 512,  3, 1.2)
    }
}

# -----------------------------
# CREAR GRÁFICOS
# -----------------------------
colores = [ROJO, AZUL]

posiciones = [
    (300, 300),
    (480, 300)
]

graficos = []

for i, jugador in enumerate(jugadores):

    x, y = posiciones[i]

    if jugador.nombre == "profe" : 
        y -= 20

    imagen_derrota = pygame.image.load(
        f"recursos/{jugador.nombre}/derrota.png"
    ).convert_alpha()

    grafico = JugadorGrafico(
        x,
        y,
        colores[i],
        jugador,
        imagen_derrota
    )

    graficos.append(grafico)

    # jugador 2 empieza mirando izquierda
    if i == 1:
        grafico.direccion_actual = "izquierda"

# -----------------------------
# CARGAR SPRITES
# -----------------------------
for i, (grafico, jugador) in enumerate(zip(graficos, jugadores)):

    animaciones = sprites_config[jugador.nombre]

    for tipo_animacion, (ruta, ancho, alto, columnas, escala) in animaciones.items():

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

# -----------------------------
# PAREDES
# -----------------------------
paredes = [
    pygame.Rect(0, 0, 160, ALTO),
    pygame.Rect(ANCHO - 170, 0, 30, ALTO)
]

# -----------------------------
# CONTROLADORES
# -----------------------------
controlador_grafico = controladorGrafico(pantalla, fuente)

# Controlador de sonidos ← agregado
sonidos = ControladorSonido()

controlador = Controlador(
    graficos[0],
    graficos[1],
    ANCHO,
    ALTO,
    paredes,
    sonidos  # ← agregado
)

# -----------------------------
# MÚSICA
# -----------------------------
musica = ControladorMusica()
musica.cambiar(ControladorMusica.PELEA)

# -----------------------------
# RELOJ
# -----------------------------
reloj = pygame.time.Clock()

# -----------------------------
# TRANSICIÓN NIVEL
# -----------------------------
esperando_cambio = False
timer_cambio = 0

# -----------------------------
# BUCLE PRINCIPAL
# -----------------------------
while controlador.corriendo:

    controlador.procesar_eventos()
    controlador.procesar_teclas()

    graficos[0].actualizar_direccion(graficos[1])
    graficos[1].actualizar_direccion(graficos[0])

    controlador_grafico.dibujar(jugadores, graficos, fondo=escenario)
    controlador_grafico.dibujar_barras_vida(pantalla, jugadores, 100)

    # Actualizar sprites
    for grafico in graficos:
        termino = grafico.sprite.actualizar(grafico.estado, grafico.movimiento)
        if termino:
            if grafico.estado in ("atacar", "bloquear", "golpeado"):
                grafico.estado = "quieto"
            elif grafico.estado == "muriendo":
                grafico.estado = "muerto"

    # -----------------------------
    # VICTORIA / DERROTA
    # -----------------------------
    if modo == "historia":

        if not jugadores[0].estoy_vivo():
            musica.cambiar(ControladorMusica.DERROTA)

        elif not jugadores[1].estoy_vivo():
            if not esperando_cambio:
                esperando_cambio = True
                timer_cambio = pygame.time.get_ticks()

    else:
        # Modo 1vs1, solo cambia la música
        if not jugadores[0].estoy_vivo() or not jugadores[1].estoy_vivo():
            musica.cambiar(ControladorMusica.DERROTA)

    # -----------------------------
    # CAMBIO DE NIVEL
    # -----------------------------
    if esperando_cambio:

        if pygame.time.get_ticks() - timer_cambio > 1000:

            continuar = controlador_juego.siguiente_nivel()

            if continuar:

                jugador2 = controlador_juego.enemigo
                jugadores[1] = jugador2

                imagen_derrota = pygame.image.load(
                    f"recursos/{jugador2.nombre}/derrota.png"
                ).convert_alpha()

                nuevo_grafico = JugadorGrafico(480, 300, AZUL, jugador2, imagen_derrota)
                nuevo_grafico.direccion_actual = "izquierda"

                animaciones = sprites_config[jugador2.nombre]

                for tipo, (ruta, ancho, alto, columnas, escala) in animaciones.items():
                    nuevo_grafico.sprite.cargar_imagenes(
                        ruta, ancho, alto, columnas, tipo,
                        escala=escala, mirar_derecha=False
                    )

                nuevo_grafico.sprite.imagen_actual = nuevo_grafico.sprite.quieto[0]

                jugadores[1] = jugador2
                graficos[1] = nuevo_grafico

                # Al recrear el controlador también pasamos los sonidos ← agregado
                controlador = Controlador(
                    graficos[0],
                    graficos[1],
                    ANCHO,
                    ALTO,
                    paredes,
                    sonidos  # ← agregado
                )

                controlador_grafico = controladorGrafico(pantalla, fuente)
                imagen_derrota = pygame.image.load(
                    f"recursos/{jugador2.nombre}/derrota.png"
                ).convert_alpha()


            else:
                print("GANASTE EL JUEGO")
                controlador.corriendo = False

            esperando_cambio = False

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
sys.exit()