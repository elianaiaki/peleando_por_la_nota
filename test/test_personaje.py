#comando para probar el test
#python -m unittest discover -s test
#python -m unittest discover -s test -v miro todos los test
import unittest
from src.Personaje import Personaje

class TestPersonaje(unittest.TestCase):

    #personaje = Personaje(10) -- no se usa asi, acordarse de los hambitos
    #def setUp(self):
        #prepara el set de datos, con el que heremos las prueba
        #self.personaje = Personaje("Alan", 100)
        #self.personaje2 = Personaje("Eli", 100)

    #CASO BASICO DE RECIBIR_DANIO
    #Test para verificar que el metodo funcione correctamente
    def test_recibir_danio(self):
        personaje = Personaje("Alan", 100)
        personaje.recibir_danio(10)
        self.assertEqual(personaje.vida, 90)

    #CASO LIMITE de recibir daño
    def test_recibir_danio_exceso(self):
        personaje = Personaje("Alan", 50)
        personaje.recibir_danio(60)
        self.assertEqual(personaje.vida, 0)

#---------------------------------------------------------------------------------------------

    #CASO BASICO DE ESTOY_VIVO
    #Test para verificar que el metodo funcione correctamente
    def test_estoy_vivo(self):
        personaje = Personaje("Alan", 100)
        personaje.estoy_vivo()
        self.assertEqual(personaje.estoy_vivo(),True)


    #Test para verificar que el metodo funcione correctamente
    def test_mostrar_estado(self):
        personaje = Personaje("Alan", 100)
        estado = personaje.mostrar_estado()
        self.assertEqual(estado, "La vida actual de Alan es 100")
        #return print(f"La vida actual de {self.nombre} es {self.vida}")


    #Test para verificar que el metodo funcione correctamente
    def test_morir(self):
        personaje = Personaje("Alan", 0)
        personaje.morir()
        self.assertEqual(personaje.vida,0)

    #Test para verificar si bloqueo
    def test_bloqueo(self):
        personaje = Personaje("Alan", 100)
        self.assertFalse(personaje.esta_bloqueando)
        personaje.bloqueo()
        self.assertTrue(personaje.esta_bloqueando)
