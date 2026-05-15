import pygame
import sys

sys.path.append(".")
from modelo.Jugador import Jugador
from vista.jugador_grafico import JugadorGrafico
from control.controlador import Controlador
from control.controladorGrafico import controladorGrafico

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

fuente = pygame.font.SysFont(None, 36) # Fuente para mostrar texto en pantalla

# -----------------------------
# MODELO
# -----------------------------
jugador1 = Jugador("Jugador 1", 100, 10, 5, "navajazo")
jugador2 = Jugador("Jugador 2", 100, 8, 6, "piña")

# -----------------------------
# VISTA (con vínculo al modelo)
# -----------------------------
grafico1 = JugadorGrafico(100, 300, ROJO, jugador1)
grafico2 = JugadorGrafico(400, 300, AZUL, jugador2)
controladorGrafico = controladorGrafico(pantalla, fuente, jugador1, jugador2)

# -----------------------------
# CONTROLADOR
# -----------------------------
controlador = Controlador(grafico1, grafico2, ANCHO, ALTO)

reloj = pygame.time.Clock()

# -----------------------------
# BUCLE PRINCIPAL
# ---------------
#--------------

while controlador.corriendo:
    # -----------------------------
    # EVENTOS - ATACAR - BLOQUEAR
    # -----------------------------
    controlador.procesar_eventos()

    # -----------------------------
    # MOVIMIENTO CONTINUO
    # -----------------------------
    controlador.procesar_teclas()

    # -----------------------------
    # DIBUJO
    # -----------------------------
    controladorGrafico.dibujar(jugador1, jugador2, grafico1, grafico2)

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
sys.exit()