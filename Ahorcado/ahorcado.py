import random

class Ahorcado:
    max_fallos = 6

    def verificar_repeticion_letra(self, letra, letras_ingresadas):
        return letras_ingresadas.count(letra) >= 2

    def crear_cadenas(self):
        palabras = ['Gato', 'Perro', 'Lapiz', 'Computadora', 'Felicidad']
        palabra = random.choice(palabras)
        palabra_escondida = '_' * len(palabra)
        return palabra, palabra_escondida

    def validar_letras(self, letras):
        if not letras.isalpha():
            return False
        if len(letras) > 1 and len(letras) < 3:
            return False
        return True

    def intentos_palabra(self, intentos):
        if intentos >= Ahorcado.max_fallos:
            return False
        return True

    def letra_ganadora(self, letra, palabra):
        return letra in palabra

    def palabra_ganadora(self, palabra, palabra_correcta):
        return palabra == palabra_correcta

    def palabra_ingresada(self, palabra):
        return palabra

    def reemplazar_simbolo(self, original, escondida, simbolo):
        cantidad = original.count(simbolo)
        inicio = 0
        for i in range(cantidad):
            pos = original.find(simbolo, inicio)
            escondida = escondida[:pos] + simbolo + escondida[pos + 1:]
            inicio = pos + 1
        return escondida

    def genera_palabra(self):
        palabras = ['Gato', 'Perro', 'Lapiz', 'Computadora', 'Felicidad']
        palabra = random.choice(palabras)
        return palabra

    def contar_cantidad_intentos_restantes(self, fallos):
        intentos_restantes = Ahorcado.max_fallos - fallos
        return intentos_restantes

    def letras_ingresadas(self, letra_ingresada, letras_utilizadas):
        return letra_ingresada in letras_utilizadas

    def verificar_derrota(self, fallos):
        return Ahorcado.max_fallos == fallos

    def adivinar_letra(self, palabra, letra):
        return 0 if letra in palabra else 1

    def crear_muñeco_ahorcado(self, intentos):
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

if __name__ == '__main__':
    juego = Ahorcado()


