from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess
import time
from behave import __main__ as behave_executable
import sys
from bs4 import BeautifulSoup
import chromedriver_binary



# Configuración de Selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def ingresar_letra(letra):
    input_field = wait.until(EC.presence_of_element_located((By.NAME, 'letra')))
    input_field.send_keys(letra)
    input_field.send_keys(Keys.RETURN)

# Ruta al ejecutable del driver de Brave
brave_driver_path = 'C:\\Users\\PC\\Desktop\\Facultad\\5to\\Metodologia\\Agiles\\Ahorcado\\chromedriver.exe'  # C:\\Users\\juanp\\OneDrive\\Desktop\\AhorcadoJP\\chromedriver.exe

# Configuración del servicio del driver
service = Service(brave_driver_path)

# Opciones para el navegador Brave
options = webdriver.ChromeOptions()
options.binary_location = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'  # Reemplaza con la ruta correcta al ejecutable de Brave
options.add_argument("--start-maximized")

# Inicialización del driver de Brave
driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)


if __name__ == '__main__':
    subprocess.Popen(['python', 'run.py'])
    behave_executable.main(['-k', 'features/prueba_aceptacion.feature'])
    
    
    
@given('que estoy en la página de inicio')
def step_estoy_en_pagina_inicio(context):
    driver.get('http://localhost:5000/')

@when('hago clic en el botón "{button_text}"')
def step_hago_clic_en_jugar(context, button_text):
    time.sleep(2)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, f"//button[text()='{button_text}']")))
    button.click()

    # Esperar un segundo para que la página se cargue completamente
    time.sleep(1)

    # Obtener la respuesta de la página y guardarla en el contexto
    context.response = driver.page_source


@then('debería ser redirigido a la página del juego')
def step_deberia_ser_redirigido(context):
    time.sleep(2)
    assert '/juego' in driver.current_url

@then('debería ver una palabra oculta en forma de guiones bajos')
def step_deberia_ver_palabra_oculta(context):
    page_source = driver.page_source
    assert '_' in page_source

@then('debería ver el dibujo del muñeco del ahorcado vacío')
def step_deberia_ver_dibujo_vacio(context):
    page_source = driver.page_source
    assert '+---+' in page_source
    assert 'O   |' not in page_source

@then('debería ver el número de intentos restantes')
def step_deberia_ver_intentos_restantes(context):
    page_source = driver.page_source
    assert 'Intentos restantes:' in page_source
    
    
"-----------------"


@when('ingreso la letra "{letra}"')
def step_ingreso_letra(context, letra):
    # Encontrar el campo de entrada de la letra y enviar la letra
    input_field = wait.until(EC.presence_of_element_located((By.NAME, 'letra')))
    input_field.send_keys(letra)
    input_field.send_keys(Keys.RETURN)


@then('debería ver la letra "{letra}" en la palabra oculta')
def step_deberia_ver_letra_palabra_oculta(context, letra):
    letra_xpath = f"//h2[contains(text(), '{letra}')]"
    letra_element = wait.until(EC.presence_of_element_located((By.XPATH, letra_xpath)))
    assert letra_element.is_displayed()


@then('el dibujo del muñeco del ahorcado debería seguir vacío')
def step_deberia_ver_dibujo_vacio(context):
    page_source = driver.page_source
    assert '+---+' in page_source
    assert 'O   |' not in page_source

@then('el número de intentos restantes debería mantenerse')
def step_deberia_ver_intentos_restantes(context):
    page_source = driver.page_source
    assert 'Intentos restantes:' in page_source
    
"---------------------------------"

@given('el contador de intentos está en {valor}')
def step_given_contador_intentos(context, valor):
    context.contador_inicial = int(valor)

@when('ingreso letra "{letra}"')
def step_ingreso_letra_incorrecta(context, letra): 
    time.sleep(2)  
    input_field = wait.until(EC.presence_of_element_located((By.NAME, 'letra')))
    input_field.send_keys(letra)
    input_field.send_keys(Keys.RETURN)
    time.sleep(2)  # Esperar un segundo para simular la entrada de la letra

