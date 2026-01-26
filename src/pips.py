from enum import Enum, unique


@unique
class Pips(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6

    @classmethod
    def values(cls):
        return [number._value_ for number in Pips.__members__.values()]

    @classmethod
    def reversedValues(cls):
        return reversed(cls.values())

    @classmethod
    def minus(cls, pip):
        return set(cls.values()) - {pip.value}


if __name__ == "__main__":
    print("\n=== Conversión a lista ===")
    print(list(Pips))

    print("\n=== Acceso por valor (constructor) ===")
    print(Pips(1))

    print("\n=== Acceso por clave/nombre (string indexing) ===")
    print(Pips["ONE"])

    print("\n=== Acceso por atributo directo ===")
    print(Pips.ONE)

    print("\n=== Obtener nombre del miembro enum ===")
    print(Pips.ONE.name)

    print("\n=== Obtener valor del miembro enum ===")
    print(Pips.ONE.value)

    print("\n=== Iterar sobre miembros del enum ===")
    for number in Pips.__members__.values():
        print(f"  {number._name_}: {number._value_}")

    print("\n=== Obtener lista de valores (método personalizado) ===")
    print(Pips.values())

    print("\n=== Obtener valores invertidos (método personalizado) ===")
    print(list(Pips.reversedValues()))

    print(
        "\n=== Obtener valores sin FIVE (operación de resta - método personalizado) ==="
    )
    print(Pips.minus(Pips.FIVE))
