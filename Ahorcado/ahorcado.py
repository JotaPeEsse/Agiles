import random

max_fallos = 7

class Ahorcado:
    
    max_fallos = 7

    def ingresar_palabra():
        palabra = []
        while True:
            letra = input()
            if not letra:
                break
            if letra.isalpha:
                palabra.append(letra)

    def validar_letras(self, letras):
        if not letras.isalpha():
            return False
        if len(letras) > 1 and len(letras) < 3:
            return False
        return True
            
    def intentos_palabra(self, intentos):
        if intentos >= 7:
            return False
        return True      
    
    def letra_ingresada(self, letra):
        return letra

    def palabra_ganadora(self, palabra):
        return palabra

    def palabra_ingresada(self, palabra):
        return palabra
    
    def reemplazar_simbolo(self, original, escondida, simbolo):
        cantidad = original.count(simbolo)
        inicio = 0
        for i in range(cantidad):
            pos = original.find(simbolo, inicio)
            escondida = escondida[:pos] + simbolo + escondida[pos+1:]
            inicio = pos + 1
        return escondida
    
    def genera_palabra(self):
        palabras = ['Gato', 'Perro', 'Lapiz', 'Computadora', 'Felicidad']
        palabra = random.choice(palabras)
        return palabra
    
    def contar_cantidad_intentos_restantes(self,max_fallos, fallos):
        intentos_restantes = max_fallos - fallos
        return intentos_restantes
    
    def letras_ingresadas(self, letras):
        return letras
        
        
    def verificar_derrota(self,fallos):
        return (max_fallos == fallos)
        
    def adivinar_letra(self, palabra, letra):
        if letra in palabra:
            return 0
        else:
            return 1

            
if __name__ == '__main__':
    juego = Ahorcado() 
    
    