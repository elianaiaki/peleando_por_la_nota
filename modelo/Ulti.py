class Ulti:
    def __init__(self, nombre):
        self.nombre = nombre

    def ejecutar(self, personaje): #REFACTORIZACION
        return f"{personaje} ejecuta su ulti: {self.nombre}"