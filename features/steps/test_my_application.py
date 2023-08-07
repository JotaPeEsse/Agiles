


import time
from behave import given, when, then
from playwright.sync_api import sync_playwright

#

@given('abro la página del ahorcado')
def step_abrir_pagina_ahorcado(context):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context.page = browser.new_page()
        context.page.goto('http://martinb.pythonanywhere.com/')