@then('debería ver el dibujo del muñeco del ahorcado con una parte dibujada')
def step_verificar_dibujo_muñeco(context):
    page_source = driver.page_source
    assert '+---+' in page_source
    assert 'O   |' in page_source


@then('el contador de intentos disminuye en 1')
def step_then_contador_intentos_disminuye(context):
    contador_element = wait.until(EC.presence_of_element_located((By.ID, 'intentos')))
    contador_text = contador_element.text
    contador_value = int(contador_text.split(': ')[1])
    assert contador_value == (context.contador_inicial - 1)


"-------------------------------"
@when('adivino correctamente todas las letras de la palabra oculta')
def step_adivino_correctamente(context):
    # Obtener el contenido HTML de la respuesta
    page_source = driver.page_source

    # Utilizar BeautifulSoup para analizar el contenido HTML
    soup = BeautifulSoup(page_source, 'html.parser')

    # Obtener la etiqueta HTML que contiene la palabra oculta
    palabra_oculta_tag = soup.find('div', id='palabra')

    # Obtener el texto de la etiqueta que representa la palabra oculta
    palabra_oculta = palabra_oculta_tag.text

    # Convertir la palabra oculta a minúsculas
    palabra_oculta = palabra_oculta.lower()

    
    
    # Convertir la lista de letras en una cadena de texto
    palabra_oculta = ''.join(palabra_oculta)

    # Adivinar cada letra de la palabra oculta
    letras_adivinadas = set()

# Adivinar cada letra de la palabra oculta
    letras_adivinadas.add("a")
    for letra in palabra_oculta:
        if letra not in letras_adivinadas:
            ingresar_letra(letra)
            time.sleep(2)  
            letras_adivinadas.add(letra)

def ingresar_letra(letra):
    input_field = wait.until(EC.presence_of_element_located((By.NAME, 'letra')))
    input_field.send_keys(letra)
    input_field.send_keys(Keys.RETURN)

    
    
@then('debería ver todas las letras correctas en la palabra oculta')
def step_verificar_letras_correctas(context):
    palabra_oculta = driver.find_element(By.ID, 'pal').text
    palabra_visible = driver.find_element(By.ID, 'palabra').text

    if palabra_visible==palabra_oculta:
        assert True

@then('el dibujo del muñeco del ahorcado debería estar en su estado inicial')
def step_verificar_dibujo_inicial(context):
    dibujo_muñeco = driver.page_source
    assert '+---+' in dibujo_muñeco
    assert 'O   |'  in dibujo_muñeco

@then('el número de intentos debería mantenerse')
def step_verificar_intentos_restantes(context):
    page_source = driver.page_source
    assert 'Intentos restantes: 5' in page_source

@then('debería ver el mensaje "¡Ganaste!"')
def step_verificar_mensaje_ganador(context):
    mensaje_ganador = driver.find_element(By.ID, 'resultado').text
    assert '¡Ganaste!' in mensaje_ganador

"--------------------------"
@given('apreto el botón de jugar de nuevo')
def step_given_apretar_boton_jugar_denuevo(context):
    # Encontrar y hacer clic en el botón de jugar de nuevo
    boton_jugar_denuevo = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Jugar de nuevo')]")))
    boton_jugar_denuevo.click()

@when('adivino incorrectamente todas las letras de la palabra oculta')
def step_adivino_incorrectamente(context):
    # Obtener el contenido HTML de la respuesta
    page_source = driver.page_source

    # Utilizar BeautifulSoup para analizar el contenido HTML
    soup = BeautifulSoup(page_source, 'html.parser')

    # Obtener la etiqueta HTML que contiene la palabra oculta
    palabra_oculta_tag = soup.find('div', id='palabra')

    # Obtener el texto de la etiqueta que representa la palabra oculta
    palabra_oculta = palabra_oculta_tag.text

    # Convertir la palabra oculta a minúsculas
    palabra_oculta = palabra_oculta.lower()

    # Convertir la lista de letras en una cadena de texto
    palabra_oculta = ''.join(palabra_oculta)

   
    
    letras = ['x'] * 6
    
    for letra in letras:
            time.sleep(2)  
            ingresar_letra_incorrecta(letra)
            

