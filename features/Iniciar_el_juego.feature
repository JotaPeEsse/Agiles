Feature: Juego del Ahorcado
    Como jugador
    Quiero jugar al juego del ahorcado
    Para adivinar la palabra oculta

Scenario: Iniciar el juego
    Given que estoy en la página de inicio
    When hago clic en el botón "Jugar"
    Then debería ser redirigido a la página del juego


Scenario: Ganar el juego
    Given que estoy en la página de juego
    When adivino correctamente todas las letras de la palabra oculta
    Then el dibujo del muñeco del ahorcado debería estar en su estado inicial
    Then el número de intentos restantes debería mantenerse
    Then debería ver el mensaje "¡Ganaste!"
    Then cierro el navegador
    
Scenario: Adivinar una letra correcta
    Given estoy en la página de juego
    When ingreso la letra "a"
    Then debería ver la letra "a" en la palabra oculta
    Then el dibujo del muñeco del ahorcado debería seguir vacío
    Then el número de intentos restantes debe mantenerse  