class Ahorcado:

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

    def palabra_elegida(self, palabra):
        return palabra
    
    def reemplazar_simbolo(self, original, escondida, simbolo):
        cantidad = original.count(simbolo)
        inicio = 0
        for i in range(cantidad):
            pos = original.find(simbolo, inicio)
            escondida = escondida[:pos] + simbolo + escondida[pos+1:]
            inicio = pos + 1
        return escondida

            
if __name__ == '__main__':
    juego = Ahorcado() 
    
    