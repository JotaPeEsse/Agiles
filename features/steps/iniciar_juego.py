from playwright.sync_api import Page, Browser, sync_playwright
from behave import given, when, then
from bs4 import BeautifulSoup

import time

BASE_URL = 'https://martinb.pythonanywhere.com/juego'

from playwright.sync_api import sync_playwright

def iniciar_navegador():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        return browser, page



"-----------------------------------------------------Iniciar-Juego-----------------------------------------------------"  

def ingresar_letra(page: Page, letra: str):
    input_selector = 'input[name="letra"]'
    page.wait_for_selector(input_selector)
    page.fill(input_selector, letra)
    page.click('button[type="submit"]')

@given('que estoy en la página de inicio')
def step_estoy_en_pagina_inicio(context):
    with sync_playwright() as p:
        browser: Browser = p.chromium.launch(headless=False)
        context.browser = browser
        context.page = browser.new_page()
        context.page.goto('https://martinb.pythonanywhere.com/')
        time.sleep(2)

@when('hago clic en el botón "{button_text}"')
def step_hago_clic_en_jugar(context, button_text):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context.page = browser.new_page()
        context.page.goto('https://martinb.pythonanywhere.com/')
        context.page.wait_for_selector(f'button:has-text("{button_text}")')
        button = context.page.query_selector(f'button:has-text("{button_text}")')
        button.click()
        time.sleep(2)
        
        
@then('debería ser redirigido a la página del juego')
def step_deberia_ser_redirigido(context):
    target_url =  'https://martinb.pythonanywhere.com/juego'
    current_url = context.page.url
    assert current_url == target_url, f"URL actual: {current_url}, URL objetivo: {target_url}"
    time.sleep(2)

"-----------------------------------------------------Ganar-Juego-----------------------------------------------------"  

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
    
@then('cierro el navegador')
def step_cerrar_navegador(context):
    context.browser.close() 

"--------------------------------Adivinar-Letra---------------------------------------------------------------"



@given('estoy en la página de juego')
def step_estoy_en_pagina_inicio(context):
    with sync_playwright() as p:
        browser: Browser = p.chromium.launch(headless=False)
        context.browser = browser
        context.page = browser.new_page()
        context.page.goto('https://martinb.pythonanywhere.com/juego')
        time.sleep(2)

@when('ingreso la letra "{letra}"')
def step_ingreso_letra(context, letra):
    context.page.fill('input[name="letra"]', letra)
    context.page.click('button[type="submit"]')
    time.sleep(1)

@then('debería ver la letra "{letra}" en la palabra oculta')
def step_ver_letra_en_palabra_oculta(context, letra):
    palabra_oculta = context.page.inner_text('#pal h2')
    assert letra in palabra_oculta
    time.sleep(1)
@then('el dibujo del muñeco del ahorcado debería seguir vacío')
def step_deberia_ver_dibujo_vacio(context):
    page_source = context.page.content()
    soup = BeautifulSoup(page_source, 'html.parser')
    dibujo_muñeco = soup.find('div', id='dibujo').pre.text

    assert '+---+' in dibujo_muñeco
    assert 'O   |' not in dibujo_muñeco
    time.sleep(1)
@then('el número de intentos restantes debe mantenerse')
def step_ver_intentos_restantes(context):
    intentos_restantes = context.page.inner_text('#intentos h2')
    assert intentos_restantes == 'Intentos restantes: 6'
    time.sleep(1)
