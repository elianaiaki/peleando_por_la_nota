import pygame

class Controlador:

    def __init__(self, jugador1, jugador2, ancho, alto):
        """
        El controlador recibe los jugadores gráficos
        y los límites de la pantalla.
        """

        self.jugador1 = jugador1
        self.jugador2 = jugador2

        self.ancho = ancho
        self.alto = alto

        self.velocidad = 5

        self.corriendo = True


    def procesar_eventos(self):
        """
        Procesa eventos discretos:
        cerrar ventana, ataques y bloqueos.
        """

        for evento in pygame.event.get():

            # Cerrar juego
            if evento.type == pygame.QUIT:
                self.corriendo = False


            # Teclas presionadas UNA vez
            if evento.type == pygame.KEYDOWN:

                # -----------------------------
                # ATAQUES
                # -----------------------------

                if evento.key == pygame.K_f:

                    # Solo ataca si colisionan
                    if self.jugador1.colisiona_con(self.jugador2):
                        self.jugador1.atacar_a(self.jugador2)

                elif evento.key == pygame.K_l:

                    if self.jugador2.colisiona_con(self.jugador1):
                        self.jugador2.atacar_a(self.jugador1)


                # -----------------------------
                # BLOQUEOS
                # -----------------------------

                elif evento.key == pygame.K_e:
                    self.jugador1.modelo.bloqueo()

                elif evento.key == pygame.K_k:
                    self.jugador2.modelo.bloqueo()



    def procesar_teclas(self):
        """
        Procesa movimiento continuo.
        """

        teclas = pygame.key.get_pressed()

        # -----------------------------
        # MOVIMIENTO JUGADOR 1
        # -----------------------------

        if teclas[pygame.K_w]:
            self.jugador1.mover("arriba", self.velocidad, self.ancho, self.alto)

        if teclas[pygame.K_s]:
            self.jugador1.mover("abajo", self.velocidad, self.ancho, self.alto)

        if teclas[pygame.K_a]:
            self.jugador1.mover("izquierda", self.velocidad, self.ancho, self.alto)

        if teclas[pygame.K_d]:
            self.jugador1.mover("derecha", self.velocidad, self.ancho, self.alto)


        # -----------------------------
        # MOVIMIENTO JUGADOR 2
        # -----------------------------

        if teclas[pygame.K_UP]:
            self.jugador2.mover("arriba", self.velocidad, self.ancho, self.alto)

        if teclas[pygame.K_DOWN]:
            self.jugador2.mover("abajo", self.velocidad, self.ancho, self.alto)

        if teclas[pygame.K_LEFT]:
            self.jugador2.mover("izquierda", self.velocidad, self.ancho, self.alto)

        if teclas[pygame.K_RIGHT]:
            self.jugador2.mover("derecha", self.velocidad, self.ancho, self.alto)