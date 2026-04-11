#comando para probar el test
#python -m unittest discover -s test
#python -m unittest discover -s test -v miro todos los test
import unittest
from modelo.Personaje import Personaje

class TestPersonaje(unittest.TestCase):

    def setUp(self):
        """prepara el set de datos, con el que heremos las prueba"""
        self.personaje = Personaje("Alan", 100, 5, 10, "navajaso")
        self.personaje2 = Personaje("Eli", 100, 5, 10, "bomba")
        self.personaje_sin_vida = Personaje("personaje_muerto", 0, 0, 0, "nada")
        self.personaje_con_pocavida = Personaje("Personaje_conpocavida", 1, 5, 10, "nada")

    #CASO BASICO DE RECIBIR_DANIO
    def test_recibir_danio(self):
        """Verifica que recibio el daño correctamente"""
        self.personaje.recibir_danio(10)
        self.assertEqual(self.personaje.vida, 90)

    def test_recibir_danio_cuando_ya_esta_muerto(self):
        """Verifica que recibir daño con vida 0 no produce vida negativa"""
        self.personaje_sin_vida.recibir_danio(50)
        self.assertEqual(self.personaje_sin_vida.vida, 0)

    #CASO LIMITE de recibir daño en exceso
    def test_recibir_danio_exceso(self):
        """Verifica que el personaje recibio un daño en exceso"""
        self.personaje.recibir_danio(110)
        self.assertEqual(self.personaje_sin_vida.vida, 0)

    def test_recibir_danio_exacto(self):
        """verifica que la vida quede en 0 y no en negativo"""
        self.personaje.recibir_danio(100)
        self.assertEqual(self.personaje.vida, 0)


#---------------------------------------------------------------------------------------------

    #CASO BASICO DE ESTOY_VIVO
    def test_estoy_vivo(self):
        """verificar que esta vivo"""
        self.assertTrue(self.personaje.estoy_vivo(), True)

    #CASO BASICO DE Mostrar estado
    def test_mostrar_estado(self):
        """verificar que la funcion mostrar estado, si muestra el estado"""
        estado = self.personaje.mostrar_estado()
        self.assertEqual(estado, "La vida actual de Alan es 100")
        #return print(f"La vida actual de {self.nombre} es {self.vida}")

#---------------------------------------------------------------------------
    #CASO BASICO de morir
    def test_morir(self):
        """verifica que el metodo morir funcione correctamente"""
        self.personaje.morir()
        self.assertEqual(self.personaje_sin_vida.vida,0)
#-----------------------------------------------------------------
    #CASO BASICO de bloquear
    def test_sin_bloqueo(self):
        """Verifica que si bloqueo"""
        self.assertFalse(self.personaje.esta_bloqueando)

    def test_bloqueo(self):
        """Verifica que la funcion de bloqueo funcione"""
        self.assertFalse(self.personaje.esta_bloqueando)
        self.personaje.bloqueo()
        self.assertTrue(self.personaje.esta_bloqueando)
#-----------------------------------------------------------------

    def test_atacar(self):
        """Verifica que la funcion atacar funciona correctamente"""
        self.personaje.atacar(self.personaje2)
        self.assertEqual(self.personaje2.vida, 100-(5+10))
        self.assertEqual(self.personaje2.vida, 85)
