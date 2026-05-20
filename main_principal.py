import pygame
import sys

sys.path.append(".")
from modelo.Jugador import Jugador
#from modelo.Ulti import Ulti

from vista.jugador_grafico import JugadorGrafico
#from vista.ulti_grafico import ultiGraficos

from control.controlador import Controlador
from control.controladorGrafico import controladorGrafico

pygame.init()
pygame.mixer.init()  # <<-- INICIALIZA EL SISTEMA DE SONIDO
try:
    
    pygame.mixer.music.load("recursos/")  # ruta al archivo
    pygame.mixer.music.set_volume(0.1)  # volumen entre 0.0 y 1.0
    pygame.mixer.music.play(-1)  # -1 significa repetir en bucle infinito
    print("Música de fondo cargada y en reproducción")
except Exception as e:
    print(f"Error al cargar música: {e}")


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

jugador1 = Jugador("Jugador 1", 100, 10, 5) #ulti1
jugador2 = Jugador("Jugador 2", 100, 8, 6)  #lti2)

# -----------------------------
# VISTA (con vínculo al modelo)
# -----------------------------
grafico1 = JugadorGrafico(100, 300, ROJO, jugador1)
grafico2 = JugadorGrafico(400, 300, AZUL, jugador2)

controladorGrafico = controladorGrafico(pantalla, fuente, jugador1, jugador2)

#GraficosUlti1 = ultiGraficos(150, 300, (0,255,0), ulti1, 800)
#GraficosUlti2 = ultiGraficos(150, 300, (235,226,0), ulti2, 800)

# -----------------------------
# CONTROLADOR
# -----------------------------
controlador = Controlador(grafico1, grafico2, ANCHO, ALTO)

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

    pygame.display.flip()
    reloj.tick(60)
    
pygame.quit()
sys.exit()