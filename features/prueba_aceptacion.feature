Feature: Juego del Ahorcado
    Como jugador
    Quiero jugar al juego del ahorcado
    Para adivinar la palabra oculta

Scenario: Iniciar el juego
    Given que estoy en la página de inicio
    When hago clic en el botón "Jugar"
    Then debería ser redirigido a la página del juego