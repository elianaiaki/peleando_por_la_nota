import pygame
import sys

sys.path.append(".")

from vista.jugador_grafico import JugadorGrafico
from control.controlador import Controlador
from control.controladorGrafico import controladorGrafico
from control.controladorMusica import ControladorMusica
from vista.seleccionar_personaje import seleccionar_personajes
from control.controladorSonido import ControladorSonido

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
    "recursos/escenario_1.png"
).convert()

escenario = pygame.transform.scale(
    escenario,
    (ANCHO, ALTO)
)

fuente = pygame.font.SysFont(None, 36)

# -----------------------------
# SELECCIÓN DE PERSONAJES
# -----------------------------
jugador1, jugador2 = seleccionar_personajes(
    pantalla,
    ANCHO,
    ALTO
)

jugadores = [jugador1, jugador2]

# -----------------------------
# CONFIG SPRITES
# -----------------------------
sprites_config = {

    "alan": {
        "quieto": ("recursos/alan/quieto.png", 512, 512, 12, 1.0),
        "caminar01": ("recursos/alan/caminar01.png", 512, 512, 8, 1.0),
        "caminar02": ("recursos/alan/caminar02.png", 512, 512, 8, 1.0),
        "atacar": ("recursos/alan/atacar.png", 512, 512, 7, 1.0),
        "bloquear00": ("recursos/alan/bloquear00.png", 512, 512, 1, 1.0),
        "bloquear01": ("recursos/alan/bloquear01.png", 512, 512, 8, 1.0),
        "bloquear02": ("recursos/alan/bloquear02.png", 512, 512, 8, 1.0),
        "muriendo": ("recursos/alan/muriendo.png", 512, 512, 6, 1.0),
        "muerto": ("recursos/alan/muerto.png", 512, 512, 1, 1.0),
        "golpeado": ("recursos/alan/golpeado.png", 512, 512, 3, 1.0)
    },

    "eliana": {
        "quieto": ("recursos/eliana/quieto.png", 512, 512, 12, 1.0),
        "caminar01": ("recursos/eliana/caminar01.png", 512, 512, 8, 1.0),
        "caminar02": ("recursos/eliana/caminar02.png", 512, 512, 8, 1.0),
        "atacar": ("recursos/eliana/atacar.png", 512, 512, 7, 1.0),
        "bloquear00": ("recursos/eliana/bloquear00.png", 512, 512, 1, 1.0),
        "bloquear01": ("recursos/eliana/bloquear01.png", 512, 512, 8, 1.0),
        "bloquear02": ("recursos/eliana/bloquear02.png", 512, 512, 8, 1.0),
        "muriendo": ("recursos/eliana/muriendo.png", 512, 512, 7, 1.0),
        "muerto": ("recursos/eliana/muerto.png", 512, 512, 1, 1.0),
        "golpeado": ("recursos/eliana/golpeado.png", 512, 512, 3, 1.0)
    },

    "gabriel": {
        "quieto": ("recursos/gabriel/quieto.png", 512, 512, 12, 1.0),
        "caminar01": ("recursos/gabriel/caminar01.png", 512, 512, 8, 1.0),
        "caminar02": ("recursos/gabriel/caminar02.png", 512, 512, 8, 1.0),
        "atacar": ("recursos/gabriel/atacar.png", 512, 512, 7, 1.0),
        "bloquear00": ("recursos/gabriel/bloquear00.png", 512, 512, 1, 1.0),
        "bloquear01": ("recursos/gabriel/bloquear01.png", 512, 512, 8, 1.0),
        "bloquear02": ("recursos/gabriel/bloquear02.png", 512, 512, 8, 1.0),
        "muriendo": ("recursos/gabriel/muriendo.png", 512, 512, 6, 1.0),
        "muerto": ("recursos/gabriel/muerto.png", 512, 512, 1, 1.0),
        "golpeado": ("recursos/gabriel/golpeado.png", 512, 512, 3, 1.0)
    },

    "gabo": {
        "quieto": ("recursos/gabo/quieto.png", 512, 512, 12, 1.0),
        "caminar01": ("recursos/gabo/caminar01.png", 512, 512, 8, 1.0),
        "caminar02": ("recursos/gabo/caminar02.png", 512, 512, 8, 1.0),
        "atacar": ("recursos/gabo/atacar.png", 512, 512, 8, 1.0),
        "bloquear00": ("recursos/gabo/bloquear00.png", 512, 512, 1, 1.0),
        "bloquear01": ("recursos/gabo/bloquear01.png", 512, 512, 8, 1.0),
        "bloquear02": ("recursos/gabo/bloquear02.png", 512, 512, 8, 1.0),
        "muriendo": ("recursos/gabo/muriendo.png", 512, 512, 6, 1.0),
        "muerto": ("recursos/gabo/muerto.png", 512, 512, 1, 1.0),
        "golpeado": ("recursos/gabo/golpeado.png", 512, 512, 3, 1.0)
    },

    "yiyo": {
        "quieto": ("recursos/yiyo/quieto.png", 512, 512, 12, 1.0),
        "caminar01": ("recursos/yiyo/caminar01.png", 512, 512, 8, 1.0),
        "caminar02": ("recursos/yiyo/caminar02.png", 512, 512, 8, 1.0),
        "atacar": ("recursos/yiyo/atacar.png", 512, 512, 7, 1.0),
        "bloquear00": ("recursos/yiyo/bloquear00.png", 512, 512, 1, 1.0),
        "bloquear01": ("recursos/yiyo/bloquear01.png", 512, 512, 8, 1.0),
        "bloquear02": ("recursos/yiyo/bloquear02.png", 512, 512, 8, 1.0),
        "muriendo": ("recursos/yiyo/muriendo.png", 512, 512, 7, 1.0),
        "muerto": ("recursos/yiyo/muerto.png", 512, 512, 1, 1.0),
        "golpeado": ("recursos/yiyo/golpeado.png", 512, 512, 3, 1.0)
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

    # graficos.append(grafico)
    graficos.append(grafico)

    # jugador 2 empieza mirando izquierda
    if i == 1:
        grafico.direccion_actual = "izquierda"

# -----------------------------
# CARGAR SPRITES
# -----------------------------
# # for grafico, jugador in zip(graficos, jugadores):

# #     animaciones = sprites_config[jugador.nombre]

# #     for tipo_animacion, (
# #         ruta,
# #         ancho,
# #         alto,
# #         columnas,
# #         escala
# #     ) in animaciones.items():

# #         grafico.sprite.cargar_imagenes(
# #             ruta,
# #             ancho,
# #             alto,
# #             columnas,
# #             tipo_animacion,
# #             escala=escala,
# #             mirar_derecha=(i == 0)
# #         )

#     if grafico.sprite.quieto:
#         grafico.sprite.imagen_actual = (
#             grafico.sprite.quieto[0]
#         )

for i, (grafico, jugador) in enumerate(
    zip(graficos, jugadores)
):

    animaciones = sprites_config[jugador.nombre]

    for tipo_animacion, (
        ruta,
        ancho,
        alto,
        columnas,
        escala
    ) in animaciones.items():

        grafico.sprite.cargar_imagenes(
            ruta,
            ancho,
            alto,
            columnas,
            tipo_animacion,
            escala=escala,

            # jugador1 mira derecha
            # jugador2 mira izquierda
            mirar_derecha=(i == 0)
        )

    if grafico.sprite.quieto:

        grafico.sprite.imagen_actual = (
            grafico.sprite.quieto[0]
        )


# -----------------------------
# PAREDES
# -----------------------------
paredes = [
    # pared izquierda
    pygame.Rect(0, 0, 160, ALTO),
    # pared derecha
    pygame.Rect(ANCHO - 170, 0, 30, ALTO)
]
# -----------------------------
# CONTROLADORES
# -----------------------------
controlador_grafico = controladorGrafico(
    pantalla,
    fuente
)

# controlador = Controlador(
#     graficos[0],
#     graficos[1],
#     ANCHO,
#     ALTO
# )

#controlador de sonidos
sonidos = ControladorSonido()

controlador = Controlador(
    graficos[0],
    graficos[1],
    ANCHO,
    ALTO,
    paredes,
    sonidos  # esto es lo único nuevo acá
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
# BUCLE PRINCIPAL
# -----------------------------
while controlador.corriendo:

    # Eventos
    controlador.procesar_eventos()

    # # Movimiento
    # controlador.procesar_teclas()

    # Movimiento
    controlador.procesar_teclas()

    graficos[0].actualizar_direccion(graficos[1])
    graficos[1].actualizar_direccion(graficos[0])

    # Dibujar
    controlador_grafico.dibujar(
        jugadores,
        graficos,
        fondo=escenario
    )

    # Barras de vida
    controlador_grafico.dibujar_barras_vida(
        pantalla,
        jugadores,
        100
    )

    # Actualizar sprites
    # for grafico in graficos:s
    #     grafico.sprite.actualizar()
    for grafico in graficos:
        # grafico.sprite.actualizar(grafico.estado)
        # termino = grafico.sprite.actualizar(grafico.estado)
        termino = grafico.sprite.actualizar(
            grafico.estado,
            grafico.movimiento
        )
        if termino:

                if grafico.estado == "atacar":
                    grafico.estado = "quieto"

                elif grafico.estado == "bloquear":
                    grafico.estado = "quieto"

                elif grafico.estado == "golpeado":
                    grafico.estado = "quieto"

                elif grafico.estado == "muriendo":
                    grafico.estado = "muerto"

    # Música derrota
    if not jugadores[0].estoy_vivo():
        musica.cambiar(ControladorMusica.DERROTA)

    elif not jugadores[1].estoy_vivo():
        musica.cambiar(ControladorMusica.DERROTA)


    # # -----------------------------
    #     # DIBUJAR PAREDES
    #     # -----------------------------
    #     for pared in paredes:
    #         pygame.draw.rect(
    #             pantalla,
    #             (255, 0, 0),
    #             pared,
    #             2
    #         )
    pygame.display.flip()

    reloj.tick(60)

pygame.quit()
sys.exit()

