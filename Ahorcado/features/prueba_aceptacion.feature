Feature: Juego del Ahorcado
    Como jugador
    Quiero jugar al juego del ahorcado
    Para adivinar la palabra oculta

Scenario: Iniciar el juego
    Given que estoy en la página de inicio
    When hago clic en el botón "Jugar"
    Then debería ser redirigido a la página del juego
    And debería ver una palabra oculta en forma de guiones bajos
    And debería ver el dibujo del muñeco del ahorcado vacío
    And debería ver el número de intentos restantes

Scenario: Adivinar una letra correcta
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
    When adivino correctamente todas las letras de la palabra oculta
    Then debería ver todas las letras correctas en la palabra oculta
    And el dibujo del muñeco del ahorcado debería estar en su estado inicial
    And el número de intentos debería mantenerse
    And debería ver el mensaje "¡Ganaste!"

    
Scenario: Perder el juego
    Given apreto el botón de jugar de nuevo
    When adivino incorrectamente todas las letras de la palabra oculta
    Then debería ver el dibujo completo del muñeco del ahorcado
    And el número de intentos restantes debería llegar a cero
    And debería ver el mensaje "¡Perdiste!"
    
