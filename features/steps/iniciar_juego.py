from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright

import asyncio
from bs4 import BeautifulSoup
from behave import given, when, then
import time

# Definir el URL base para la página de juego
BASE_URL = 'https://martinb.pythonanywhere.com/juego'


# ---------------------------------------Iniciar Juego-------------------------------------------------------------
@given('que estoy en la página de inicio')
async def step_estoy_en_pagina_inicio(context):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context.browser = browser
        context.page = await browser.new_page()
        await context.page.goto('https://martinb.pythonanywhere.com')
        time.sleep(2)


@when('hago clic en el botón "{button_text}"')
async def step_hago_clic_en_jugar(context, button_text):
    await context.page.goto('https://martinb.pythonanywhere.com')
    await context.page.wait_for_selector(f'button:has-text("{button_text}")')
    button = await context.page.query_selector(f'button:has-text("{button_text}")')
    await button.click()
    time.sleep(2)


@then('debería ser redirigido a la página del juego')
async def step_deberia_ser_redirigido(context):
    target_url = BASE_URL
    current_url = context.page.url
    assert current_url == target_url, f"URL actual: {current_url}, URL objetivo: {target_url}"
    time.sleep(2)


# ---------------------------------------Adivinar una Letra Correcta-------------------------------------------------------------

@given('que estoy en la página de juego')
async def step_abrir_pagina_de_juego(context):
    browser = await async_playwright().start().chromium.launch(headless=False)
    context.browser = browser
    context.page = await browser.new_page()
    await context.page.goto(BASE_URL)


@when('ingreso la letra "{letra}"')
async def step_ingreso_letra(context, letra):
    await context.page.fill('input[name="letra"]', letra)
    await context.page.click('button[type="submit"]')


@then('debería ver la letra "{letra}" en la palabra oculta')
async def step_ver_letra_en_palabra_oculta(context, letra):
    palabra_oculta = await context.page.inner_text('#pal h2')
    assert letra in palabra_oculta


@then('el dibujo del muñeco del ahorcado debería seguir vacío')
async def step_deberia_ver_dibujo_vacio(context):
    page_source = await context.page.content()
    soup = BeautifulSoup(page_source, 'html.parser')
    dibujo_muñeco = soup.find('div', id='dibujo').pre.text

    assert '+---+' in dibujo_muñeco
    assert 'O   |' not in dibujo_muñeco


@then('el número de intentos restantes debería mantenerse')
async def step_ver_intentos_restantes(context):
    intentos_restantes = await context.page.inner_text('#intentos h2')
    assert intentos_restantes == 'Intentos restantes: 6'


# ---------------------------------------Adivinar una Letra Incorrecta-------------------------------------------------------------

@given('el contador de intentos está en 6')
async def step_contador_intentos_inicial(context):
    browser = await async_playwright().start().chromium.launch(headless=False)
    context.browser = browser
    context.page = await browser.new_page()
    await context.page.goto(BASE_URL)
    intentos_restantes = await context.page.inner_text('#intentos h2')
    assert intentos_restantes == 'Intentos restantes: 6'


@when('ingreso letra "{letra}"')
async def step_ingreso_letra_incorrecta(context, letra):
    await context.page.fill('input[name="letra"]', letra)
    await context.page.click('button[type="submit"]')


@then('debería ver el dibujo del muñeco del ahorcado con una parte dibujada')
async def step_ver_dibujo_con_parte_dibujada(context):
    page_source = await context.page.content()
    soup = BeautifulSoup(page_source, 'html.parser')
    dibujo_muñeco = soup.find('div', id='dibujo').pre.text

    assert '+---+' in dibujo_muñeco
    assert 'O   |' in dibujo_muñeco
    assert '/|\\' not in dibujo_muñeco


@then('el contador de intentos disminuye en 1')
async def step_contador_intentos_disminuye(context):
    intentos_restantes = await context.page.inner_text('#intentos h2')
    assert intentos_restantes == 'Intentos restantes: 5'