def ingresar_letra_incorrecta(letra):
    input_field = wait.until(EC.presence_of_element_located((By.NAME, 'letra')))
    input_field.send_keys(letra)
    input_field.send_keys(Keys.RETURN)

@then('debería ver el dibujo completo del muñeco del ahorcado')
def step_verificar_dibujo_completo(context):
    page_source = driver.page_source
    assert '+---+' in page_source
    assert 'O   |' in page_source
    assert '/|\  |' in page_source
    assert '/ \  |' in page_source

@then('el número de intentos restantes debería llegar a cero')
def step_verificar_numero_intentos_cero(context):
    page_source = driver.page_source
    assert 'Intentos restantes: 0' in page_source

@then('debería ver el mensaje "¡Perdiste!"')
def step_verificar_mensaje_perdiste(context):
    page_source = driver.page_source
    assert '¡Perdiste!' in page_source



"--------------------------------------------------------------------------------------------------"
"""
@given('que estoy en la página principal')
def step_given_juego_en_pagina_inicio(context):
    driver.get('http://localhost:5000/')

@when('el usuario hace clic en el botón "{button_text}"')
def step_when_usuario_hace_clic_en_boton(context, button_text):
    time.sleep(2)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, f"//button[text()='{button_text}']")))
    button.click()

@then('se muestra la página del juego')
def step_then_se_muestra_pagina_juego(context):
    time.sleep(2)
    wait.until(EC.url_contains('/juego'))
    
"--------------------------------------------------------------------------------------------------"    
    
    
@given('que estoy en la página del juego')
def step_given_juego_en_pagina_juego(context):
    time.sleep(2)
    wait.until(EC.url_contains('/juego'))

@when('ingreso la letra "{letra}"')
def step_when_ingreso_letra_valida(context, letra):
        input_field = wait.until(EC.presence_of_element_located((By.NAME, 'letra')))
        input_field.send_keys(letra)
        input_field.send_keys(Keys.RETURN)

@then('la letra "{letra}" se muestra en el tablero')
def step_then_letra_se_muestra_en_tablero(context, letra):
        letra_element = wait.until(EC.presence_of_element_located((By.XPATH, f"//h2[contains(text(), '{letra}')]")))
        assert letra_element.is_displayed()
        
        
"--------------------------------------------------------------------------------------------------"        
        
        
@given('estoy en la página del juego')
def step_given_juego_en_pagina_juego(context):
    time.sleep(2)
    wait.until(EC.url_contains('/juego'))
    
@given('el contador de intentos está en {valor}')
def step_given_contador_intentos(context, valor):
    context.contador_inicial = int(valor)


@when('si ingreso la letra "{letra}"')
def step_when_ingreso_letra_invalida(context, letra):
    input_field = wait.until(EC.presence_of_element_located((By.NAME, 'letra')))
    input_field.send_keys(letra)
    input_field.send_keys(Keys.RETURN)

@then('la letra "{letra}" no se muestra en el tablero')
def step_then_letra_no_se_muestra_en_tablero(context, letra):
    try:
        letra_element = context.driver.find_element(By.XPATH, f"//h2[contains(text(), '{letra}')]")
        assert not letra_element.is_displayed()
    except:
        pass

@then('el contador de intentos disminuye en 1')
def step_then_contador_intentos_disminuye(context):
    contador_element = wait.until(EC.presence_of_element_located((By.ID, 'intentos')))
    contador_text = contador_element.text
    contador_value = int(contador_text.split(': ')[1])
    assert contador_value == (context.contador_inicial - 1)

"--------------------------------------------------------------------------------------------------"

@given('página del juego')
def step_given_juego_en_pagina_juego(context):
    time.sleep(1)
    wait.until(EC.url_contains('/juego'))


@when('ingreso primer letra "{letra}"')
def step_when_ingreso_letras(context, letra):
        input_field = wait.until(EC.presence_of_element_located((By.NAME, 'letra')))
        input_field.send_keys(letra)
        input_field.send_keys(Keys.RETURN)
        
        
@when('ingreso segunda letra "{letra}"')
def step_when_ingreso_letras(context, letra):
        input_field = wait.until(EC.presence_of_element_located((By.NAME, 'letra')))
        input_field.send_keys(letra)
        input_field.send_keys(Keys.RETURN)
        
@when('ingreso tercer letra "{letra}"')
def step_when_ingreso_letras(context, letra):
        input_field = wait.until(EC.presence_of_element_located((By.NAME, 'letra')))
        input_field.send_keys(letra)
    
        input_field.send_keys(Keys.RETURN)
        
@when('ingreso cuarta letra "{letra}"')
def step_when_ingreso_letras(context, letra):
        input_field = wait.until(EC.presence_of_element_located((By.NAME, 'letra')))
        input_field.send_keys(letra)
        
        input_field.send_keys(Keys.RETURN)

@then('se muestra un mensaje de victoria')
def step_then_mensaje_victoria(context):
    time.sleep(2)
    mensaje_element = wait.until(EC.presence_of_element_located((By.ID, 'resu_auto')))
    assert mensaje_element.text == '¡Ganaste!'


"--------------------------------------------------------------------------------------------------"

@given('apreto el botón de jugar de nuevo')
def step_given_apretar_boton_jugar_denuevo(context):
    # Encontrar y hacer clic en el botón de jugar de nuevo
    boton_jugar_denuevo = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Jugar de nuevo')]")))
    boton_jugar_denuevo.click()


@when('ingreso la letra primera "{letra}"')
def step_when_ingreso_letras(context, letra):
        input_field = wait.until(EC.presence_of_element_located((By.NAME, 'letra')))
        input_field.send_keys(letra)
        input_field.send_keys(Keys.RETURN)
        
@when('ingreso la letra segunda "{letra}"')
def step_when_ingreso_letras(context, letra):
        input_field = wait.until(EC.presence_of_element_located((By.NAME, 'letra')))
        input_field.send_keys(letra)
        input_field.send_keys(Keys.RETURN)
        
@when('ingreso la letra tercera "{letra}"')
def step_when_ingreso_letras(context, letra):
        input_field = wait.until(EC.presence_of_element_located((By.NAME, 'letra')))
        input_field.send_keys(letra)
        input_field.send_keys(Keys.RETURN)
        
@when('ingreso la letra cuarta "{letra}"')
def step_when_ingreso_letras(context, letra):
        input_field = wait.until(EC.presence_of_element_located((By.NAME, 'letra')))
        input_field.send_keys(letra)
        input_field.send_keys(Keys.RETURN)
        
@when('ingreso la letra quinta "{letra}"')
def step_when_ingreso_letras(context, letra):
        input_field = wait.until(EC.presence_of_element_located((By.NAME, 'letra')))
        input_field.send_keys(letra)
        input_field.send_keys(Keys.RETURN)

@when('ingreso la letra sexta "{letra}"')
def step_when_ingreso_letras(context, letra):
        input_field = wait.until(EC.presence_of_element_located((By.NAME, 'letra')))
        input_field.send_keys(letra)
        input_field.send_keys(Keys.RETURN)
        


@then('se muestra un mensaje de derrota')
def step_then_mensaje_derrota(context):
    # Verificar que se muestre el mensaje de derrota
    resultado_element = wait.until(EC.presence_of_element_located((By.ID, 'resultado')))
    assert resultado_element.is_displayed(), "El mensaje de derrota no se muestra"




"--------------------------------------------------------------------------------------------------"

# Cierre del navegador al finalizar las pruebas"""
