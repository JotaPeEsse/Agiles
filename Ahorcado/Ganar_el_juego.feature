Feature: Juego del Ahorcado
    Como jugador
    Quiero jugar al juego del ahorcado
    Para adivinar la palabra oculta

Scenario: Ganar el juego
    Given que estoy en la página de juego
    When adivino correctamente todas las letras de la palabra oculta
    Then el dibujo del muñeco del ahorcado debería estar en su estado inicial
    Then el número de intentos restantes debería mantenerse
    Then debería ver el mensaje "¡Ganaste!"