#from modelo.Ulti import Ulti

class Personaje:
    """Clase que representa al personaje basico del cual los demas heredan"""
    def __init__(self, nombre, vida_maxima, fuerza, ataque):
        """Inicializa nombre, vida máxima y estados del personaje"""

        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser un string")

        for valor in [vida_maxima, fuerza, ataque]:
            if not isinstance(valor, (int, float)):
                raise TypeError("Los valores deben ser numéricos")
            if valor < 0:
                raise ValueError("Los valores no pueden ser negativos")     

        self.nombre = nombre
        self.vida_maxima = vida_maxima
        self.vida = vida_maxima
        self.fuerza = fuerza
        self.ataque = ataque
        self.esta_atacando = False
        self.esta_bloqueando = False
        #self.ulti = ulti

    def recibir_danio(self, danio):
        """Reduce la vida del personaje según el daño recibido"""
        if danio < 0 : 
            raise ValueError("El daño no puede ser negativo")
    
        if self.esta_bloqueando:
            self.esta_bloqueando = False
            return 0
        
        self.vida = self.vida - danio
        if self.vida < 0:
                self.vida = 0

        if self.vida == 0:
            self.morir()
        return danio

    def estoy_vivo(self):
        """Muestra la vida actual del personaje"""
        return self.vida > 0

    def mostrar_estado(self):
        """Muestra la vida actual del personaje"""
        return f"La vida actual de {self.nombre} es {self.vida}"
    
    def calcular_danio(self):
        """Calcula el daño en base a fuerza y ataque"""
        danio = self.fuerza + self.ataque
        return danio

    def atacar(self, enemigo):
        """Ataca a otro personaje calculando el daño"""
        self.esta_atacando = True

        """Si esta vivo ataca"""
        if self.vida > 0:

            danio = self.calcular_danio()
            danio_real = enemigo.recibir_danio(danio)

            #falso despues de pegar, por que sino queda pegando
            self.esta_atacando = False
            return danio_real
            """Si no esta vivo no ataca"""
        else:
            return 0

    def bloqueo(self):
        """Indica si el personaje bloqueo"""
        self.esta_bloqueando = True
        return True

    def morir(self):
        """Se ejecuta cuando el personaje muere"""
        self.vida = 0
        #self.ulti.activar()

        
