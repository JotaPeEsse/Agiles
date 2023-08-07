from playwright.sync_api import Page, Browser, sync_playwright
from behave import given, when, then
import time


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
    
    

@pytest.fixture
def context():
    return {}