# --------------------------------------- Ganar el Juego -------------------------------------------------------------


# Función para ingresar una letra en el campo de entrada
def ingresar_letra(page, letra):
    input_selector = 'input[name="letra"]'
    page.wait_for_selector(input_selector)
    page.fill(input_selector, letra)
    page.click('button[type="submit"]')


# Steps para el escenario de adivinar correctamente todas las letras de la palabra oculta
@given('estoy en la página de juego')
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
            time.sleep(2)  # Agrega una pausa entre las adivinanzas para evitar problemas
            letras_adivinadas.add(letra)

    # Imprimir la palabra oculta final después de adivinar todas las letras
    palabra_oculta_actualizada = context.page.inner_text('#pal h2').strip().lower()
    print(f'Palabra oculta final: {palabra_oculta_actualizada}')


@then('el dibujo del muñeco del ahorcado debería estar en su estado inicial')
def step_ver_dibujo_estado_inicial(context):
    page_source = context.page.content()
    soup = BeautifulSoup(page_source, 'html.parser')
    dibujo_muñeco = soup.find('div', id='dibujo').pre.text

    assert '+---+' in dibujo_muñeco
    assert 'O   |' not in dibujo_muñeco
    time.sleep(2)


@then('el número de intentos restantes debe mantenerse')
def step_ver_intentos_restantes(context):
    intentos_restantes_text = context.page.inner_text('#intentos h2')
    assert 'Intentos restantes' in intentos_restantes_text
    assert intentos_restantes_text.split()[-1] != ''  # Aseguramos que el valor no esté vacío
    assert 'Intentos restantes: 6' in intentos_restantes_text
    time.sleep(2)


@then('debería ver el mensaje "¡Ganaste!"')
def step_verificar_mensaje_ganador(context):
    mensaje_ganador_element = context.page.wait_for_selector('#resultado h2')
    mensaje_ganador = mensaje_ganador_element.inner_text()
    assert '¡Ganaste!' in mensaje_ganador


# --------------------------------------- Perder el Juego -------------------------------------------------------------

# Función para ingresar una letra incorrecta en el campo de entrada
def ingresar_letra_incorrecta(page, letra):
    input_selector = 'input[name="letra"]'
    page.wait_for_selector(input_selector)
    page.fill(input_selector, letra)
    page.click('button[type="submit"]')


@given('que estoy en la página del juego')
async def step_abrir_pagina_del_juego(context):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context.browser = browser
        context.page = await browser.new_page()
        await context.page.goto(BASE_URL)
        time.sleep(2)


@when('adivino incorrectamente todas las letras de la palabra oculta')
async def step_adivino_incorrectamente(context):
    await step_abrir_pagina_del_juego(context)

    # Obtener la palabra oculta de la página
    palabra_oculta = await context.page.inner_text('#palabra h2').strip().lower()

    # Lista de letras incorrectas
    letras_incorrectas = ['x'] * 6

    for letra in letras_incorrectas:
        await asyncio.sleep(2)
        await ingresar_letra_incorrecta(context.page, letra)
    time.sleep(2)


@then('debería ver el dibujo completo del muñeco del ahorcado')
async def step_verificar_dibujo_completo(context):
    page_source = await context.page.content()
    assert '+---+' in page_source
    assert 'O   |' in page_source
    assert '/|\\  |' in page_source
    assert '/ \\  |' in page_source


@then('el número de intentos restantes debería llegar a cero')
async def step_verificar_numero_intentos_cero(context):
    intentos_restantes_text = await context.page.inner_text('#intentos h2')
    assert 'Intentos restantes: 0' in intentos_restantes_text
    time.sleep(2)


@then('debería ver el mensaje "¡Perdiste!"')
async def step_verificar_mensaje_perdiste(context):
    mensaje_perdiste_element = await context.page.wait_for_selector('#resultado h2')
    mensaje_perdiste = await mensaje_perdiste_element.inner_text()
    assert '¡Perdiste!' in mensaje_perdiste
    time.sleep(2)
