Feature: Juego del Ahorcado
    Como jugador
    Quiero jugar al juego del ahorcado
    Para adivinar la palabra oculta

Scenario: Iniciar el juego
    Given que estoy en la página de inicio
    When hago clic en el botón "Jugar"
    Then debería ser redirigido a la página del juego

Scenario: Adivinar una letra correcta
    Given que estoy en la página de juego
    When ingreso la letra "a"
    Then debería ver la letra "a" en la palabra oculta
    And el dibujo del muñeco del ahorcado debería seguir vacío
    And el número de intentos restantes debería mantenerse

Scenario: Adivinar una letra incorrecta
    Given el contador de intentos está en 6
    When ingreso letra "z"
    Then debería ver el dibujo del muñeco del ahorcado con una parte dibujada
    And el contador de intentos disminuye en 1

Scenario: Ganar el juego
    Given estoy en la página de juego
    When adivino correctamente todas las letras de la palabra oculta
    Then el dibujo del muñeco del ahorcado debería estar en su estado inicial
    Then el número de intentos restantes debe mantenerse
    Then debería ver el mensaje "¡Ganaste!"

Scenario: Perder el juego
    Given que estoy en la página del juego 
    When adivino incorrectamente todas las letras de la palabra oculta
    Then debería ver el dibujo completo del muñeco del ahorcado
    And el número de intentos restantes debería llegar a cero
    And debería ver el mensaje "¡Perdiste!"