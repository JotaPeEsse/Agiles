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
        palabra = juego.palabra_ganadora(["T","E","S","T"])
        self.assertTrue(letra in palabra)
        
class TestPalabraAleatoria(unittest.TestCase):
    def test_palabra_aleatoria(self):
        juego = Ahorcado()
        palabras = ['Gato', 'Perro', 'Lapiz', 'Computadora', 'Felicidad']
        palabra = juego.genera_palabra()
        self.assertTrue(palabra in palabras)
        
        
class TestPalabraGanadora(unittest.TestCase):
    def test_palabra_ganadora(self):
        juego = Ahorcado()
        palabra = juego.palabra_ingresada("Juego")
        palabra_correcta = juego.palabra_ganadora("Juego")
        self.assertEqual(palabra, palabra_correcta)


if __name__ == '__main__':
    unittest.main()
    
    
