import random


class Ahorcado:

    def verificar_repeticion_letra(self, letra, letras_ingresadas):
        return letra in letras_ingresadas

    def crear_cadenas(self):
        palabras = [
        'Gato', 'Computadora', 'Felicidad', 'Jardin', 'Pelota',
        'Montaña','Cafe', 'Luna', 'Rana', 'Musica',
        'Playa', 'Puerta', 'Risa'
        ]
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
        return intentos < 6

    def letra_ganadora(self, letra, palabra):
        return letra in palabra

    def palabra_ganadora(self, palabra, palabra_correcta):
        return palabra == palabra_correcta

    def reemplazar_simbolo(self, original, escondida, simbolo):
        cantidad = original.count(simbolo)
        inicio = 0
        for i in range(cantidad):
            pos = original.find(simbolo, inicio)
            escondida = escondida[:pos] + simbolo + escondida[pos + 1:]
            inicio = pos + 1
        return escondida

    def contar_cantidad_intentos_restantes(self, fallo, max_fallos):
        intentos_restantes = max_fallos - fallo
        return intentos_restantes

    def adivinar_letra(self, palabra, letra):
        return letra in palabra

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
              /|\\  |
                   |
                   |
                  ===
            """,
            """
               +---+
               O   |
              /|\\  |
              /    |
                   |
                  ===
            """,
            """
               +---+
               O   |
              /|\\  |
              / \\  |
                   |
                  ===
            """
        ]

        return dibujo[intentos]


if __name__ == '__main__':
    juego = Ahorcado()
