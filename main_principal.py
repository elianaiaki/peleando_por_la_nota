import pygame
import sys

sys.path.append(".")
from modelo.Jugador import Jugador
#from modelo.Ulti import Ulti

from vista.jugador_grafico import JugadorGrafico
#from vista.ulti_grafico import ultiGraficos
from vista.sprite_jugador import SpriteJugador

from control.controlador import Controlador
from control.controladorGrafico import controladorGrafico
from control.controladorMusica import ControladorMusica
from vista.seleccionar_personaje import seleccionar_personajes

pygame.init()

# -----------------------------
# CONFIGURACIÓN
# -----------------------------
ANCHO, ALTO = 800, 600 # Tamaño de la ventana
pantalla = pygame.display.set_mode((ANCHO, ALTO)) # Crea la ventana del juego
pygame.display.set_caption("PELEANDO POR LA NOTA") # Título de la ventana

NEGRO  = (0, 0, 0)     # Color de fondo
BLANCO = (255, 255, 255) # Color de texto
ROJO   = (255, 0, 0)   # Color del jugador 1
AZUL   = (0, 0, 255)    # Color del jugador 2
VERDE = (0, 255, 0)    # Color de jugador 3
AMARILLO = (255, 255, 0) # Color de jugador 4
VIOLETA = (238, 130, 238) # Color de jugador 5

# -----------------------------
# ESCENARIO / FONDO
# -----------------------------
escenario = pygame.image.load("recursos/escenario03.png")
escenario = pygame.transform.scale(escenario, (ANCHO, ALTO))

fuente = pygame.font.SysFont(None, 36) # Fuente para mostrar texto en pantalla

# -----------------------------
# MODELO
# -----------------------------

#ulti1 = Ulti("navajazo")
#ulti2 = Ulti("piña")
# jugador1, jugador2 = seleccionar_personajes(pantalla, ANCHO, ALTO)
# jugador1 = Jugador("eliana", 100, 10, 5) #ulti1
# jugador2 = Jugador("alan", 100, 8, 6)  #lti2)
# jugador3 = Jugador("gabriel", 120, 12, 4)
# jugador4 = Jugador("gabo", 80, 15, 3)
# jugador5 = Jugador("yiyo", 90, 11, 5)

# -----------------------------
# VISTA (con vínculo al modelo)
# -----------------------------
muerte1 = pygame.image.load("recursos/eliana/derrota.png") #sprite eliana
muerte2 = pygame.image.load("recursos/alan/derrota.png")# sprite alan
muerte3 = pygame.image.load("recursos/gabriel/derrota.png") 
muerte4 = pygame.image.load("recursos/gabo/derrota.png") 
muerte5 = pygame.image.load("recursos/yiyo/derrota.png")


# cargar imágenes
#grafico1 = JugadorGrafico(100, 300, ROJO, jugador1, muerte1)
#grafico2 = JugadorGrafico(400, 300, AZUL, jugador2, muerte2)

grafico1 = JugadorGrafico(100, 300, ROJO, jugador1, muerte1)
grafico2 = JugadorGrafico(400, 300, AZUL, jugador2, muerte2)
grafico3 = JugadorGrafico(600, 300, VERDE, jugador3, muerte3)
grafico4 = JugadorGrafico(200, 300, AMARILLO, jugador4, muerte4)
grafico5 = JugadorGrafico(500, 300, VIOLETA, jugador5, muerte5)

# -----------------------------
# CARGAR SPRITES
# -----------------------------
columnas_alan = {
    "quieto": 12,
    "caminar01": 8,
    "caminar02": 8,
    "atacar": 7,
    "bloquear00": 1,
    "bloquear01": 8,
    "bloquear02": 8,
    "muriendo": 6,
    "muerto": 1,
    "golpeado": 3
}

