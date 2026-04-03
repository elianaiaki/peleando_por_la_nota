import pygame
import sys

pygame.init()

ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))

pygame.display.set_caption("Mi primer juego con pygame")

NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

corriendo = True

reloj = pygame.time.Clock()

rect_rojo = pygame.Rect(100, 100, 60, 60)
rect_azul = pygame.Rect(300, 200, 60, 60)

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    pantalla.fill(NEGRO)

    pygame.draw.rect(pantalla, ROJO, rect_rojo)
    pygame.draw.rect(pantalla, AZUL, rect_azul)

    pygame.display.flip()

    reloj.tick(60)

    velocidad = 5

    teclas = pygame.key.get_pressed()

    if  teclas[pygame.K_w]:
        rect_rojo.y -= velocidad
    if  teclas[pygame.K_s]:
        rect_rojo.y += velocidad
    if  teclas[pygame.K_a]:
        rect_rojo.x -= velocidad
    if  teclas[pygame.K_d]:
        rect_rojo.x += velocidad

    if  teclas[pygame.K_UP]:
        rect_azul.y -= velocidad
    if  teclas[pygame.K_DOWN]:
        rect_azul.y += velocidad
    if  teclas[pygame.K_LEFT]:
        rect_azul.x -= velocidad
    if  teclas[pygame.K_RIGHT]:
        rect_azul.x += velocidad

pygame.quit()
sys.exit()