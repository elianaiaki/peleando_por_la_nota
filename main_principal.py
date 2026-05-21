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

jugador1 = Jugador("eliana", 100, 10, 5) #ulti1
jugador2 = Jugador("alan", 100, 8, 6)  #lti2)

# -----------------------------
# VISTA (con vínculo al modelo)
# -----------------------------
muerte1 = pygame.image.load("recursos/eliana/eliana_derrotada.png") #sprite eliana
muerte2 = pygame.image.load("recursos/gabriel/gabriel_derrotado.png")# sprite gaby


# cargar imágenes
#grafico1 = JugadorGrafico(100, 300, ROJO, jugador1, muerte1)
#grafico2 = JugadorGrafico(400, 300, AZUL, jugador2, muerte2)

grafico1 = JugadorGrafico(100, 300, ROJO, jugador1, muerte1)
grafico2 = JugadorGrafico(400, 300, AZUL, jugador2, muerte2)

# -----------------------------
# CARGAR SPRITES
# -----------------------------
columnas_alan = {
    "quieto": 1,
    "caminar": 8,
    "atacar": 7,
    "bloquear": 1,
    "bloquear_caminando": 8,
    "muriendo": 6,
    "muerto": 1,
    "golpeado": 3
}

columnas_gabriel = {
    "quieto": 1,
    "caminar": 8,
    "atacar": 7,
    "bloquear": 1,
    "bloquear_caminando": 8,
    "muriendo": 6,
    "muerto": 1,
    "golpeado": 3
}

columnas_gabo = {
    "quieto": 1,
    "caminar": 8,
    "atacar": 8,
    "bloquear": 1,
    "bloquear_caminando": 8,
    "muriendo": 6,
    "muerto": 1,
    "golpeado": 3
}

columnas_eliana = {
    "quieto": 1,
    "caminar": 8,
    "atacar": 7,
    "bloquear": 1,
    "bloquear_caminando": 8,
    "muriendo": 7,
    "muerto": 1,
    "golpeado": 3
}

columnas_yiyo = {
    "quieto": 1,
    "caminar": 8,
    "atacar": 7,
    "bloquear": 1,
    "bloquear_caminando": 8,
    "muriendo": 6,
    "muerto": 1,
    "golpeado": 3
}

#rutas de los sprites
sprites_config = {
    "alan": {
        "quieto":    ("recursos/alan/alanbase_bloquear.png",   150, 150, columnas_alan["quieto"], 2.5),
        "caminar":    ("recursos/alan/alanbase_caminar.png",   150, 150, columnas_alan["caminar"], 2.5),
        "atacar":  ("recursos/alan/alanbase_atacar.png", 150, 150, columnas_alan["atacar"], 2.5),
        "bloquear":  ("recursos/alan/alanbase_bloquear_idle.png", 150, 150, columnas_alan["bloquear"], 2.5),
        "bloquear_caminando":   ("recursos/alan/alanbase_bloquear_caminando.png",  150, 150, columnas_alan["bloquear_caminando"], 2.5),
        "muriendo":  ("recursos/alan/alanbasea_caida.png", 150, 150, columnas_alan["muriendo"], 2.5),
        "muerto": ("recursos/alan/alanbase_muerte.png", 150, 150, columnas_alan["muerto"], 2.5),
        "golpeado": ("recursos/alan/alanbase_recibir_golpe.png", 150, 150, columnas_alan["golpeado"], 2.5)
    },
    "eliana": {
        "quieto":    ("recursos/eliana/elianabase_bloquear.png",   150, 150, columnas_alan["quieto"], 2.5),
        "caminar":    ("recursos/eliana/elianabase_caminar.png",   150, 150, columnas_alan["caminar"], 2.5),
        "atacar":  ("recursos/eliana/elianabase_atacar.png", 150, 150, columnas_alan["atacar"], 2.5),
        "bloquear":  ("recursos/eliana/elianabase_bloquear.png", 150, 150, columnas_alan["bloquear"], 2.5),
        "bloquear_caminando":   ("recursos/eliana/elianabase_caminar.png",  150, 150, columnas_alan["bloquear_caminando"], 2.5),
        "muriendo":  ("recursos/eliana/elianabase_caida.png", 150, 150, columnas_alan["muriendo"], 2.5),
        "muerto": ("recursos/eliana/elianabase_muerte.png", 150, 150, columnas_alan["muerto"], 2.5),
        "golpeado": ("recursos/eliana/elianabase_recibir_golpe.png", 150, 150, columnas_alan["golpeado"], 2.5)
    },
    "gabo": {
        "quieto":    ("recursos/gabo/gabonase_bloquear.png",   150, 150, columnas_alan["quieto"], 2.5),
        "caminar":    ("recursos/gabo/gabonase_caminar_adelante.png",   150, 150, columnas_alan["caminar"], 2.5),
        "atacar":  ("recursos/gabo/gabonase_atacar.png", 150, 150, columnas_alan["atacar"], 2.5),
        "bloquear":  ("recursos/gabo/gabonase_bloquear.png", 150, 150, columnas_alan["bloquear"], 2.5),
        "bloquear_caminando":   ("recursos/gabo/gabo_caminar_cubriendose_ADELANTE.png",  150, 150, columnas_alan["bloquear_caminando"], 2.5),
        "muriendo":  ("recursos/gabo/gabonase_caida.png", 150, 150, columnas_alan["muriendo"], 2.5),
        "muerto": ("recursos/gabo/gabonase_muerte.png", 150, 150, columnas_alan["muerto"], 2.5),
        "golpeado": ("recursos/gabo/gabonase_recibir_golpe.png", 150, 150, columnas_alan["golpeado"], 2.5)
    },
}

# for jugadores in [jugador1, jugador2]:
#     nombre = jugadores.nombre
#     animaciones = sprites_config[nombre]
#     for tipo_animacion, (ruta, ancho, alto, columnas, escala) in animaciones.items():
#         jugadores.sprite.cargar_imagenes(ruta, ancho, alto, columnas, tipo_animacion, escala=escala,mirar_derecha=True)
#     if jugadores.sprite.quieto:
#         jugadores.sprite.imagen_actual = jugadores.sprite.quieto[0]

for grafico, jugadores in [(grafico1, jugador1), (grafico2, jugador2)]:

    nombre = jugadores.nombre
    animaciones = sprites_config[jugadores.nombre]

    for tipo_animacion, (ruta, ancho, alto, columnas, escala) in animaciones.items():

        grafico.sprite.cargar_imagenes(ruta, ancho, alto, columnas, tipo_animacion, escala=escala, mirar_derecha=True)

    if grafico.sprite.quieto:
        grafico.sprite.imagen_actual = grafico.sprite.quieto[0]

controladorGrafico = controladorGrafico(pantalla, fuente, jugador1, jugador2)

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
    controladorGrafico.dibujar(jugador1, jugador2, grafico1, grafico2, fondo=escenario)

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