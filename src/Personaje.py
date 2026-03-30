class Personaje:
    """Clase que representa al personaje basico del cual los demas heredan"""
    def __init__(self, nombre, vida_maxima, fuerza, ataque):
        """Inicializa nombre, vida máxima y estados del personaje"""
        self.nombre = nombre
        self.vida_maxima = vida_maxima
        self.vida = vida_maxima
        self.fuerza = fuerza
        self.ataque = ataque
        self.esta_atacando = False
        self.esta_bloqueando = False

    def recibir_danio(self, danio):
        """Reduce la vida del personaje según el daño recibido"""
        if danio < 0 : 
            print("El daño no puede ser negativo")
            return
    
        if self.esta_bloqueando:
            #CORREJIII
            #self.bloqueo() --redundante, ya sabemos que está bloqueando
            # no tiene sentido volver a llamar al método que setea esta_bloqueando = True
            print(f"{self.nombre} bloqueó el daño!")
            self.esta_bloqueando = False
            return
        
        else:
            self.vida = self.vida - danio
            if self.vida < 0:
                self.vida = 0
            print(f"{self.nombre} recibió {danio} de daño")

        if self.vida == 0:
            self.morir()

    def estoy_vivo(self):
        """Devuelve la vida actual del personaje"""
        if self.vida > 0:
            print(f"Estoy vivo")
            return True
        else:
            print(f"No esta vivo")
            return False

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
        enemigo.recibir_danio(danio)
        print(f"{self.nombre} ataco a {enemigo.nombre} con {danio} de danio")

        # CORREJIIII: tiene que ser falso despues de pegar, por que sino queda pegando por la eternidad jajaj
        self.esta_atacando = False
        return danio
    

    def bloqueo(self):
        """Indica si el personaje bloqueo"""
        self.esta_bloqueando = True
        print(f"{self.nombre} bloqueo el ataque del enemigo")
        return True

    def morir(self):
        """Se ejecuta cuando el personaje muere"""
        # self.vida = 0
        print(f"{self.nombre} ha muerto!")
        return True
    