columnas_eliana = {
    "quieto":12,
    "caminar01": 8,
    "caminar02": 8,
    "atacar": 7,
    "bloquear00": 1,
    "bloquear01": 8,
    "bloquear02": 8,
    "muriendo": 7,
    "muerto": 1,
    "golpeado": 3
}

columnas_gabriel = {
    "quieto":12,
    "caminar01": 8,
    "caminar02": 8,
    "atacar": 7,
    "bloquear00": 1,
    "bloquear01": 8,
    "bloquear02": 8,
    "muriendo": 6,
    "muerto": 1,
    "golpeado": 3
}

columnas_gabo = {
    "quieto":12,
    "caminar01": 8,
    "caminar02": 8,
    "atacar": 8,
    "bloquear00": 1,
    "bloquear01": 8,
    "bloquear02": 8,
    "muriendo": 6,
    "muerto": 1,
    "golpeado": 3
}

columnas_yiyo = {
    "quieto":12,
    "caminar01": 8,
    "caminar02": 8,
    "atacar": 7,
    "bloquear00": 1,
    "bloquear01": 8,
    "bloquear02": 8,
    "muriendo": 7,
    "muerto": 1,
    "golpeado": 3
}

#rutas de los sprites
sprites_config = {
    "alan": {
        "quieto":    ("recursos/alan/quieto.png", 512, 512, columnas_alan["quieto"], 2.5),
        "caminar01":    ("recursos/alan/caminar01.png",   512, 512, columnas_alan["caminar01"], 2.5),
        "caminar02":    ("recursos/alan/caminar02.png",   512, 512, columnas_alan["caminar02"], 2.5),
        "atacar":  ("recursos/alan/atacar.png", 512, 512, columnas_alan["atacar"], 2.5),
        "bloquear00":  ("recursos/alan/bloquear00.png", 512, 512, columnas_alan["bloquear00"], 2.5),
        "bloquear01":  ("recursos/alan/bloquear01.png", 512, 512, columnas_alan["bloquear01"], 2.5),
        "bloquear02":  ("recursos/alan/bloquear02.png", 512, 512, columnas_alan["bloquear02"], 2.5),
        "muriendo":  ("recursos/alan/muriendo.png", 512, 512, columnas_alan["muriendo"], 2.5),
        "muerto": ("recursos/alan/muerto.png", 512, 512, columnas_alan["muerto"], 2.5),
        "golpeado": ("recursos/alan/golpeado.png", 512, 512, columnas_alan["golpeado"], 2.5)
    },
    "eliana": {
        "quieto":    ("recursos/eliana/quieto.png",   512, 512, columnas_eliana["quieto"], 2.5),
        "caminar01":    ("recursos/eliana/caminar01.png",   512, 512, columnas_eliana["caminar01"], 2.5),
        "caminar02":    ("recursos/eliana/caminar02.png",   512, 512, columnas_eliana["caminar02"], 2.5),
        "atacar":  ("recursos/eliana/atacar.png", 512, 512, columnas_eliana["atacar"], 2.5),
        "bloquear00":  ("recursos/eliana/bloquear00.png", 512, 512, columnas_eliana["bloquear00"], 2.5),
        "bloquear01":  ("recursos/eliana/bloquear01.png", 512, 512, columnas_eliana["bloquear01"], 2.5),
        "bloquear02":  ("recursos/eliana/bloquear02.png", 512, 512, columnas_eliana["bloquear02"], 2.5),
        "muriendo":  ("recursos/eliana/muriendo.png", 512, 512, columnas_eliana["muriendo"], 2.5),
        "muerto": ("recursos/eliana/muerto.png", 512, 512, columnas_eliana["muerto"], 2.5),
        "golpeado": ("recursos/eliana/golpeado.png", 512, 512, columnas_eliana["golpeado"], 2.5)
    },
    "gabriel": {
        "quieto":    ("recursos/gabriel/quieto.png",   512, 512, columnas_gabriel["quieto"], 2.5),
        "caminar01":    ("recursos/gabriel/caminar01.png",   512, 512, columnas_gabriel["caminar01"], 2.5),
        "caminar02":    ("recursos/gabriel/caminar02.png",   512, 512, columnas_gabriel["caminar02"], 2.5),
        "atacar":  ("recursos/gabriel/atacar.png", 512, 512, columnas_gabriel["atacar"], 2.5),
        "bloquear00":  ("recursos/gabriel/bloquear00.png", 512, 512, columnas_gabriel["bloquear00"], 2.5),
        "bloquear01":  ("recursos/gabriel/bloquear01.png", 512, 512, columnas_gabriel["bloquear01"], 2.5),
        "bloquear02":  ("recursos/gabriel/bloquear02.png", 512, 512, columnas_gabriel["bloquear02"], 2.5),
        "muriendo":  ("recursos/gabriel/muriendo.png", 512, 512, columnas_gabriel["muriendo"], 2.5),
        "muerto": ("recursos/gabriel/muerto.png", 512, 512, columnas_gabriel["muerto"], 2.5),
        "golpeado": ("recursos/gabriel/golpeado.png", 512, 512, columnas_gabriel["golpeado"], 2.5)
    },
    "gabo": {
        "quieto":    ("recursos/gabo/quieto.png",   512, 512, columnas_gabo["quieto"], 2.5),
        "caminar01":    ("recursos/gabo/caminar01.png",   512, 512, columnas_gabo["caminar01"], 2.5),
        "caminar02":    ("recursos/gabo/caminar02.png",   512, 512, columnas_gabo["caminar02"], 2.5),
        "atacar":  ("recursos/gabo/atacar.png", 512, 512, columnas_gabo["atacar"], 2.5),
        "bloquear00":  ("recursos/gabo/bloquear00.png", 512, 512, columnas_gabo["bloquear00"], 2.5),
        "bloquear01":  ("recursos/gabo/bloquear01.png", 512, 512, columnas_gabo["bloquear01"], 2.5),
        "bloquear02":  ("recursos/gabo/bloquear02.png", 512, 512, columnas_gabo["bloquear02"], 2.5),
        "muriendo":  ("recursos/gabo/muriendo.png", 512, 512, columnas_gabo["muriendo"], 2.5),
        "muerto": ("recursos/gabo/muerto.png", 512, 512, columnas_gabo["muerto"], 2.5),
        "golpeado": ("recursos/gabo/golpeado.png", 512, 512, columnas_gabo["golpeado"], 2.5)
    },
    "yiyo": {
        "quieto":    ("recursos/eliana/quieto.png",   512, 512, columnas_yiyo["quieto"], 2.5),
        "caminar01":    ("recursos/yiyo/caminar01.png",   512, 512, columnas_yiyo["caminar01"], 2.5),
        "caminar02":    ("recursos/yiyo/caminar02.png",   512, 512, columnas_yiyo["caminar02"], 2.5),
        "atacar":  ("recursos/yiyo/atacar.png", 512, 512, columnas_yiyo["atacar"], 2.5),
        "bloquear00":  ("recursos/yiyo/bloquear00.png", 512, 512, columnas_yiyo["bloquear00"], 2.5),
        "bloquear01":  ("recursos/yiyo/bloquear01.png", 512, 512, columnas_yiyo["bloquear01"], 2.5),
        "bloquear02":  ("recursos/yiyo/bloquear02.png", 512, 512, columnas_yiyo["bloquear02"], 2.5),
        "muriendo":  ("recursos/yiyo/muriendo.png", 512, 512, columnas_yiyo["muriendo"], 2.5),
        "muerto": ("recursos/yiyo/muerto.png", 512, 512, columnas_yiyo["muerto"], 2.5),
        "golpeado": ("recursos/yiyo/golpeado.png", 512, 512, columnas_yiyo["golpeado"], 2.5)
    }
}

