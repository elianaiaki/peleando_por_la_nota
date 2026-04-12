#comando para probar el test
#python -m unittest discover -s test
#python -m unittest discover -s test -v miro todos los test
# python -m unittest test.test_personaje -v para probar solo el test_personaje.py

import unittest
from modelo.Personaje import Personaje

class TestPersonaje(unittest.TestCase):

    def setUp(self):
        """prepara el set de datos, con el que heremos las prueba"""
        self.personaje = Personaje("Alan", 100, 5, 10, "navajaso")
        self.personaje2 = Personaje("Eli", 100, 5, 10, "bomba")
        self.personaje_sin_vida = Personaje("personaje_muerto", 0, 0, 0, "nada")

    #CASO BASICO DE RECIBIR_DANIO
    def test_recibir_danio(self):
        """Verifica que la funcion recibir daño funciona correctamenet"""
        self.personaje.recibir_danio(10)
        self.assertEqual(self.personaje.vida, 90)

    def test_recibir_danio_cuando_ya_esta_muerto(self):
        """Verifica que recibir daño con vida 0 no produce vida negativa"""
        self.personaje_sin_vida.recibir_danio(50)
        self.assertEqual(self.personaje_sin_vida.vida, 0)

    #CASO LIMITE
    def test_recibir_danio_exceso(self):
       """Verifica que el personaje recibio demasiado daño"""
       self.personaje.recibir_danio(110)
       self.assertEqual(self.personaje.vida, 0)

    
    def test_recibir_danio_0(self):
        """Verifica que recibir daño 0 no cambia la vida"""
        self.personaje.recibir_danio(0)
        self.assertEqual(self.personaje.vida, 100)
    
    def test_recibir_danio_negativo(self):
        """No debería permitir daño negativo"""
        with self.assertRaises(ValueError):
            self.personaje.recibir_danio(-10)

#---------------------------------------------------------------------------------------------
    #CASO BASICO DE ESTOY_VIVO
    def test_estoy_vivo(self):
        """verificar que esta vivo"""
        self.assertTrue(self.personaje.estoy_vivo())

#------------------------------------------------------------------------------------------------------------------

     #CASO BASICO DE Mostrar estado
    def test_mostrar_estado(self):
        """verificar que la funcion mostrar estado, si muestra el estado"""
        estado = self.personaje.mostrar_estado()
        self.assertEqual(estado, "La vida actual de Alan es 100")
        #return print(f"La vida actual de {self.nombre} es {self.vida}")

#---------------------------------------------------------------------------------------------------------------------

    def test_morir(self):
       """Verifica que la funcion morir funciona correctamente"""
       self.personaje.morir()
       self.assertEqual(self.personaje.vida, 0)
       self.assertFalse(self.personaje.estoy_vivo())
    


#-----------------------------------------------------------------------------------------------------------------

    def test_bloqueo(self):
        """Verifica que bloqueo el ataque"""
        self.assertFalse(self.personaje.esta_bloqueando)
        self.personaje.bloqueo()
        self.assertTrue(self.personaje.esta_bloqueando)

    # test para verificar que bloquea y no recibe daño
    def test_bloqueo_absorbe_danio(self):
        """ verificar que bloqueo y no recibe daño"""
        self.personaje.bloqueo()
        self.personaje.recibir_danio(50)
        self.assertEqual(self.personaje.vida, 100)

#------------------------------------------------------------------------------------------------------------------------

     # test para verificar que el daño calculado es exactamente fuerza + ataque
    def test_calcular_danio(self):
        """Verificar que el daño calculado es exactamente fuerza + ataque"""
        self.assertEqual(self.personaje.calcular_danio(), 15)

#-----------------------------------------------------------------

    def test_atacar(self):
        """Verificar que el ataque reduce la vida del oponente correctamente"""
        self.personaje.atacar(self.personaje2)
        self.assertEqual(self.personaje2.vida, 85)
    
    def test_atacar_a_personaje_muerto(self):
        """Verificar que atacar a un personaje muerto no cambia su vida"""
        self.personaje.atacar(self.personaje_sin_vida)
        self.assertEqual(self.personaje_sin_vida.vida, 0)
    
    def test_atacar_a_personaje_bloqueando(self):
        """Verificar que atacar a un personaje bloqueando no cambia su vida"""
        self.personaje2.bloqueo()
        self.personaje.atacar(self.personaje2)
        self.assertEqual(self.personaje2.vida, 100)
    
    def test_muerte_por_ataque(self):
        """Verificar que un ataque puede matar"""
        self.personaje2.recibir_danio(90)
        self.personaje.atacar(self.personaje2)
        self.assertFalse(self.personaje2.estoy_vivo())
    