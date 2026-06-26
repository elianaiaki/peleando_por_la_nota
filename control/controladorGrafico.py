import pygame

class controladorGrafico:

    def __init__(self, pantalla, fuente):
        self.pantalla = pantalla
        self.fuente = fuente

        # HUD
        self.imagen_barra_vida = pygame.image.load("recursos/barraVida.png").convert_alpha()
        self.imagen_barra_vida = pygame.transform.scale(self.imagen_barra_vida,(300,40))
        self.imagen_barra_llena = pygame.image.load("recursos/barraVidallena.png").convert_alpha()
        self.imagen_barra_llena = pygame.transform.scale(self.imagen_barra_llena,(300,40))
        self.imagen_barra_vacia = pygame.image.load("recursos/barraVidavacia.png").convert_alpha()
        self.imagen_barra_vacia = pygame.transform.scale(self.imagen_barra_vacia,(300,40))
        # NUMEROS DEL TEMPORIZADOR
        self.sprite_numeros = pygame.image.load("recursos/tempo-sheet.png").convert_alpha()
        self.tamaño_numero = 64
        # LETRAS DE LOS NOMBRES
        self.sprite_letras = pygame.image.load("recursos/letras.png").convert_alpha()
        self.tamaño_letra = 64
        self.escala_letra = 0.35

        # ANIMACIÓN MUERTE
        self.animacion_muerte = False
        self.alpha = 0
        self.zoom = 2.0
        self.superficie_negra = pygame.Surface((800, 600))
        self.superficie_negra.fill((0, 0, 0))
        self.contador_derrota = 0
        self.duracion_derrota = 180

        # FASE FESTEJO
        self.fase_festejo = False

        self.ganador_grafico = None   # JugadorGrafico del ganador
        self.perdedor_grafico = None  # JugadorGrafico del perdedor

        self.mostrar_festejo = True
        self.contador_festejo = 0
        self.duracion_festejo = 580  # cuántos frames dura el festejo en pantalla

        self.fondo_actual = None   # acá guardamos el último fondo que se dibujó, para poder reusarlo en el festejo

        self.festejo_termino = False  # para saber si ya pasamos por el festejo (y no repetirlo)
        self.solo_jugador1_festeja = False  # en 1vs1 cualquiera de los dos puede festejar


    #def dibujar(self, jugadores, graficos, fondo=None):
     #   self.fondo_actual = fondo   # nuevo: lo guardamos para usarlo después en el festejo
      #  # Fondo: color negro si no hay imagen
       # if fondo is not None:
        #    self.pantalla.blit(fondo, (0, 0))
        #else:
         #   self.pantalla.fill((0, 0, 0))

        #for grafico in graficos:
         #   grafico.dibujar(self.pantalla)

    def dibujar(self, jugadores, graficos, temporizador=None, fondo=None):

        self.fondo_actual = fondo
        if fondo is not None:
            self.pantalla.blit(fondo,(0,0))
        else:
            self.pantalla.fill((0,0,0))

        # Dibuja los personajes en pantalla
        for grafico in graficos:
            grafico.dibujar(self.pantalla)

        # HUD
        # Dibuja las barras de vida y los nombres
        self.dibujar_barra_sprite(self.pantalla,jugadores[0],30,25,False)
        self.dibujar_barra_sprite(self.pantalla,jugadores[1],470,25,True)

        # TEMPORIZADOR
        # Solo dibuja el temporizador si fue enviado
        if temporizador is not None:
            self.dibujar_temporizador_sprite(self.pantalla, temporizador)

        # ------------------------------------------------------------------------------------------------------
        # Animación de muerte, solo se ejecuta cuando corresponde.
        self.animacion_de_muerte(jugadores, graficos)


    def animacion_de_muerte(self, jugadores, graficos):
        # Detectamos que la animación de "muriendo" ya terminó de verdad
        for grafico in graficos:
            if grafico.estado == "muerto":
                self.animacion_muerte = True

        if not self.animacion_muerte:
            return

        # Identificamos ganador y perdedor UNA sola vez, apenas arranca todo esto
        if self.ganador_grafico is None and self.perdedor_grafico is None:
            for jugador, grafico in zip(jugadores, graficos):
                if jugador.estoy_vivo():
                    self.ganador_grafico = grafico
                else:
                    self.perdedor_grafico = grafico

            #este modo solo permite que festeje jugadores[0] (Alan)
            # y quien ganó no es jugadores[0], cancelamos el festejo de esta pelea
            if self.solo_jugador1_festeja and self.ganador_grafico is not graficos[0]:
                self.mostrar_festejo = False

        # ------------------------------------------------------------
        # FASE 1: festejo del ganador, ANTES de que se ponga todo negro.
        # El escenario sigue visible de fondo, igual que durante la pelea.
        # ------------------------------------------------------------
        if self.mostrar_festejo and not self.festejo_termino:
            self.fase_festejo = True
            self.ganador_grafico.estado = "festejo"

            if self.fondo_actual is not None:
                self.pantalla.blit(self.fondo_actual, (0, 0))
            else:
                self.pantalla.fill((0, 0, 0))
            self.perdedor_grafico.dibujar(self.pantalla)
            self.ganador_grafico.dibujar(self.pantalla)

            self.contador_festejo += 1
            if self.contador_festejo >= self.duracion_festejo:
                self.festejo_termino = True
                self.fase_festejo = False  # el festejo ya terminó, ahora arranca el fundido
            return

        # ------------------------------------------------------------
        # FASE 2: fundido a negro y, recién cuando ya está todo tapado,
        # la imagen de derrota (con su zoom).
        # Esto se repite TODOS los frames para que el negro se mantenga
        # sólido detrás de la imagen de derrota (si no, se vería el
        # escenario por los bordes).
        # ------------------------------------------------------------
        self.alpha += 3
        if self.alpha > 255:
            self.alpha = 255
        self.superficie_negra.set_alpha(self.alpha)
        self.pantalla.blit(self.superficie_negra, (0, 0))

        if self.alpha >= 255:
            self._mostrar_imagen_derrota(jugadores, graficos)



    def _mostrar_imagen_derrota(self, jugadores, graficos):
        grafico_muerto = None
        for jugador, grafico in zip(jugadores, graficos):
            if jugador.estado == "muerto":
                grafico_muerto = grafico
                break
        if grafico_muerto is None:
            return

        imagen = grafico_muerto.imagen_derrota
        ancho = int(800 * self.zoom)
        alto = int(600 * self.zoom)
        imagen_escalada = pygame.transform.scale(imagen, (ancho, alto))
        x = (800 - ancho) // 2
        y = (600 - alto) // 2
        self.pantalla.blit(imagen_escalada, (x, y))

        if self.zoom > 1:
            self.zoom -= 0.002

        self.contador_derrota += 1

    
    def dibujar_barras_vida(self, pantalla, jugadores, vida_maxima):

        posiciones = [(20, 20),(630, 20),(20, 60),(630, 60),(325, 20)]
        for jugador, (x, y) in zip(jugadores, posiciones):
            porcentaje = max(0, jugador.vida / vida_maxima) # Calcula el porcentaje de vida restante
            ancho_vida = int(100 * porcentaje)
            pygame.draw.rect(pantalla, (0,0,0), (x-1, y-1, 102, 12))
            pygame.draw.rect(pantalla, (255,0,0), (x, y, 100, 10))
            pygame.draw.rect(pantalla, (0,255,0), (x, y, ancho_vida, 10))
            texto = self.fuente.render(f"{jugador.nombre}: {jugador.vida}",True,(255,255,255))
            pantalla.blit(texto, (x, y + 15))
    
    def dibujar_barra_sprite(self, pantalla, jugador, x, y, invertida=False):
        porcentaje = max(0, jugador.vida / jugador.vida_maxima)
        pantalla.blit(self.imagen_barra_vacia,(x,y))
        ancho = int(self.imagen_barra_llena.get_width() * porcentaje) # Calcula el ancho visible de la barra de vida
        if invertida: # Permite que la barra derecha se vacíe hacia la izquierda
            barra = self.imagen_barra_llena.subsurface((self.imagen_barra_llena.get_width() - ancho,0,ancho,self.imagen_barra_llena.get_height()))
            pantalla.blit(barra,(x + self.imagen_barra_llena.get_width() - ancho,y))
        else:
            barra = self.imagen_barra_llena.subsurface((0,0,ancho,self.imagen_barra_llena.get_height()))
            pantalla.blit(barra,(x,y)) # Dibuja el marco de la barra
        pantalla.blit(self.imagen_barra_vida,(x,y))
        # Dibuja el nombre del jugador
        nombre = jugador.nombre.lower()
        ancho_real = len(nombre) * (self.tamaño_letra * self.escala_letra)
        nombre_x = x + self.imagen_barra_vida.get_width()/2 - ancho_real/2
        self.dibujar_nombre_sprite(pantalla, nombre, nombre_x, y + 45)

    def dibujar_temporizador_sprite(self,pantalla,temporizador):
        tiempo = str(temporizador.tiempo_restante())    # Obtiene el tiempo restante del combate
        ancho_total = len(tiempo) * self.tamaño_numero  # Calcula el ancho total del número
        # Centra el temporizador entre ambas barras
        x = (400 - ancho_total // 2)
        # Dibuja cada dígito usando el spritesheet
        for digito in tiempo:
            imagen = self.obtener_numero(int(digito))
            pantalla.blit(imagen,(x,25))
            x += self.tamaño_numero

    # Muestra los numeros nuevos en pantalla llamando a los sprites
    def obtener_numero(self, numero):
        # Obtiene el sprite correspondiente al número solicitado
        x = numero * self.tamaño_numero
        return self.sprite_numeros.subsurface((x,0,self.tamaño_numero,self.sprite_numeros.get_height()))
    
    #  llama a los sprites letras
    def obtener_letra(self, letra):
        letra = letra.lower() # Convierte la letra a minúscula
        # Calcula la posición de la letra en el spritesheet
        indice = ord(letra) - ord('a')
        x = indice * self.tamaño_letra
        imagen = self.sprite_letras.subsurface((x, 0, self.tamaño_letra, self.tamaño_letra))
        # Escala la letra al tamaño deseado
        nuevo_tam = int(self.tamaño_letra * self.escala_letra)
        return pygame.transform.scale( imagen, (nuevo_tam, nuevo_tam))
    
    # Muestra en pantalla las nuevas letras
    def dibujar_nombre_sprite(self,pantalla,nombre,x,y):
        # Convierte el nombre a minúsculas
        nombre = nombre.lower()
        pos_x = x
        # Dibuja cada letra utilizando el spritesheet
        for letra in nombre:
            # Agrega un espacio cuando corresponde
            if letra == " ":
                pos_x += self.tamaño_letra
                continue
            imagen = self.obtener_letra(letra)
            pantalla.blit(imagen,(pos_x, y))
            # Avanza a la siguiente posición
            pos_x += int(self.tamaño_letra * self.escala_letra)

    def cargar_escenarios(self, ancho, alto, modo="1vs1"):
        if modo == "historia":
            self.escenarios = {
                1: pygame.transform.scale(pygame.image.load("recursos/escenarios/escenario_1.png").convert(), (ancho, alto)),
                2: pygame.transform.scale(pygame.image.load("recursos/escenarios/escenario_2.png").convert(), (ancho, alto)),
                3: pygame.transform.scale(pygame.image.load("recursos/escenarios/escenario_3.png").convert(), (ancho, alto)),
                4: pygame.transform.scale(pygame.image.load("recursos/escenarios/escenario_4.png").convert(), (ancho, alto)),
                5: pygame.transform.scale(pygame.image.load("recursos/escenarios/escenario_5.png").convert(), (ancho, alto)),
                6: pygame.transform.scale(pygame.image.load("recursos/escenarios/escenario_6.png").convert(), (ancho, alto)),
                7: pygame.transform.scale(pygame.image.load("recursos/escenarios/escenario_7.png").convert(), (ancho, alto)),
                8: pygame.transform.scale(pygame.image.load("recursos/escenarios/escenario_8.png").convert(), (ancho, alto))
            }
            
        else:
            self.escenarios = {
                1: pygame.transform.scale(pygame.image.load("recursos/escenarios/escenario_1vs1.png").convert(), (ancho, alto)),
            }

    def obtener_escenario(self, nivel):
        """Devuelve el escenario correspondiente al nivel"""
        return self.escenarios.get(nivel, self.escenarios[1])
        
    def resetear_graficos(self, graficos):
        """Resetea el estado y posición de todos los gráficos al inicio de un nuevo nivel"""
        posiciones_x = [300, 480]
        for i, grafico in enumerate(graficos):
            grafico.estado = "quieto"
            grafico.movimiento = "adelante"
            grafico.sprite.indice_frame = 0
            grafico.sprite.contador_frame = 0
            grafico.sprite.imagen_actual = grafico.sprite.quieto[0]
            grafico.rect.x = posiciones_x[i]
            grafico.col_rect.center = grafico.rect.center