# for jugadores in [jugador1, jugador2]:
#     nombre = jugadores.nombre
#     animaciones = sprites_config[nombre]
#     for tipo_animacion, (ruta, ancho, alto, columnas, escala) in animaciones.items():
#         jugadores.sprite.cargar_imagenes(ruta, ancho, alto, columnas, tipo_animacion, escala=escala,mirar_derecha=True)
#     if jugadores.sprite.quieto:
#         jugadores.sprite.imagen_actual = jugadores.sprite.quieto[0]

for grafico, jugadores in [(grafico1, jugador1), (grafico2, jugador2), (grafico3, jugador3), (grafico4, jugador4), (grafico5, jugador5)]:

    nombre = jugadores.nombre
    animaciones = sprites_config[jugadores.nombre]

    for tipo_animacion, (ruta, ancho, alto, columnas, escala) in animaciones.items():

        grafico.sprite.cargar_imagenes(ruta, ancho, alto, columnas, tipo_animacion, escala=escala, mirar_derecha=True)

    if grafico.sprite.quieto:
        grafico.sprite.imagen_actual = grafico.sprite.quieto[0]

# controladorGrafico = controladorGrafico(pantalla, fuente, jugador1, jugador2)
controladorGrafico = controladorGrafico(pantalla, fuente)

