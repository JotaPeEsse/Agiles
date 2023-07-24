import random

max_fallos = 6

palabras = ['Gato', 'Perro', 'Lapiz', 'Computadora', 'Felicidad', 
            'Jardin', 'Avion', 'Pelota', 'Libro', 'Montaña', 'Cafe', 'Sol', 'Luna', 
            'Rana', 'Chocolate', 'Musica', 'Playa', 'Nube', 'Puerta', 'Risa']

class Ahorcado:
    
    max_fallos = 6

    def verificar_repeticion_letra(self, letra, letras_ingresadas):
        return letras_ingresadas.count(letra) >= 2

    def crear_cadenas(self):
        palabra = random.choice(palabras)
        palabra_escondida = '_'*len(palabra)
        return palabra, palabra_escondida

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
        if intentos >= 6:
            return False
        return True 

    def letra_ganadora(self, letra, palabra):
        if letra in palabra:
            return True
        else:
            return False
    
    def palabra_ganadora(self, palabra, palabra_correcta):
        if palabra == palabra_correcta:
            return True
        else:
            return False

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
    
    def letras_ingresadas(self, letra_ingresada, letras_utilizadas):
        if letra_ingresada in letras_utilizadas:
            return True
        else:
            return False
        
        
    def verificar_derrota(self,fallos):
        return (max_fallos == fallos)
        
    def adivinar_letra(self, palabra, letra):
        if letra in palabra:
            return 0
        else:
            return 1
    
    def crear_muñeco_ahorcado(intentos):
        dibujo = [
        """
           +---+
               |
               |
               |
               |
              ===
        """,
        """
           +---+
           O   |
               |
               |
               |
              ===
        """,
        """
           +---+
           O   |
           |   |
               |
               |
              ===
        """,
        """
           +---+
           O   |
          /|   |
               |
               |
              ===
        """,
        """
           +---+
           O   |
          /|\  |
               |
               |
              ===
        """,
        """
           +---+
           O   |
          /|\  |
          /    |
               |
              ===
        """,
        """
           +---+
           O   |
          /|\  |
          / \  |
               |
              ===
        """
        ]
    
        return dibujo[intentos]

def ahorcado():
    #os.system("cls")
    #print(f"Hola, vamos a jugar al juego del Ahorcado. \n \nLa palabra escondida sera una palabra aleatoria.\n \nTienes {max_fallos} intentos!! \n\n¡Comencemos!")
    
   # input("\nPresiona Enter para comenzar...")
    #os.system("cls")
    
    original, escondida = crear_cadenas()
    fallos = 0
    while escondida != original and fallos < max_fallos:
       # os.system("cls")
       # print(f"Palabra: {original}")
       # print(f"Palabra: {escondida}")
        
       # s = input("\n¿Qué letra vas a elegir?\n\n")
        
               
        s = s.upper()  # Convierte la letra ingresada a mayúscula
        if s[0] == original[0].upper():
            
            escondida = reemplazar_simbolo(original, escondida, s)
           # print("\n¡Bien hecho! Esa letra es parte de la palabra.")
        else: 
            
            s=s.lower()    
            if s in original:
                
                escondida = reemplazar_simbolo(original, escondida, s)
              #  print("\n¡Bien hecho! Esa letra es parte de la palabra.")
            else:
                fallos += 1
                
                dibujo_muñeco = crear_muñeco_ahorcado(fallos-1)
                print(dibujo_muñeco)
               # print(f"\nEsa letra no es parte de la palabra. Te quedan {max_fallos - fallos} intentos!")
            
     #   input("\nPresione Enter para continuar...")
        
   # if escondida == original:
       # os.system("cls")
      #  print(f"\n¡Ganaste! La palabra es {escondida}.")
  #  else:
       # os.system("cls")
       # print(f"\n¡Perdiste! La palabra era {original}.")
        
   # print("\nGracias por jugar.\n")
            
if __name__ == '__main__':
    juego = Ahorcado() 