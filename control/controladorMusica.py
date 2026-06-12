import pygame
pygame.mixer.init()  # <<-- INICIALIZA EL SISTEMA DE SONIDO

class ControladorMusica:
    """Maneja toda la música del juego según el estado actual."""

    MENU    = "menu"
    PELEA   = "pelea"
    VICTORIA = "victoria"
    DERROTA  = "derrota"

    CANCIONES = {
        "menu":     "recursos/Musica/Cancion.de.Menu.mp3",
        "pelea":    "recursos/Musica/Cancion.de.Pelea.mp3",
        "victoria": "recursos/Musica/Cancion.de.Victoria.mp3",
        "derrota":  "recursos/Musica/Cancion.de.Derrota.mp3",
    }

    # def __init__(self, volumen=0.1):
    def __init__(self,volumen=0.1):
        self.estado_actual = None
        self.volumen = volumen

    def cambiar(self, nuevo_estado):
        ruta = self.CANCIONES.get(nuevo_estado)
        if not ruta or nuevo_estado == self.estado_actual:
            return  # Misma canción o estado desconocido, no hacer nada

        try:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(ruta)
            pygame.mixer.music.set_volume(self.volumen)

            if nuevo_estado in (self.MENU, self.PELEA):
                loops = -1  # pelea/menú en loop infinito
            else:
                loops = 0   # Victoria y derrota suenan una sola vez

            pygame.mixer.music.play(loops)

            self.estado_actual = nuevo_estado
            print(f"Música cambiada a: {nuevo_estado}")
        except Exception as e:
            print(f"Error al cargar música '{ruta}': {e}")

    def detener(self):
        pygame.mixer.music.stop()
        self.estado_actual = None

    def cambiar_pelea_nivel(self, nivel):

        print("ENTRE A CAMBIAR_PELEA_NIVEL", nivel)

        ruta = f"recursos/Musica/niveles/pelea_{nivel}.wav"

        try:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(ruta)
            pygame.mixer.music.set_volume(self.volumen)
            pygame.mixer.music.play(-1)

            self.estado_actual = f"pelea_{nivel}"

        except Exception as e:
            print("ERROR DE MUSICA:", e)