#GraficosUlti1 = ultiGraficos(150, 300, (0,255,0), ulti1, 800)
#GraficosUlti2 = ultiGraficos(150, 300, (235,226,0), ulti2, 800)

# -----------------------------
# CONTROLADOR
# -----------------------------
controlador = Controlador(grafico1, grafico2, ANCHO, ALTO)

musica = ControladorMusica()
musica.cambiar(ControladorMusica.PELEA)  # Empieza con música de pelea

reloj = pygame.time.Clock()

# -----------------------------
# BUCLE PRINCIPAL
# ---------------
while controlador.corriendo:
    # Eventos
    controlador.procesar_eventos()
    # Movimiento
    controlador.procesar_teclas()

    # -----------------------------
    # ACTIVAR ULTIS
    # -----------------------------
    #Si la ulti lógica está activa pero la gráfica no, esta se activa 
    #if jugador1.ulti.activa and not GraficosUlti1.activa:
    #    GraficosUlti1.activar(grafico1.rect.x, grafico1.rect.y)

    #if jugador2.ulti.activa and not GraficosUlti2.activa:
    #    GraficosUlti2.activar(grafico2.rect.x, grafico2.rect.y)

    # Actualizar ulti
    #GraficosUlti1.actualizar(800)
    #GraficosUlti2.actualizar(800)

    # Dibujado
    # controladorGrafico.dibujar(jugador1, jugador2, grafico1, grafico2, fondo=escenario)
    controladorGrafico.dibujar(
        [jugador1, jugador2, jugador3, jugador4, jugador5],
        [grafico1, grafico2, grafico3, grafico4, grafico5],
        fondo=escenario
    )

    controladorGrafico.dibujar_barras_vida(
    pantalla,
    [jugador1, jugador2, jugador3, jugador4, jugador5],
    100
    )
    # controladorGrafico.dibujar_barras_vida(pantalla, 100)
    # grafico1.sprite.actualizar()
    # grafico2.sprite.actualizar()
    for grafico in [grafico1, grafico2, grafico3, grafico4, grafico5]:
        grafico.sprite.actualizar()
    # jugador1.actualizar_direccion(jugador2)
    # jugador2.actualizar_direccion(jugador1)

    #GraficosUlti1.dibujar(pantalla)
    #GraficosUlti2.dibujar(pantalla)

    # ---- LÓGICA DE MÚSICA: DERROTA ----
    if not jugador2.estoy_vivo():
        musica.cambiar(ControladorMusica.DERROTA)   # jugador1 ganó
    elif not jugador1.estoy_vivo():
        musica.cambiar(ControladorMusica.DERROTA)    # jugador1 perdió

    pygame.display.flip()
    reloj.tick(60)
    
pygame.quit()
sys.exit()