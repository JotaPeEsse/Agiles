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


class TestIntentosRestantes(unittest.TestCase):
    def test_contar_intentos_restantes(self):
        juego = Ahorcado()
        juego.max_fallos
        fallos = 3
        intentos_restantes = juego.contar_cantidad_intentos_restantes(juego.max_fallos, fallos)
        self.assertEqual(intentos_restantes, 4)
        
        
class TestLetrasIngresadas(unittest.TestCase):
    def test_letras_ingresadas(self):
        juego = Ahorcado()
        letra_ingresada = juego.letra_ingresada("E")
        letras_ingresadas = juego.letras_ingresadas(["A","E","K","W","Ñ"])
        self.assertTrue(letra_ingresada in letras_ingresadas)

class TestLetraIncorrecta(unittest.TestCase):
    def test_letra_incorrecta(self):
        juego = Ahorcado()
        letra_ingresada = juego.letra_ingresada("A")
        palabra_correcta = juego.palabra_ganadora(["T","E","S","T"])
        self.assertFalse(letra_ingresada in palabra_correcta)

class TestVerificarDerrota(unittest.TestCase):
    def test_verificar_derrota(self):
        juego = Ahorcado()
        juego.max_fallos
        fallos = 7
        self.assertTrue(juego.verificar_derrota(fallos))

class TestVerificacionLetraIncorrecta(unittest.TestCase):
    def test_verificacion_letra_incorrecta(self):
        juego = Ahorcado()
        palabra_correcta = ["T","E","S","T"]
        letra_ingresada = "A"
        fallo = juego.adivinar_letra(palabra_correcta, letra_ingresada)
        self.assertEqual(fallo, 1)


if __name__ == '__main__':
    unittest.main()
    
    
