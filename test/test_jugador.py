import unittest
from src.Jugador import Jugador

class TestJugador(unittest.TestCase):
    
    def setUp(self):
        """prepara el set de datos, con el que heremos las prueba"""
        self.jugador = Jugador("Alan", 100, 20, 15, "navajaso")
        self.jugador2 = Jugador("Eli", 100, 20, 15, "bomba")
        self.jugador_sin_vida = Jugador("personaje_muerto", 0, 0, 0, "nada")

    #CASO BASICO DE RECIBIR_DANIO
    def test_recibir_danio(self):
        """Verifica que la funcion recibir daño funciona correctamenet"""
        self.jugador.recibir_danio(10)
        self.assertEqual(self.jugador.vida, 90)

    def test_recibir_danio_cuando_ya_esta_muerto(self):
        """Verifica que recibir daño con vida 0 no produce vida negativa"""
        self.jugador_sin_vida.recibir_danio(50)
        self.assertEqual(self.jugador_sin_vida.vida, 0)

    #CASO LIMITE
    def test_recibir_danio_exceso(self):
       """Verifica que el jugador recibio demasiado daño"""
       self.jugador.recibir_danio(110)
       self.assertEqual(self.jugador_sin_vida.vida, 0)

#---------------------------------------------------------------------------------------------
    #CASO BASICO DE ESTOY_VIVO
    def test_estoy_vivo(self):
        """verificar que esta vivo"""
        self.assertTrue(self.jugador.estoy_vivo())

#------------------------------------------------------------------------------------------------------------------

    def test_mostrar_estado(self):
        """Verifica que el la funcion mostrar estado funciona correctamente"""
        estado = self.jugador.mostrar_estado()
        self.assertEqual(estado, "Alan: Vida = 100/100, Fuerza=20, Ataque=15, Ulti=navajaso")
        #"{self.nombre}: Vida = {self.vida}/{self.vida_maxima}, Fuerza={self.fuerza}, Ataque={self.ataque}"

#---------------------------------------------------------------------------------------------------------------------

    def test_morir(self):
       """Verifica que la funcion morir funciona correctamente"""
       self.jugador.morir()
       self.assertEqual(self.jugador_sin_vida.vida, 0)

#-----------------------------------------------------------------------------------------------------------------

    def test_bloqueo(self):
        """Verifica que bloqueo el ataque"""
        self.assertFalse(self.jugador.esta_bloqueando)
        self.jugador.bloqueo()
        self.assertTrue(self.jugador.esta_bloqueando)

    # test para verificar que bloquea y no recibe daño
    def test_bloqueo_absorbe_danio(self):
        """ verificar que bloqueo y no recibe daño"""
        self.jugador.bloqueo()
        self.jugador.recibir_danio(50)
        self.assertEqual(self.jugador.vida, 100)

#------------------------------------------------------------------------------------------------------------------------

     # test para verificar que el daño calculado es exactamente fuerza + ataque
    def test_calcular_danio(self):
        """Verificar que el daño calculado es exactamente fuerza + ataque"""
        self.assertEqual(self.jugador.calcular_danio(), 35)