# Yatzy Refactoring Kata

**Kata readme by [Emily Bache](https://github.com/emilybache)** Thanks!! :clap::clap:

[Emily Bache kata repo](https://github.com/emilybache/Yatzy-Refactoring-Kata)

*Designed by Jon Jagger. It's available in his Cyber-Dojo. [Blog post](http://jonjagger.blogspot.co.uk/2012/05/yahtzee-cyber-dojo-refactoring-in-java.html)*

## Kata: Yatzy rules

The game of Yatzy is a simple dice game. Each player
rolls five six-sided dice. They can re-roll some or all
of the dice up to three times (including the original roll).

For example, suppose a players rolls:

    3,4,5,5,2
    
They hold (-,-,5,5,-) and re-roll (3,4,-,-,2):

    5,1,5,5,3

They hold (5,-,5,5,-) and re-roll (-,1,-,-,3):

    5,6,5,5,2

The player then places the roll in a category, such as ones,
twos, fives, pair, two pairs etc (see below). If the roll is
compatible with the category, the player gets a score for the
roll according to the rules. If the roll is not compatible
with the category, the player scores zero for the roll.

For example, suppose a player scores 5,6,5,5,2 in the fives
category they would score 15 (three fives). The score for
that go is then added to their total and the category cannot
be used again in the remaining goes for that game.
A full game consists of one go for each category. Thus, for
their last go in a game, a player must choose their only
remaining category.

Your task is to score a GIVEN roll in a GIVEN category.
You do NOT have to program the random dice rolling.
The game is NOT played by letting the computer choose the
highest scoring category for a given roll.
  
## Kata: Yatzy Categories and Scoring Rules

### Chance

The player scores the sum of all dice, no matter what they read.
For example:
  
- 1,1,3,3,6 placed on "chance" scores 14 (1+1+3+3+6)
- 4,5,5,6,1 placed on "chance" scores 21 (4+5+5+6+1)  

### Yatzy

If all dice have the same number, the player scores 50 points.
For example:
  
- 1,1,1,1,1 placed on "yatzy" scores 50
- 1,1,1,2,1 placed on "yatzy" scores 0

### Ones, Twos, Threes, Fours, Fives, Sixes

The player scores the sum of the dice that reads one, two, three, four, five or six, respectively.For example:

- 1,1,2,4,4 placed on "fours" scores 8 (4+4)
- 2,3,2,5,1 placed on "twos" scores 4  (2+2)
- 3,3,3,4,5 placed on "ones" scores 0

### Pair

The player scores the sum of the two highest matching dice.
For example, when placed on "pair":
  
- 3,3,3,4,4 scores 8 (4+4)
- 1,1,6,2,6 scores 12 (6+6)
- 3,3,3,4,1 scores 6 (3+3)
- 3,3,3,3,1 scores 6 (3+3)

### Two pairs

If there are two pairs of dice with the same number, the player scores the sum of these dice. For example, when placed on "two pairs":
  
- 1,1,2,3,3 scores 8 (1+1+3+3)
- 1,1,2,3,4 scores 0
- 1,1,2,2,2 scores 6 (1+1+2+2)

### Three of a kind

If there are three dice with the same number, the player
scores the sum of these dice.

For example, when placed on "three of a kind":

- 3,3,3,4,5 scores 9 (3+3+3)
- 3,3,4,5,6 scores 0
- 3,3,3,3,1 scores 9 (3+3+3)

### Four of a kind

If there are four dice with the same number, the player scores the sum of these dice.

For example, when placed on "four of a kind":
  
- 2,2,2,2,5 scores 8 (2+2+2+2)
- 2,2,2,5,5 scores 0
- 2,2,2,2,2 scores 8 (2+2+2+2)

### Small straight

When placed on "small straight", if the dice read

   1,2,3,4,5,

the player scores 15 (the sum of all the dice).

### Large straight

When placed on "large straight", if the dice read

    2,3,4,5,6,

the player scores 20 (the sum of all the dice).

### Full house

If the dice are two of a kind and three of a kind, the player scores the sum of all the dice.

For example, when placed on "full house":

- 1,1,2,2,2 scores 8 (1+1+2+2+2)
- 2,2,3,3,4 scores 0
- 4,4,4,4,4 scores 0

---

## Métodos de clase en Python: `@staticmethod` vs `@classmethod`

Lee el código en [`yatzy_refactored.py`](./src/yatzy_refactored.py)

### Objetivo 🎯

Explicar, con ejemplos prácticos sacados de `src/yatzy_refactored.py`, cuándo y por qué usar `@staticmethod` y `@classmethod` en Python.

---

### Resumen breve ✅

- `@staticmethod`: función ligada a la clase por SRP; **no recibe** ni `self` ni `cls`. Útil para operaciones puramente funcionales relacionadas con la clase que no necesitan acceder al estado de una instancia o de la clase.

- `@classmethod`: método que recibe la **clase** como primer argumento (`cls`). Útil cuando el comportamiento necesita acceder o modificar datos de clase, o cuando queremos que el método sea heredable por subclases.

---

### Diferencias 🔍

- Signatura: `def f(*args)` vs `def f(cls, *args)`
- Acceso: no puede usar atributos de clase (`staticmethod`) ↔ usa `cls` para acceder/alterar atributos o invocar otros métodos de clase
- Heredabilidad: `classmethod` respeta la clase que llama; `staticmethod` es independiente de la clase que la contiene

---

### Ejemplos del proyecto 🔧

#### 1- `@staticmethod` — función pura relacionada con la lógica del juego

```python
@staticmethod
def chance(*dice):
    return sum(dice)

@staticmethod
def yatzy(*dice):
    return Yatzy.FIFTY if len(set(dice)) == 1 else Yatzy.ZERO
```

Por qué usamos `staticmethod` aquí:

- Estas funciones calculan un resultado a partir de los argumentos (`dice`) y **no necesitan** acceder a la instancia (`self`) ni a la clase (`cls`).
- Son utilitarias: su comportamiento no cambia si la clase se hereda.

#### 2- `@classmethod` — necesita conocer la clase o usar otros métodos de clase

```python
@classmethod
def pair(cls, *dice):
    PAIR = Pips.TWO.value
    pip = cls.__biggest_pip_repeated(dice, PAIR)
    return pip * PAIR if pip else Yatzy.ZERO

@classmethod
def small_straight(cls, *dice):
    return cls.chance(*dice) if not Pips.minus(Pips.SIX) - set(dice) else Yatzy.ZERO
```

Por qué usamos `classmethod` aquí:

- `pair` y `small_straight` llaman a otros métodos que pertenecen a la clase (por ejemplo `cls.__biggest_pip_repeated`, `cls.chance`). Usar `cls` permite que una subclase que reimplemente esos métodos conserve el comportamiento correcto.
- `classmethod` facilita la extensibilidad y la reutilización por herencia.

#### 3- Método de instancia

```python
def fours(self):
    return self.__sum_dice_equals(Pips.FOUR.value)
```

Este método usa `self.dice`, el estado de una instancia u objeto de la clase, por eso NO puede ser `@staticmethod` ni `@classmethod`.

---

### Buenas prácticas y recomendaciones 💡

- Usa `@staticmethod` para utilidades que no requieren ni `cls` ni `self` (pure functions relacionadas conceptualmente con la clase).
- Usa `@classmethod` cuando el método **debe conocer la clase** que lo invoca (para acceder a atributos de clase, construir instancias, o apoyar herencia).
- Preferir `cls.CONSTANT` dentro de `@classmethod` para mantener compatibilidad con subclases.
- Evitar mezclar responsabilidades: si el método necesita estado de instancia, debe ser un método de instancia.

---

### Preguntas tipo examen (con respuestas) ✅

1. ¿Qué recibe siempre un `@classmethod` como primer argumento? — `cls` (la clase que llama).
2. ¿Es `@staticmethod` heredable por una subclase? — Sí, pero no obtiene ninguna referencia a la subclase a menos que se le pase explícitamente.
3. Verdadero/Falso: Un `@classmethod` puede llamar a otros `@classmethod` usando `cls`. — Verdadero.

---

### Conexión con `Pips` (enum) 🧩

`Pips.reversedValues()` y `Pips.minus()` están definidos como `@classmethod` en el `Enum`: eso tiene sentido porque operan sobre los miembros de la clase `Enum` y su comportamiento debe ser coherente con la clase, no con una instancia concreta.

---

### Prompt

`#file:yatzy_refactored.py #file:test_yatzy_from_scratch.py #file:pips.py`

He resuelto el kata Yatzy sobre refactorización.

Utilizo este kata como introducción a la programación orientada a objetos en Python y, en particular, a los distintos tipos de métodos de clase: `staticmethod` y `classmethod`.

Redacta un fichero markdown para mi alumnado de formación profesional de desarrollo de aplicaciones multiplataforma en el módulo de programación donde expliques los conceptos de programación Python y orientada a objetos sobre los métodos de clase `staticmethod` y `classmethod` utilizando los métodos del fichero #file:yatzy_refactored.py como ejemplo.

El manual de referencia que usamos en el aula es Learning Python de Mark Lutz.
