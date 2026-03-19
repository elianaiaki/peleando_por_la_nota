class Personaje:
    def __init__(self, vida_maxima):
        self.vida_maxima = vida_maxima
        self.vida = vida_maxima
        self.esta_atacando = False
        self.esta_bloqueando = False

    def recibir_Danio(self, danio):
        if self.esta_bloqueando:
            danio = danio // 2
            print(f"{self.nombre} bloqueó parte del daño!")

        self.vida = self.vida - danio
        print(f"{self.nombre} recibió {danio} de daño")

        if self.vida <0:
            self.morir()

    def estoy_Vivo(self):
        return self.vida > 0
    
    def mostrar_estado(self):
        return self.vida

    def atacar(self, enemigo):
        self.esta_atacando = True
        danio = 1
        enemigo.recibir_Danio(danio)

    def morir(self):
        if self.vida < 0:
            self.vida = 0
            print(f"{self.nombre} ha muerto!")