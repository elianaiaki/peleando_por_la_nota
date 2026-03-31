#comando para probar el test
#python -m unittest discover -s test
#python -m unittest discover -s test -v miro todos los test
import unittest
from src.Personaje import Personaje

class TestPersonaje(unittest.TestCase):

    #personaje = Personaje(10) -- no se usa asi, acordarse de los hambitos
    def setUp(self):
        """prepara el set de datos, con el que heremos las prueba"""
        self.personaje = Personaje("Alan", 100, 5, 10)
        self.personaje2 = Personaje("Eli", 100, 5, 10)
        self.personaje_sin_vida = Personaje("personaje_muerto", 0, 0, 0)

    #CASO BASICO DE RECIBIR_DANIO
    #Test para verificar que el metodo funcione correctamente
    def test_recibir_danio(self):
        self.personaje.recibir_danio(10)
        self.assertEqual(self.personaje.vida, 90)

    #CASO LIMITE de recibir daño en exceso
    def test_recibir_danio_exceso(self):
        self.personaje.recibir_danio(60)
        self.assertEqual(self.personaje_sin_vida.vida, 0)

    #CASO BASICO daño exactamente igual a la vida restante
    # verifica que la vida quede en 0 y no en negativo
    def test_recibir_danio_exacto(self):
        self.personaje.recibir_danio(100)
        self.assertEqual(self.personaje.vida, 0)
 
    # CASO LIMITE - daño 0 no debe cambiar la vida
    def test_recibir_danio_cero(self):
        self.personaje.recibir_danio(0)
        self.assertEqual(self.personaje.vida, 100)
 
    # CASO LIMITE: Daño negativo no modifica la vida (se ignora con print)
    def test_recibir_danio_negativo(self):
        self.personaje.recibir_danio(-10)
        self.assertEqual(self.personaje.vida, 100)

#---------------------------------------------------------------------------------------------

    #CASO BASICO DE ESTOY_VIVO
    #Test para verificar que el metodo funcione correctamente
    def test_estoy_vivo(self):
        self.assertTrue(self.personaje.estoy_vivo())


    #Test para verificar que el metodo funcione correctamente
    def test_mostrar_estado(self):
        estado = self.personaje.mostrar_estado()
        self.assertEqual(estado, "La vida actual de Alan es 100")
        #return print(f"La vida actual de {self.nombre} es {self.vida}")

#---------------------------------------------------------------------------
    #Test para verificar que el metodo funcione correctamente
    def test_morir(self):
        self.personaje.morir()
        self.assertEqual(self.personaje_sin_vida.vida,0)
#-----------------------------------------------------------------
    #Test para verificar si bloqueo
    def test_sin_bloqueo(self):
        self.assertFalse(self.personaje.esta_bloqueando)

    def test_bloqueo(self):
        """Verifica que la funcion de bloqueo funcione"""
        self.assertFalse(self.personaje.esta_bloqueando)
        self.personaje.bloqueo()
        self.assertTrue(self.personaje.esta_bloqueando)
#-----------------------------------------------------------------
    #Test para verificar que el metodo atacar funcione correctamente
    def test_atacar(self):
        self.personaje.atacar(self.personaje2)
        self.assertEqual(self.personaje2.vida, 100-(5+10))
        self.assertEqual(self.personaje2.vida, 85)
