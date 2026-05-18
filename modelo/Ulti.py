class Ulti:

    def __init__(self, nombre):
        self.nombre = nombre
        self.activa = False

    def activar(self):
        self.activa = True
        print("ulti se activo")

    def desactivar(self):
        self.activa = False

    def ejecutar_ulti(self, personaje):
        return f"{personaje} ejecuta su ulti: {self.nombre}"