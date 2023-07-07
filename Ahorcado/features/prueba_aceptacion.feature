Feature: Juego del Ahorcado

  Scenario: Comienzo del juego
    Given que estoy en la página principal
    When el usuario hace clic en el botón "Jugar"
    Then se muestra la página del juego

  Scenario: Ingresar una letra válida
    Given que estoy en la página del juego
    When ingreso la letra "a"
    Then la letra "a" se muestra en el tablero

  Scenario: Ingresar una letra inválida
    Given estoy en la página del juego
    And el contador de intentos está en 6
    When si ingreso la letra "x"
    Then la letra "x" no se muestra en el tablero
    And el contador de intentos disminuye en 1

  Scenario: Ganar el juego
    Given página del juego
    When ingreso primer letra "g"
    When ingreso segunda letra "a"
    When ingreso tercer letra "t"
    When ingreso cuarta letra "o"
    Then se muestra un mensaje de victoria
    
  Scenario: Perder el juego
    Given apreto el botón de jugar de nuevo
    When ingreso la letra primera "b"
    When ingreso la letra segunda "h"
    When ingreso la letra tercera "f"
    When ingreso la letra cuarta "s"
    When ingreso la letra quinta "q"
    When ingreso la letra sexta "r"
    Then se muestra un mensaje de derrota