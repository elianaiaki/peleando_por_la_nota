import pygame

class Controlador:

    # def __init__(self, jugador1, jugador2, ancho, alto):
    def __init__(self,
    jugador1,
    jugador2,
    ancho,
    alto,
    paredes
    ):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.ancho = ancho
        self.alto = alto
        self.velocidad = 5
        self.corriendo = True
        self.paredes = paredes

    # JUGADOR 1
    # def controlar_jugador1(self, teclas):
        # Movimiento
        # if teclas[pygame.K_w]:
        #     self.jugador1.mover("arriba", self.velocidad, self.ancho, self.alto)
        # if teclas[pygame.K_s]:
        #     self.jugador1.mover("abajo", self.velocidad, self.ancho, self.alto)
        # if teclas[pygame.K_a]:
        #     self.jugador1.mover("izquierda", self.velocidad, self.ancho, self.alto)
        # if teclas[pygame.K_d]:
        #     self.jugador1.mover("derecha", self.velocidad, self.ancho, self.alto)

        # if teclas[pygame.K_a]:

        #     self.jugador1.sprite.mirar_derecha = False
        #     self.jugador1.mover("izquierda", self.velocidad, self.ancho, self.alto)

        # if teclas[pygame.K_d]:

        #     self.jugador1.sprite.mirar_derecha = True
        #     self.jugador1.mover("derecha", self.velocidad, self.ancho, self.alto)

    def controlar_jugador1(self, teclas):

            if self.jugador1.estado in [
                "atacar",
            #    "bloquear", // Comente esto por que me di cuenta que provocaba un retraso en la animacion de bloqueo.
                "golpeado",
                "muriendo",
                "muerto"
            ]:
                return
            
            moviendo = False

            # BLOQUEO   // aca añadi alunas cositas tanto en jugador 1 como en 2
            if teclas[pygame.K_e]:

                self.jugador1.modelo.esta_bloqueando = True
                self.jugador1.estado = "bloquear"

                return

            else:

                self.jugador1.modelo.esta_bloqueando = False

            if teclas[pygame.K_a]:

                self.jugador1.estado = "caminar"

                self.jugador1.mover(
                    "izquierda",
                    self.velocidad,
                    self.ancho,
                    self.alto,
                    self.jugador2,
                    self.paredes
                )

                moviendo = True

            if teclas[pygame.K_d]:

                self.jugador1.estado = "caminar"

                # self.jugador1.mover(
                #     "derecha",
                #     self.velocidad,
                #     self.ancho,
                #     self.alto
                # )

                self.jugador1.mover(
                    "derecha",
                    self.velocidad,
                    self.ancho,
                    self.alto,
                    self.jugador2,
                    self.paredes
                )

                moviendo = True

            if not moviendo:
                self.jugador1.estado = "quieto"


    def acciones_jugador1(self, evento):
        # Ataque
        # if evento.key == pygame.K_f:

        #     if self.jugador1.colisiona_con(self.jugador2):
        #         self.jugador1.atacar_a(self.jugador2)

        if evento.key == pygame.K_f:

            self.jugador1.estado = "atacar"

            # # if self.jugador1.colisiona_con(self.jugador2):
            # if self.jugador1.obtener_hitbox_ataque().colliderect(
            #         self.jugador2.rect
            #     ):

            #     self.jugador1.atacar_a(self.jugador2)

            #     self.jugador2.estado = "golpeado"

            #     if not self.jugador2.modelo.estoy_vivo():
            #         self.jugador2.estado = "muriendo"

            if self.jugador1.obtener_hitbox_ataque().colliderect(
        self.jugador2.rect
    ):

                # SI ESTA BLOQUEANDO NO RECIBE DAÑO
                if self.jugador2.estado == "bloquear":

                    print("ATAQUE BLOQUEADO")

                else:

                    self.jugador1.atacar_a(self.jugador2)

                    self.jugador2.estado = "golpeado"

                    if not self.jugador2.modelo.estoy_vivo():
                        self.jugador2.estado = "muriendo"

        # Bloqueo
        # elif evento.key == pygame.K_e:
        #     self.jugador1.modelo.bloqueo()

        # elif evento.key == pygame.K_e:

        #     self.jugador1.estado = "bloquear"

        #     self.jugador1.modelo.bloqueo()

    # =====================================
       # JUGADOR 2
    # def controlar_jugador2(self, teclas):
    #     # Movimiento
    #     # if teclas[pygame.K_UP]:
    #     #     self.jugador2.mover("arriba", self.velocidad, self.ancho, self.alto)
    #     # if teclas[pygame.K_DOWN]:
    #     #     self.jugador2.mover("abajo", self.velocidad, self.ancho, self.alto)
    #     # if teclas[pygame.K_LEFT]:
    #     #     self.jugador2.mover("izquierda", self.velocidad, self.ancho, self.alto)
    #     # if teclas[pygame.K_RIGHT]:
    #     #     self.jugador2.mover("derecha", self.velocidad, self.ancho, self.alto)

    #     if teclas[pygame.K_LEFT]:

    #         self.jugador2.sprite.mirar_derecha = False
    #         self.jugador2.mover("izquierda", self.velocidad, self.ancho, self.alto)

    #     if teclas[pygame.K_RIGHT]:

    #         self.jugador2.sprite.mirar_derecha = True
    #         self.jugador2.mover("derecha", self.velocidad, self.ancho, self.alto)

    def controlar_jugador2(self, teclas):

        if self.jugador2.estado in [
                "atacar",
                "bloquear",
                "golpeado",
                "muriendo",
                "muerto"
            ]:
                return
        
        moviendo = False
        
        # BLOQUEO
        if teclas[pygame.K_k]:

            self.jugador2.modelo.esta_bloqueando = True
            self.jugador2.estado = "bloquear"

            return

        else:

            self.jugador2.modelo.esta_bloqueando = False
         
        if teclas[pygame.K_LEFT]:

            self.jugador2.estado = "caminar"

            # self.jugador2.mover(
            #     "izquierda",
            #     self.velocidad,
            #     self.ancho,
            #     self.alto
            # )
            self.jugador2.mover(
                "izquierda",
                self.velocidad,
                self.ancho,
                self.alto,
                self.jugador1,
                self.paredes
            )

            
            moviendo = True

        if teclas[pygame.K_RIGHT]:

            self.jugador2.estado = "caminar"

            # self.jugador2.mover(
            #     "derecha",
            #     self.velocidad,
            #     self.ancho,
            #     self.alto
            # )

            self.jugador2.mover(
                "derecha",
                self.velocidad,
                self.ancho,
                self.alto,
                self.jugador1,
                self.paredes
            )
            

            moviendo = True

        if not moviendo:
            self.jugador2.estado = "quieto"

    def acciones_jugador2(self, evento):

        # ATAQUE
        if evento.key == pygame.K_l:

            self.jugador2.estado = "atacar"

            if self.jugador2.obtener_hitbox_ataque().colliderect(
                self.jugador1.rect
            ):

                if self.jugador1.estado == "bloquear":

                    print("ATAQUE BLOQUEADO")

                else:

                    self.jugador2.atacar_a(self.jugador1)

                    self.jugador1.estado = "golpeado"

                    if not self.jugador1.modelo.estoy_vivo():
                        self.jugador1.estado = "muriendo"

        # BLOQUEO
        # elif evento.key == pygame.K_k:

        #     self.jugador2.estado = "bloquear"

        #     self.jugador2.modelo.bloqueo()

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

        