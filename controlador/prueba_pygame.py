import pygame
import sys

sys.path.append(".")
from modelo.Jugador import Jugador
from vista.jugador_grafico import JugadorGrafico

pygame.init()

ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("PELEANDO POR LA NOTA")

NEGRO  = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO   = (255, 0, 0)
AZUL   = (0, 0, 255)

# MODELO
jugador1 = Jugador("Jugador 1", 100, 10, 5, "navajazo")
jugador2 = Jugador("Jugador 2", 100, 8, 6, "piña")

# VISTA
grafico1 = JugadorGrafico(100, 300, 60, 60, ROJO)
grafico2 = JugadorGrafico(640, 300, 60, 60, AZUL)

velocidad = 5
reloj = pygame.time.Clock()
fuente = pygame.font.SysFont(None, 36)

cooldown_ataque = 500
ultimo_ataque_jugador1 = 0
ultimo_ataque_jugador2 = 0

corriendo = True
while corriendo:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    teclas = pygame.key.get_pressed()
    tiempo_actual = pygame.time.get_ticks()

    # MOVIMIENTO
    if teclas[pygame.K_w]:
        grafico1.mover(0, -velocidad)
    if teclas[pygame.K_s]:
        grafico1.mover(0, velocidad)
    if teclas[pygame.K_a]:
        grafico1.mover(-velocidad, 0)
    if teclas[pygame.K_d]:
        grafico1.mover(velocidad, 0)

    if teclas[pygame.K_UP]:
        grafico2.mover(0, -velocidad)
    if teclas[pygame.K_DOWN]:
        grafico2.mover(0, velocidad)
    if teclas[pygame.K_LEFT]:
        grafico2.mover(-velocidad, 0)
    if teclas[pygame.K_RIGHT]:
        grafico2.mover(velocidad, 0)

    # LIMITES
    grafico1.limitar_pantalla(ANCHO, ALTO)
    grafico2.limitar_pantalla(ANCHO, ALTO)

    # COLISION
    if grafico1.colisiona_con(grafico2):

        if teclas[pygame.K_f]:
            if tiempo_actual - ultimo_ataque_jugador1 >= cooldown_ataque:
                jugador1.atacar(jugador2)
                ultimo_ataque_jugador1 = tiempo_actual

        if teclas[pygame.K_l]:
            if tiempo_actual - ultimo_ataque_jugador2 >= cooldown_ataque:
                jugador2.atacar(jugador1)
                ultimo_ataque_jugador2 = tiempo_actual

    # BLOQUEO
    if teclas[pygame.K_e]:
        jugador1.bloqueo()

    if teclas[pygame.K_k]:
        jugador2.bloqueo()

    # DIBUJO
    pantalla.fill(NEGRO)

    grafico1.dibujar(pantalla)
    grafico2.dibujar(pantalla)

    texto1 = fuente.render(f"J1 Vida: {jugador1.vida}", True, BLANCO)
    texto2 = fuente.render(f"J2 Vida: {jugador2.vida}", True, BLANCO)

    pantalla.blit(texto1, (10, 10))
    pantalla.blit(texto2, (10, 50))

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
sys.exit()