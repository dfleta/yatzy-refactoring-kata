# Métodos de clase en Python: `@staticmethod` vs `@classmethod` (usando `yatzy_refactored.py`)

## Objetivo 🎯
Explicar, con ejemplos prácticos sacados de `src/yatzy_refactored.py`, cuándo y por qué usar `@staticmethod` y `@classmethod` en Python. Al final hay ejercicios cortos para practicar y preguntas tipo test.

---

## Resumen breve ✅
- `@staticmethod`: función ligada a la clase por SRP; **no recibe** ni `self` ni `cls`. Útil para operaciones puramente funcionales relacionadas con la clase que no necesitan acceder al estado de una instancia o de la clase.
- `@classmethod`: método que recibe la **clase** como primer argumento (`cls`). Útil cuando el comportamiento necesita acceder o modificar datos de clase, o cuando queremos que el método sea heredable por subclases.

---

## Diferencias 🔍
- Signatura: `def f(*args)` vs `def f(cls, *args)`
- Acceso: no puede usar atributos de clase (`staticmethod`) ↔ usa `cls` para acceder/alterar atributos o invocar otros métodos de clase
- Heredabilidad: `classmethod` respeta la clase que llama; `staticmethod` es independiente de la clase que la contiene

---

## Ejemplos del proyecto 🔧

### 1- `@staticmethod` — función pura relacionada con la lógica del juego

```python
@staticmethod
def chance(*dice):
    return sum(dice)

@staticmethod
def yatzy(*dice):
    return Yatzy.FIFTY if len(set(dice)) == 1 else Yatzy.ZERO
```

Por qué `staticmethod` aquí:
- Estas funciones calculan un resultado a partir de los argumentos (`dice`) y **no necesitan** acceder a la instancia (`self`) ni a la clase (`cls`).
- Son utilitarias: su comportamiento no cambia si la clase se hereda.

### 2- `@classmethod` — necesita conocer la clase o usar otros métodos de clase

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

Por qué `classmethod` aquí:
- `pair` y `small_straight` llaman a otros métodos que pertenecen a la clase (por ejemplo `cls.__biggest_pip_repeated`, `cls.chance`). Usar `cls` permite que una subclase que reimplemente esos métodos conserve el comportamiento correcto.
- `classmethod` facilita la extensibilidad y la reutilización por herencia.

### 3- Método de instancia
```python
def fours(self):
    return self.__sum_dice_equals(Pips.FOUR.value)
```

Este método usa `self.dice`, el estado de una instancia u objeto de la clase, por eso NO puede ser `@staticmethod` ni `@classmethod`.

---

## Buenas prácticas y recomendaciones 💡
- Usa `@staticmethod` para utilidades que no requieren ni `cls` ni `self` (pure functions relacionadas conceptualmente con la clase).
- Usa `@classmethod` cuando el método **debe conocer la clase** que lo invoca (para acceder a atributos de clase, construir instancias, o apoyar herencia).
- Preferir `cls.CONSTANT` dentro de `@classmethod` para mantener compatibilidad con subclases.
- Evitar mezclar responsabilidades: si el método necesita estado de instancia, debe ser un método de instancia.

---

## Preguntas tipo examen (con respuestas) ✅
1. ¿Qué recibe siempre un `@classmethod` como primer argumento? — `cls` (la clase que llama).
2. ¿Es `@staticmethod` heredable por una subclase? — Sí, pero no obtiene ninguna referencia a la subclase a menos que se le pase explícitamente.
3. Verdadero/Falso: Un `@classmethod` puede llamar a otros `@classmethod` usando `cls`. — Verdadero.

---

## Conexión con `Pips` (enum) 🧩
`Pips.reversedValues()` y `Pips.minus()` están definidos como `@classmethod` en el `Enum`: eso tiene sentido porque operan sobre los miembros de la clase `Enum` y su comportamiento debe ser coherente con la clase, no con una instancia concreta.

---


Prompt:

#file:yatzy_refactored.py #file:test_yatzy_from_scratch.py #file:pips.py 

He resuelto el kata Yatzy sobre refactorización.

Utilizo este kata como introducción a la programación orientada a objetos en Python y, en particular, a los distintos tipos de métodos de clase: `staticmethod` y `classmethod`.

Redacta un fichero markdown para mi alumnado de formación profesional de desarrollo de aplicaciones multiplataforma en el módulo de programación donde expliques los conceptos de programación Python y orientada a objetos sobre los métodos de clase `staticmethod` y `classmethod` utilizando los métodos del fichero #file:yatzy_refactored.py como ejemplo.

El libro de referencia que usamos en el aula es Learning Python de Mark Lutz.
