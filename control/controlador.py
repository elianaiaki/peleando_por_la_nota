import pygame

class Controlador:

    def __init__(self, jugador1, jugador2, ancho, alto):

        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.ancho = ancho
        self.alto = alto
        self.velocidad = 5
        self.corriendo = True

    # JUGADOR 1
    def controlar_jugador1(self, teclas):
        # Movimiento
        # if teclas[pygame.K_w]:
        #     self.jugador1.mover("arriba", self.velocidad, self.ancho, self.alto)
        # if teclas[pygame.K_s]:
        #     self.jugador1.mover("abajo", self.velocidad, self.ancho, self.alto)
        # if teclas[pygame.K_a]:
        #     self.jugador1.mover("izquierda", self.velocidad, self.ancho, self.alto)
        # if teclas[pygame.K_d]:
        #     self.jugador1.mover("derecha", self.velocidad, self.ancho, self.alto)

        if teclas[pygame.K_a]:

            self.jugador1.sprite.mirar_derecha = False
            self.jugador1.mover("izquierda", self.velocidad, self.ancho, self.alto)

        if teclas[pygame.K_d]:

            self.jugador1.sprite.mirar_derecha = True
            self.jugador1.mover("derecha", self.velocidad, self.ancho, self.alto)
    def acciones_jugador1(self, evento):
        # Ataque
        if evento.key == pygame.K_f:

            if self.jugador1.colisiona_con(self.jugador2):
                self.jugador1.atacar_a(self.jugador2)

        # Bloqueo
        elif evento.key == pygame.K_e:
            self.jugador1.modelo.bloqueo()

    # =====================================
       # JUGADOR 2
    def controlar_jugador2(self, teclas):
        # Movimiento
        # if teclas[pygame.K_UP]:
        #     self.jugador2.mover("arriba", self.velocidad, self.ancho, self.alto)
        # if teclas[pygame.K_DOWN]:
        #     self.jugador2.mover("abajo", self.velocidad, self.ancho, self.alto)
        # if teclas[pygame.K_LEFT]:
        #     self.jugador2.mover("izquierda", self.velocidad, self.ancho, self.alto)
        # if teclas[pygame.K_RIGHT]:
        #     self.jugador2.mover("derecha", self.velocidad, self.ancho, self.alto)

        if teclas[pygame.K_LEFT]:

            self.jugador2.sprite.mirar_derecha = False
            self.jugador2.mover("izquierda", self.velocidad, self.ancho, self.alto)

        if teclas[pygame.K_RIGHT]:

            self.jugador2.sprite.mirar_derecha = True
            self.jugador2.mover("derecha", self.velocidad, self.ancho, self.alto)
    def acciones_jugador2(self, evento):
        # Ataque
        if evento.key == pygame.K_l:

            if self.jugador2.colisiona_con(self.jugador1):
                self.jugador2.atacar_a(self.jugador1)

        # Bloqueo
        elif evento.key == pygame.K_k:
            self.jugador2.modelo.bloqueo()

    # =====================================
    # EVENTOS
    def procesar_eventos(self):
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                self.corriendo = False

            if evento.type == pygame.KEYDOWN:

                self.acciones_jugador1(evento)
                self.acciones_jugador2(evento)

    # =====================================
    # TECLAS
    # =====================================
    def procesar_teclas(self):

        teclas = pygame.key.get_pressed()

        self.controlar_jugador1(teclas)
        self.controlar_jugador2(teclas)

        