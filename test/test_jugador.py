import unittest
from src.Jugador import Jugador

class TestJugador(unittest.TestCase):
    
    #personaje = Personaje(10) -- no se usa asi, acordarse de los hambitos
    #def setUp(self):
        #prepara el set de datos, con el que heremos las prueba
        #self.personaje = Personaje("Alan", 100)
        #self.personaje2 = Personaje("Eli", 100)

    #CASO BASICO DE RECIBIR_DANIO
    #Test para verificar que el metodo funcione correctamente
    def test_recibir_danio(self):
        jugador = Jugador("Alan", 100, 20, 15)
        jugador.recibir_danio(10)
        self.assertEqual(jugador.vida, 90)

    #CASO LIMITE de recibir daño
    def test_recibir_danio_exceso(self):
        jugador = Jugador("Alan", 50, 20, 15)
        jugador.recibir_danio(60)
        self.assertEqual(jugador.vida, 0)

    #CASO LIMITE:daño negativo no modifica la vida en Jugador (heredado de Personaje)
    def test_recibir_danio_negativo(self):
        jugador = Jugador("Alan", 100, 20, 15)
        jugador.recibir_danio(-5)
        self.assertEqual(jugador.vida, 100)

#---------------------------------------------------------------------------------------------

    #CASO BASICO DE ESTOY_VIVO
    #Test para verificar que el metodo funcione correctamente
    def test_estoy_vivo(self):
        jugador = Jugador("Alan", 100, 20, 15)
        #jugador.estoy_vivo()
        self.assertTrue(jugador.estoy_vivo())


    #Test para verificar que el metodo funcione correctamente
    def test_mostrar_estado(self):
        jugador = Jugador("Alan", 100, 20, 15)
        estado = jugador.mostrar_estado()
        self.assertEqual(estado, "Alan: Vida = 100/100, Fuerza=20, Ataque=15")
        #"{self.nombre}: Vida = {self.vida}/{self.vida_maxima}, Fuerza={self.fuerza}, Ataque={self.ataque}"


    #Test para verificar que el metodo funcione correctamente
    def test_morir(self):
        jugador = Jugador("Alan", 0, 20, 15)
        jugador.morir()
        self.assertEqual(jugador.vida, 0)

    #Test para verificar si bloqueo
    def test_bloqueo(self):
        jugador = Jugador("Alan", 100, 20, 15)
        self.assertFalse(jugador.esta_bloqueando)
        jugador.bloqueo()
        self.assertTrue(jugador.esta_bloqueando)

     # test para verificar que el daño calculado es exactamente fuerza + ataque
    def test_calcular_danio(self):
        jugador = Jugador("Alan", 100, 20, 15)
        self.assertEqual(jugador.calcular_danio(), 35)