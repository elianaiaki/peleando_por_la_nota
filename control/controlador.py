import pygame

class Controlador:

    # def __init__(self, jugador1, jugador2, ancho, alto):
    def __init__(self,
    jugador1,
    jugador2,
    ancho,
    alto,
    paredes, 
    controlador_sonidos
    ):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.ancho = ancho
        self.alto = alto
        self.velocidad = 5
        self.corriendo = True
        self.paredes = paredes

         # Contador de frames que faltan para aplicar el golpe del jugador 1
        self.delay_golpe_j1 = 0
        # Contador de frames que faltan para aplicar el golpe del jugador 2
        self.delay_golpe_j2 = 0
        # Cantidad de frames de delay antes de aplicar el golpe (20 frames = ~0.33 segundos a 60fps)
        self.DELAY = 20

        # Guardamos el controlador de sonidos para usarlo en los golpes
        self.sonidos = controlador_sonidos

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
            
            if self.jugador1.estado in ["atacar", "golpeado", "muriendo", "muerto"]:
                return
            
            moviendo = False

            if teclas[pygame.K_e]:
                self.jugador1.modelo.esta_bloqueando = True
                self.jugador1.estado = "bloquear"

            else:
                self.jugador1.modelo.esta_bloqueando = False
                self.jugador1.estado = "quieto"  # solo resetea si no bloquea

            if teclas[pygame.K_a]:
                self.jugador1.estado = "caminar"  # sobreescribe "bloquear" visualmente
                self.jugador1.mover("izquierda", self.velocidad, self.ancho, self.alto, self.jugador2, self.paredes)
                moviendo = True


            if teclas[pygame.K_d]:
                self.jugador1.estado = "caminar"
                self.jugador1.mover("derecha", self.velocidad, self.ancho, self.alto, self.jugador2, self.paredes)
                moviendo = True

            if not moviendo and not teclas[pygame.K_e]:
                self.jugador1.estado = "quieto"


    def acciones_jugador1(self, evento):
        if evento.key == pygame.K_f:
            self.jugador1.estado = "atacar"
            if self.jugador1.obtener_hitbox_ataque().colliderect(self.jugador2.rect):
                if self.jugador2.estado == "bloquear":
                    print("ATAQUE BLOQUEADO")
                else:
                    # Suena el puñetazo cuando se lanza el golpe
                    self.sonidos.reproducir_golpe()
                    # Arranca la cuenta regresiva para aplicar el daño con delay
                    self.delay_golpe_j1 = self.DELAY

    def controlar_jugador2(self, teclas):

        if self.jugador2.estado in ["atacar", "golpeado", "muriendo", "muerto"]:
            return
        
        moviendo = False
        
        # BLOQUEO
        if teclas[pygame.K_k]:
            self.jugador2.modelo.esta_bloqueando = True
            self.jugador2.estado = "bloquear"

        else:
            self.jugador2.modelo.esta_bloqueando = False
            self.jugador2.estado = "quieto"  # solo resetea si no bloquea
         
        if teclas[pygame.K_LEFT]:

            self.jugador2.estado = "caminar"  # sobreescribe "bloquear" visualmente
            self.jugador2.mover("izquierda", self.velocidad, self.ancho, self.alto, self.jugador1, self.paredes)
            moviendo = True


        if teclas[pygame.K_RIGHT]:

            self.jugador1.estado = "caminar"
            self.jugador1.mover("derecha", self.velocidad, self.ancho, self.alto, self.jugador1, self.paredes)
            moviendo = True

        if not moviendo and not teclas[pygame.K_e]:
            self.jugador2.estado = "quieto"

    def acciones_jugador2(self, evento):
        if evento.key == pygame.K_l:
            self.jugador2.estado = "atacar"
            if self.jugador2.obtener_hitbox_ataque().colliderect(self.jugador1.rect):
                if self.jugador1.estado == "bloquear":
                    print("ATAQUE BLOQUEADO")
                else:
                    # Suena el puñetazo cuando se lanza el golpe
                    self.sonidos.reproducir_golpe()
                    # Arranca la cuenta regresiva para aplicar el daño con delay
                    self.delay_golpe_j2 = self.DELAY

    def procesar_delays(self):
        # Jugador 1
        if self.delay_golpe_j1 > 0:
            self.delay_golpe_j1 -= 1
            if self.delay_golpe_j1 == 0:
                self.jugador1.atacar_a(self.jugador2)
                # Sonido del personaje cuando recibe el golpe
                self.sonidos.reproducir_golpeado(self.jugador2.modelo.nombre)
                self.jugador2.estado = "golpeado"
                if not self.jugador2.modelo.estoy_vivo():
                    self.jugador2.estado = "muriendo"
                    self.sonidos.reproducir_muerte(self.jugador2.modelo.nombre)

        #Jugador 2
        if self.delay_golpe_j2 > 0:
            self.delay_golpe_j2 -= 1
            if self.delay_golpe_j2 == 0:
                self.jugador2.atacar_a(self.jugador1)
                # Sonido del personaje cuando recibe el golpe
                self.sonidos.reproducir_golpeado(self.jugador1.modelo.nombre)
                self.jugador1.estado = "golpeado"
                if not self.jugador1.modelo.estoy_vivo():
                    self.jugador1.estado = "muriendo"
                    self.sonidos.reproducir_muerte(self.jugador1.modelo.nombre)

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
        self.procesar_delays()  # ← esto

        