import pygame

class ControladorSonido:
    """Maneja todos los efectos de sonido del juego, separado de la música de fondo"""

    def __init__(self, volumen=0.5):
        self.volumen = volumen
        self.canal_golpe = None  # acá vamos a guardar el canal del último golpe

        # Sonido de golpe, compartido por todos los personajes
        self.sonido_golpe = self._cargar("recursos/sonidos/golpear2.wav")

        # Nombres de los personajes que tienen sonidos propios
        nombres_personajes = ["alan", "eliana", "gabriel", "gabo", "yiyo", "profe"]

        # En vez de un diccionario de diccionarios, usamos dos diccionarios planos:
        # uno para "golpeado" y otro para "muriendo". Misma información, menos anidado.
        self.sonidos_golpeado = {}
        self.sonidos_muerte = {}

        for nombre in nombres_personajes:
            self.sonidos_golpeado[nombre] = self._cargar(f"recursos/sonidos/{nombre}/golpeado.wav")
            self.sonidos_muerte[nombre] = self._cargar(f"recursos/sonidos/{nombre}/muriendo.wav")

    def _cargar(self, ruta):
        """Carga un sonido desde una ruta, devuelve None si no existe"""
        try:
            sonido = pygame.mixer.Sound(ruta)
            sonido.set_volume(self.volumen)
            return sonido
        except Exception as e:
            print(f"No se pudo cargar el sonido '{ruta}': {e}")
            return None

    def reproducir_golpe(self):
        """Reproduce el sonido de puño al atacar, compartido por todos"""
        if self.sonido_golpe is not None:
            self.canal_golpe = self.sonido_golpe.play()

    def detener_golpe(self):
        """Corta el sonido de golpe si está sonando"""
        if self.canal_golpe is not None:
            self.canal_golpe.stop()

    def reproducir_golpeado(self, nombre_personaje):
        """Reproduce el sonido del personaje cuando recibe un golpe"""
        sonido = self.sonidos_golpeado.get(nombre_personaje)
        if sonido is not None:
            sonido.play()

    def reproducir_muerte(self, nombre_personaje):
        """Reproduce el sonido del personaje cuando muere"""
        sonido = self.sonidos_muerte.get(nombre_personaje)
        if sonido is not None:
            sonido.play()