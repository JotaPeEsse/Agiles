from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess
import time
from behave import __main__ as behave_executable
import re


# Configuración de Selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Ruta al ejecutable del driver de Brave
brave_driver_path = 'C:\\Users\\PC\\Desktop\\Facultad\\5to\\Metodologia\\Agiles\\Ahorcado\\chromedriver.exe'  # Reemplaza con la ruta correcta al ejecutable del driver de Brave

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
    subprocess.Popen(['python', 'front.py'])
    
    behave_executable.main(['-k', 'features/prueba_aceptacion.feature'])

"--------------------------------------------------------------------------------------------------"

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

# Cierre del navegador al finalizar las pruebas
