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

         # Lista de golpes pendientes, permite encolar golpes sin pisarse entre sí
        self.cola_golpes_j1 = []
        self.cola_golpes_j2 = []

        # Frames antes de aplicar el daño (~0.33s a 60fps), sincroniza el daño con la animación
        self.DELAY = 20

        # Guarda si hay un ataque encolado esperando que termine la animación actual
        self.proximo_ataque_j1 = False
        self.proximo_ataque_j2 = False

        self.sonidos = controlador_sonidos

    def controlar_jugador1(self, teclas):

        # No procesa movimiento si está en medio de una animación importante 
        if self.jugador1.estado in ["atacar", "golpeado", "muriendo", "muerto", "festejo"]:
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
            # No ataca si está golpeado, muriendo o muerto
            if self.jugador1.estado in ["golpeado", "muriendo", "muerto"]:
                return
            # tampoco ataca si el rival ya está muriendo/muerto
            if self.jugador2.estado in ["muriendo", "muerto"]:
                return

            if self.jugador1.estado == "atacar":
                # Si ya está atacando, guarda el próximo para ejecutarlo cuando termine la animación
                # Evita acumular más de un golpe pendiente para que los sonidos no se pisen
                if not self.proximo_ataque_j1 and len(self.cola_golpes_j1) == 0:
                    self.proximo_ataque_j1 = True
            else:
                self.jugador1.estado = "atacar"
                if self.jugador1.obtener_hitbox_ataque().colliderect(self.jugador2.rect):
                    if self.jugador2.estado == "bloquear":
                        print("ATAQUE BLOQUEADO")
                    else:
                         # Solo agrega a la cola si está vacía, evita golpes acumulados
                        if len(self.cola_golpes_j1) == 0:
                            self.cola_golpes_j1.append(self.DELAY)


    def controlar_jugador2(self, teclas):

        # No procesa movimiento si está en medio de una animación importante
        if self.jugador2.estado in ["atacar", "golpeado", "muriendo", "muerto", "festejo"]:
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

            self.jugador2.estado = "caminar"
            self.jugador2.mover("derecha", self.velocidad, self.ancho, self.alto, self.jugador1, self.paredes)
            moviendo = True

        if not moviendo and not teclas[pygame.K_k]:
            self.jugador2.estado = "quieto"


    def acciones_jugador2(self, evento):
        if evento.key == pygame.K_l:
            # No ataca si está golpeado, muriendo o muerto
            if self.jugador2.estado in ["golpeado", "muriendo", "muerto"]:
                return
            # tampoco ataca si el rival ya está muriendo/muerto
            if self.jugador1.estado in ["muriendo", "muerto"]:
                return
        
            if self.jugador2.estado == "atacar":
                # Si ya está atacando, guarda el próximo para ejecutarlo cuando termine la animación
                # Evita acumular más de un golpe pendiente para que los sonidos no se pisen
                if not self.proximo_ataque_j2 and len(self.cola_golpes_j2) == 0:
                    self.proximo_ataque_j2 = True
            else:
                self.jugador2.estado = "atacar"
                if self.jugador2.obtener_hitbox_ataque().colliderect(self.jugador1.rect):
                    if self.jugador1.estado == "bloquear":
                        print("ATAQUE BLOQUEADO")
                    else:
                         # Solo agrega a la cola si está vacía, evita golpes acumulados
                        if len(self.cola_golpes_j2) == 0:
                            self.cola_golpes_j2.append(self.DELAY)



    def procesar_delays(self):
        # --- Jugador 1 ---
        # Procesamos cada golpe pendiente en la cola
        nueva_cola_j1 = []
        for contador in self.cola_golpes_j1:
            contador -= 1
            # En procesar_delays - reproducir_golpe cuando impacta
            if contador == 0:
                # El golpe impacta: aplica daño y reproduce ambos sonidos juntos
                self.jugador1.atacar_a(self.jugador2)
                self.sonidos.reproducir_golpe()        # ← acá, cuando toca
                self.sonidos.reproducir_golpeado(self.jugador2.modelo.nombre)
                self.jugador2.estado = "golpeado"
                if not self.jugador2.modelo.estoy_vivo():
                    self.jugador2.estado = "muriendo"
                     # Cancela golpes pendientes para que no se procesen después de muerto
                    self.cola_golpes_j1 = []
                    # Cancela el ataque encolado también
                    self.proximo_ataque_j1 = False
                    self.sonidos.detener_golpe()
                    self.sonidos.reproducir_muerte(self.jugador2.modelo.nombre)
            else:
                 # Todavía no impacta, lo mantenemos en la cola
                nueva_cola_j1.append(contador)
        self.cola_golpes_j1 = nueva_cola_j1

        # --- Jugador 2 ---
        nueva_cola_j2 = []
        for contador in self.cola_golpes_j2:
            contador -= 1
            if contador == 0:
                # El golpe impacta: aplica daño y reproduce ambos sonidos juntos
                self.jugador2.atacar_a(self.jugador1)
                self.sonidos.reproducir_golpe()
                self.sonidos.reproducir_golpeado(self.jugador1.modelo.nombre)
                self.jugador1.estado = "golpeado"
                if not self.jugador1.modelo.estoy_vivo():
                    self.jugador1.estado = "muriendo"
                    # Cancela golpes pendientes para que no se procesen después de muerto
                    self.cola_golpes_j2 = []
                    # Cancela el ataque encolado también
                    self.proximo_ataque_j2 = False
                    self.sonidos.detener_golpe()
                    self.sonidos.reproducir_muerte(self.jugador1.modelo.nombre)
            else:
                nueva_cola_j2.append(contador)
        self.cola_golpes_j2 = nueva_cola_j2


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
        self.procesar_delays()
        self._procesar_proximos_ataques()

    def _procesar_proximos_ataques(self):

         # Ejecuta el ataque que quedó encolado mientras duraba la animación anterior
        # Jugador 1 --------------------------------------------------------------------------------------------
        if self.proximo_ataque_j1 and self.jugador1.estado not in ["atacar", "golpeado", "muriendo", "muerto"]:
            self.proximo_ataque_j1 = False
            self.jugador1.estado = "atacar"
            # Solo agrega si la cola está vacía, evita golpes acumulados
            if len(self.cola_golpes_j1) == 0:  # solo agrega si la cola está vacía
                if self.jugador1.obtener_hitbox_ataque().colliderect(self.jugador2.rect):
                    if self.jugador2.estado == "bloquear":
                        print("ATAQUE BLOQUEADO")
                    else:
                        self.cola_golpes_j1.append(self.DELAY)

        # Jugador 2 --------------------------------------------------------------------------------------------
        if self.proximo_ataque_j2 and self.jugador2.estado not in ["atacar", "golpeado", "muriendo", "muerto"]:
            self.proximo_ataque_j2 = False
            self.jugador2.estado = "atacar"
            # Solo agrega si la cola está vacía, evita golpes acumulados
            if len(self.cola_golpes_j2) == 0:  # solo agrega si la cola está vacía
                if self.jugador2.obtener_hitbox_ataque().colliderect(self.jugador1.rect):
                    if self.jugador1.estado == "bloquear":
                        print("ATAQUE BLOQUEADO")
                    else:
                        self.cola_golpes_j2.append(self.DELAY)


    def ia_atacar(self):
        """Ataque de la IA usando el mismo sistema que el jugador humano"""
        if self.jugador2.estado in ["golpeado", "muriendo", "muerto", "atacar"]:
            return
        
        self.jugador2.estado = "atacar"
        
        if self.jugador2.obtener_hitbox_ataque().colliderect(self.jugador1.rect):
            if self.jugador1.estado == "bloquear":
                print("ATAQUE BLOQUEADO")
            else:
                if len(self.cola_golpes_j2) == 0:
                    self.cola_golpes_j2.append(self.DELAY)