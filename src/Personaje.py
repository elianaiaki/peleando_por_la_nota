class Personaje:
    "Clase que representa al personaje basico del cual los demas heredan"
    def __init__(self, nombre, vida_maxima):
        "Inicializa nombre, vida máxima y estados del personaje"
        self.nombre = nombre
        self.vida_maxima = vida_maxima
        self.vida = vida_maxima
        self.esta_atacando = False
        self.esta_bloqueando = False

    def recibir_Danio(self, danio):
        "Reduce la vida del personaje según el daño recibido"
        if (danio < 0 ): 
            print("El daño no puede ser negativo")
            return
    
        if self.esta_bloqueando:
            self.bloqueo()
            print(f"{self.nombre} bloqueó el daño!")
            self.esta_bloqueando = False
            return False
        else:
            self.vida = self.vida - danio
            if self.vida < 0:
                self.vida = 0
            print(f"{self.nombre} recibió {danio} de daño")

        if self.vida == 0:
            "Indica si el personaje sigue con vida"
            self.morir()

    def estoy_Vivo(self):
        "Devuelve la vida actual del personaje"
        if self.vida > 0:
            print(f"Estoy vivo")
            return True
        else:
            print(f"No esta vivo")
            return False

    "Muestra la vida actual del personaje"
    def mostrar_estado(self):
        return f"La vida actual de {self.nombre} es {self.vida}"

    def atacar(self, enemigo):
        "Ataca a otro personaje calculando el daño"
        self.esta_atacando = True
        danio = self.calcularDanio()
        enemigo.recibir_Danio(danio)
        print(f"{self.nombre} ataco a {enemigo.nombre} con {danio} de danio")

    def bloqueo(self):
        self.esta_bloqueando = True
        print(f"{self.nombre} bloqueo el ataque del enemigo")
        return True

    def morir(self):
        "Se ejecuta cuando el personaje muere"
        # self.vida = 0
        print(f"{self.nombre} ha muerto!")
        return True
    