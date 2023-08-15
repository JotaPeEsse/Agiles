from flask import Flask, render_template, request, session
import random
import os
from ahorcado import Ahorcado

app = Flask(__name__)
app.secret_key = 'clave_secreta'

max_fallos = 6

palabras = ['Gato', 'Computadora', 'Felicidad', 
            'Jardin','Pelota', 'Montaña', 'Cafe', 'Luna', 
            'Rana',  'Musica', 'Playa', 'Puerta', 'Risa']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/juego', methods=['GET', 'POST'])
def juego():
    ahoracado = Ahorcado()
    if request.method == 'POST':
        letra = request.form['letra']
        palabra = session['palabra']
        escondida = session['escondida']
        fallos = session['fallos']
        dibujo = session['dibujo']
        letras_ingresadas = session.get('letras_ingresadas', [])  # Obtén la lista de letras ingresadas
        
        letra = letra.upper()
        if letra[0] == palabra[0].upper():
            escondida = ahoracado.reemplazar_simbolo(palabra, escondida, letra)
        else:
            letra = letra.lower()
            if letra in palabra:
                escondida = ahoracado.reemplazar_simbolo(palabra, escondida, letra)
            else:
                fallos += 1
                dibujo = ahoracado.crear_muñeco_ahorcado(fallos)
            
        letras_ingresadas.append(letra)  # Agrega la letra ingresada a la lista de letras ingresadas
        
        session['escondida'] = escondida
        session['fallos'] = fallos
        session['dibujo'] = dibujo
        session['letras_ingresadas'] = letras_ingresadas  # Actualiza la lista de letras ingresadas

        if escondida == palabra:
            resultado = 'ganaste'
        elif fallos >= max_fallos:
            resultado = 'perdiste'
        else:
            resultado = 'continuar'

        return render_template('juego.html', palabra=palabra, escondida=escondida, fallos=fallos, dibujo=dibujo, resultado=resultado, max_fallos=max_fallos, letras_ingresadas=letras_ingresadas)  # Pasa la lista de letras ingresadas al contexto
    else:
        palabra, escondida = ahoracado.crear_cadenas()

        session['palabra'] = palabra
        session['escondida'] = escondida
        session['fallos'] = 0
        session['dibujo'] = ahoracado.crear_muñeco_ahorcado(0)
        session.pop('letras_ingresadas', None)  # Reinicia la lista de letras ingresadas

        return render_template('juego.html', palabra=palabra, escondida=escondida, fallos=0, dibujo=ahoracado.crear_muñeco_ahorcado(0), resultado='continuar', max_fallos=max_fallos)


@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)











