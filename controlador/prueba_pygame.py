import pygame
import sys

sys.path.append(".")
from modelo.Jugador import Jugador

# Inicializamos todos los módulos de Pygame
pygame.init()

# Definimos el tamaño de la ventana
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("PELEANDO POR LA NOTA")

# Colores
NEGRO  = (0,   0,   0)
BLANCO = (255, 255, 255)
ROJO   = (255, 0,   0)
AZUL   = (0,   0,   255)

# Creamos los jugadores lógicos (Entrega 1)
jugador1 = Jugador("Jugador 1", 100, fuerza=10, ataque=5, Ulti="navajaso")
jugador2 = Jugador("Jugador 2", 100, fuerza=8, ataque=6, Ulti="bomba")

# Creamos los rectángulos que representan a cada jugador
rectangulo_jugador1 = pygame.Rect(100, 300, 60, 60)
rectangulo_jugador2 = pygame.Rect(640, 300, 60, 60)

# Velocidad de movimiento y reloj
velocidad = 5
reloj = pygame.time.Clock()

# Fuente para mostrar texto en pantalla
fuente = pygame.font.SysFont(None, 36)

# Cooldown de ataque para que no haga daño en cada frame
cooldown_ataque  = 500  # milisegundos
ultimo_ataque_jugador1 = 0
ultimo_ataque_jugador2 = 0

# Bucle principal
corriendo = True
while corriendo:

    # 1. Gestión de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # 2. Captura de teclas
    teclas = pygame.key.get_pressed()
    tiempo_actual = pygame.time.get_ticks()

    # Movimiento Jugador 1 con WASD
    if teclas[pygame.K_w]:
        rectangulo_jugador1.y -= velocidad
    if teclas[pygame.K_s]:
        rectangulo_jugador1.y += velocidad
    if teclas[pygame.K_a]:
        rectangulo_jugador1.x -= velocidad
    if teclas[pygame.K_d]:
        rectangulo_jugador1.x += velocidad

    # Movimiento Jugador 2 con flechas
    if teclas[pygame.K_UP]:
        rectangulo_jugador2.y -= velocidad
    if teclas[pygame.K_DOWN]:
        rectangulo_jugador2.y += velocidad
    if teclas[pygame.K_LEFT]:
        rectangulo_jugador2.x -= velocidad
    if teclas[pygame.K_RIGHT]:
        rectangulo_jugador2.x += velocidad

    # Límites de pantalla Jugador 1
    if rectangulo_jugador1.left < 0:
        rectangulo_jugador1.left = 0
    if rectangulo_jugador1.right > ANCHO:
        rectangulo_jugador1.right = ANCHO
    if rectangulo_jugador1.top < 0:
        rectangulo_jugador1.top = 0
    if rectangulo_jugador1.bottom > ALTO:
        rectangulo_jugador1.bottom = ALTO

    # Límites de pantalla Jugador 2
    if rectangulo_jugador2.left < 0:
        rectangulo_jugador2.left = 0
    if rectangulo_jugador2.right > ANCHO:
        rectangulo_jugador2.right = ANCHO
    if rectangulo_jugador2.top < 0:
        rectangulo_jugador2.top = 0
    if rectangulo_jugador2.bottom > ALTO:
        rectangulo_jugador2.bottom = ALTO

    # Colisión entre jugadores
    if rectangulo_jugador1.colliderect(rectangulo_jugador2):
        print("Colision detectada!")

        # Jugador 1 ataca con F
        if teclas[pygame.K_f]:
            if tiempo_actual - ultimo_ataque_jugador1 >= cooldown_ataque:
                jugador1.atacar(jugador2)
                ultimo_ataque_jugador1 = tiempo_actual

        # Jugador 2 ataca con L
        if teclas[pygame.K_l]:
            if tiempo_actual - ultimo_ataque_jugador2 >= cooldown_ataque:
                jugador2.atacar(jugador1)
                ultimo_ataque_jugador2 = tiempo_actual

    # Jugador 1 bloquea con E
    if teclas[pygame.K_e]:
        jugador1.bloqueo()

    # Jugador 2 bloquea con K
    if teclas[pygame.K_k]:
        jugador2.bloqueo()

    # 3. Dibujo en pantalla
    pantalla.fill(NEGRO)

    pygame.draw.rect(pantalla, ROJO, rectangulo_jugador1)
    pygame.draw.rect(pantalla, AZUL, rectangulo_jugador2)

    # Texto con la vida de cada jugador
    texto_jugador1 = fuente.render("J1 Vida: " + str(jugador1.vida), True, BLANCO)
    texto_jugador2 = fuente.render("J2 Vida: " + str(jugador2.vida), True, BLANCO)
    pantalla.blit(texto_jugador1, (10, 10))
    pantalla.blit(texto_jugador2, (10, 50))

    # 4. Actualización de pantalla y control de tiempo
    pygame.display.flip()
    reloj.tick(60)

# Cierre ordenado
pygame.quit()
sys.exit()