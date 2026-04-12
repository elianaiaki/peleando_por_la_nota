from modelo.Ulti import Ulti


class Personaje:
    """Clase que representa al personaje basico del cual los demas heredan"""
    def __init__(self, nombre, vida_maxima, fuerza, ataque, ulti):
        """Inicializa nombre, vida máxima y estados del personaje"""

        #Validamos el tipo de dato

        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser un string")

        for valor in [vida_maxima, fuerza, ataque]: # refactorizacion 
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

        if isinstance(ulti, str):
            self.ulti = Ulti(ulti)      #Se adaptó el constructor para aceptar tanto strings como objetos Ulti, mejorando la flexibilidad sin romper los tests existentes.
        else:
            self.ulti = ulti            #REFACTORIZACION


    def recibir_danio(self, danio):
        """Reduce la vida del personaje según el daño recibido"""
        if danio < 0 : 
            #validamos que el daño no es negativo
            raise ValueError("El daño no puede ser negativo")
    
        if self.esta_bloqueando:
            self.esta_bloqueando = False
            return 0 #REFACTORIZACION
        

        self.vida = self.vida - danio
        if self.vida < 0:
                self.vida = 0

        if self.vida == 0:
            self.morir()
        return danio #REFACTORIZACION  

    def estoy_vivo(self):
        """Muestra la vida actual del personaje"""
        return self.vida > 0 #REFACTORIZACION


    """Muestra la vida actual del personaje"""
    def mostrar_estado(self):
        return f"La vida actual de {self.nombre} es {self.vida}"
    
    def calcular_danio(self):
        """Calcula el daño en base a fuerza y ataque"""
        danio = self.fuerza + self.ataque
        return danio

    def atacar(self, enemigo):
        """Ataca a otro personaje calculando el daño"""
        self.esta_atacando = True

        danio = self.calcular_danio()
        danio_real = enemigo.recibir_danio(danio) #REFACTORIZACION

        #falso despues de pegar, por que sino queda pegando
        self.esta_atacando = False

        return danio_real
    

    def bloqueo(self):
        """Indica si el personaje bloqueo"""
<<<<<<< HEAD
        self.esta_bloqueando = True         #REFACTORIZACION
=======
        self.esta_bloqueando = True  #REFACTORIZACION
>>>>>>> 25e0d54 (Agregue los test faltante y la actualizacion del README.md)
        return True

    def morir(self):
        """Se ejecuta cuando el personaje muere"""
        self.vida = 0
        if self.ulti: #REFACTORIZACION
            self.ulti.ejecutar(self.nombre)
    