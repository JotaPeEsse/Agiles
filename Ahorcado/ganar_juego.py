from playwright.sync_api import Page, Browser, sync_playwright
from behave import given, when, then
import time


# Definir el URL base para la página de juego
BASE_URL = 'https://martinb.pythonanywhere.com/juego'

# Función para ingresar una letra en el campo de entrada
def ingresar_letra(page: Page, letra: str):
    input_selector = 'input[name="letra"]'
    page.wait_for_selector(input_selector)
    page.fill(input_selector, letra)
    page.click('button[type="submit"]')

# Steps para el escenario de adivinar correctamente todas las letras de la palabra oculta
@given('que estoy en la página de juego')
def step_abrir_pagina_de_juego(context):
    context.browser = sync_playwright().start().chromium.launch(headless=False)
    context.page = context.browser.new_page()
    context.page.goto(BASE_URL)
    time.sleep(2)

@when('adivino correctamente todas las letras de la palabra oculta')
def step_adivino_correctamente(context):
    # Obtener la palabra oculta de la página
    palabra_oculta = context.page.inner_text('#palabra h2').strip().lower()
    print(palabra_oculta)

    # Crear un conjunto para almacenar las letras adivinadas
    letras_adivinadas = set()
    
     # Obtener el número de intentos restantes antes de adivinar las letras
    intentos_restantes_text = context.page.inner_text('#intentos h2')
    intentos_restantes = int(intentos_restantes_text.split()[-1])

    # Adivinar cada letra de la palabra oculta
    for letra in palabra_oculta:
        if letra not in letras_adivinadas:
            ingresar_letra(context.page, letra)
            time.sleep(2)
            letras_adivinadas.add(letra)
    # Actualizar la palabra oculta después de cada adivinanza
        palabra_oculta_actualizada = context.page.inner_text('#pal h2').strip().lower()
        letras_ocultas = set(palabra_oculta_actualizada)

    # Imprimir la palabra oculta final después de adivinar todas las letras
    print(f'Palabra oculta final: {palabra_oculta_actualizada}')
    time.sleep(1)

@then('el dibujo del muñeco del ahorcado debería estar en su estado inicial')
def step_ver_dibujo_estado_inicial(context):
 
    page_source = context.page.content()
    soup = BeautifulSoup(page_source, 'html.parser')
    dibujo_muñeco = soup.find('div', id='dibujo').pre.text

    assert '+---+' in dibujo_muñeco
    assert 'O   |' not in dibujo_muñeco
    time.sleep(1)

@then('el número de intentos restantes debería mantenerse')
def step_ver_intentos_restantes(context):
    context.page.wait_for_selector('#intentos h2')
    intentos_restantes_text = context.page.inner_text('#intentos h2')
    assert 'Intentos restantes' in intentos_restantes_text
    assert intentos_restantes_text.split()[-1] != ''  # Aseguramos que el valor no esté vacío
    assert 'Intentos restantes: 6' in intentos_restantes_text
    time.sleep(1)



@then('debería ver el mensaje "¡Ganaste!"')
def step_verificar_mensaje_ganador(context):
    mensaje_ganador_element = context.page.wait_for_selector('#resultado h2')
    mensaje_ganador = mensaje_ganador_element.inner_text()
    assert '¡Ganaste!' in mensaje_ganador
    time.sleep(2)
