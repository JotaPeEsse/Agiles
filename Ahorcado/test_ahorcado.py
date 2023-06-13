import unittest
from ahorcado import Ahorcado

         
class TestIngresarPalabra(unittest.TestCase):
    def test_ingreso_de_palabra(self):
        juego = Ahorcado() 
        self.assertTrue(juego.validar_letras("python"))
        
        
class TestIntentos(unittest.TestCase):
    def test_intentos(self):
        juego = Ahorcado() 
        self.assertTrue(juego.intentos_palabra(3))
        self.assertTrue(juego.intentos_palabra(6))
        
        
class TestPalabraOculta(unittest.TestCase):
    def test_palabra_oculta(self):
        juego = Ahorcado()
        palabra = "Perro"
        palabra_oculta = "_____"
        letra = "r"
        palabra_oculta = juego.reemplazar_simbolo(palabra, palabra_oculta, letra)
        self.assertEqual(palabra_oculta, "__rr_")
       
class TestLetraValida(unittest.TestCase):
    def test_palabra_valida(self):
        juego = Ahorcado()
        letra = juego.letra_ingresada("E")
        palabra = juego.palabra_elegida(["T","E","S","T"])
        self.assertTrue(letra in palabra)
        

if __name__ == '__main__':
    unittest.main()
    
    
