import unittest
import coverage
from ahorcado import Ahorcado


cov = coverage.Coverage()
cov.start()


         
class TestIngresarPalabra(unittest.TestCase):
    def test_ingreso_de_palabra(self):
        juego = Ahorcado() 
        self.assertTrue(juego.validar_letras("python"))
        
        
class TestIntentos(unittest.TestCase):
    def test_intentos(self):
        juego = Ahorcado() 
        self.assertTrue(juego.intentos_palabra(3))
        self.assertTrue(juego.intentos_palabra(5))
        
        
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
        letra = "E"
        palabra = ["T","E","S","T"]
        self.assertTrue(juego.letra_ganadora(letra, palabra))
        
        
class TestPalabraGanadora(unittest.TestCase):
    def test_palabra_ganadora(self):
        juego = Ahorcado()
        palabra = "Juego"
        palabra_correcta = "Juego"
        self.assertTrue(juego.palabra_ganadora(palabra, palabra_correcta))


class TestIntentosRestantes(unittest.TestCase):
    def test_contar_intentos_restantes(self):
        juego = Ahorcado()
        fallos = 3
        max_fallos = 6
        intentos_restantes = juego.contar_cantidad_intentos_restantes(fallos, max_fallos)
        self.assertEqual(intentos_restantes, max_fallos - fallos)
        

class TestLetraIncorrecta(unittest.TestCase):
    def test_letra_incorrecta(self):
        juego = Ahorcado()
        letra_ingresada = "A"
        palabra_correcta = ["T","E","S","T"]
        self.assertFalse(juego.letra_ganadora(letra_ingresada, palabra_correcta))


class TestVerificacionLetraIncorrecta(unittest.TestCase):
    def test_verificacion_letra_incorrecta(self):
        juego = Ahorcado()
        palabra_correcta = ["T","E","S","T"]
        letra_ingresada = "A"
        fallo = juego.adivinar_letra(palabra_correcta, letra_ingresada)
        self.assertEqual(fallo, False)

class TestVereficarRepeticionLetra(unittest.TestCase):
    def test_verificar_repeticion_letra(self):
        juego = Ahorcado()
        letra = 'e'
        letras_ingresadas = ['a', 'b', 'e', 'e']
        result = juego.verificar_repeticion_letra(letra, letras_ingresadas)
        self.assertTrue(result)

class TestVereficarNoRepeticionLetra(unittest.TestCase):       
    def test_verificar_no_repeticion_letra(self):
        juego = Ahorcado()
        letra = 'e'
        letras_ingresadas = ['a', 'b', 'c']
        result = juego.verificar_repeticion_letra(letra, letras_ingresadas)
        self.assertFalse(result)

class TestCrearCadenasOcultas(unittest.TestCase):
    def test_crear_cadenas(self):
        juego = Ahorcado()
        palabra, palabra_escondida = juego.crear_cadenas()
        self.assertTrue(all(c == '_' for c in palabra_escondida))

class TestCrearMuñecoAhorcado(unittest.TestCase):
    def test_crear_muñeco_ahorcado(self):
        for intentos in range(7):
            juego = Ahorcado()
            dibujo_esperado = juego.crear_muñeco_ahorcado(intentos)
            self.assertEqual(dibujo_esperado.strip(), juego.crear_muñeco_ahorcado(intentos).strip())

cov.stop()
cov.save()


if __name__ == '__main__':
    unittest.main()
    
    
