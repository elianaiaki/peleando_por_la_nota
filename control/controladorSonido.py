import pygame

class ControladorSonido:
    """Maneja todos los efectos de sonido del juego, separado de la música de fondo"""

    def __init__(self, volumen=0.5):
        # Volumen base para todos los efectos
        self.volumen = volumen

        # Sonido de golpe, compartido por todos los personajes
        self.sonido_golpe = self._cargar("recursos/sonidos/golpear2.mp3")

        # Diccionario con los sonidos de cada personaje
        # Cada personaje tiene su propio sonido al recibir daño y al morir
        self.sonidos_personajes = {
            "alan":    self._cargar_personaje("alan"),
            "eliana":  self._cargar_personaje("eliana"),
            "gabriel": self._cargar_personaje("gabriel"),
            "gabo":    self._cargar_personaje("gabo"),
            "yiyo":    self._cargar_personaje("yiyo"),
        }

    def _cargar(self, ruta):
        """Carga un sonido desde una ruta, devuelve None si no existe"""
        try:
            sonido = pygame.mixer.Sound(ruta)
            sonido.set_volume(self.volumen)
            return sonido
        except Exception as e:
            print(f"No se pudo cargar el sonido '{ruta}': {e}")
            return None

    def _cargar_personaje(self, nombre):
        """Carga los sonidos específicos de un personaje"""
        return {
            "golpeado": self._cargar(f"recursos/sonidos/{nombre}/golpeado.wav"),
            "muriendo":   self._cargar(f"recursos/sonidos/{nombre}/muriendo.wav"),
        }

    def reproducir_golpe(self):
        """Reproduce el sonido de puño al atacar, compartido por todos"""
        if self.sonido_golpe:
            self.sonido_golpe.play()

    def reproducir_golpeado(self, nombre_personaje):
        """Reproduce el sonido del personaje cuando recibe un golpe"""
        sonidos = self.sonidos_personajes.get(nombre_personaje)
        if sonidos and sonidos["golpeado"]:
            sonidos["golpeado"].play()

    def reproducir_muerte(self, nombre_personaje):
        """Reproduce el sonido del personaje cuando muere"""
        sonidos = self.sonidos_personajes.get(nombre_personaje)
        if sonidos and sonidos["muriendo"]:
            sonidos["muriendo"].play()