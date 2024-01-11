from src.pips import Pips

class Yatzy:

    # propiedades de clase
    ZERO = 0
    FIFTY = 50

    # No es necesario.
    # Lo mantengo para no romper la interfaz
    # publica de la clase segun los
    # casos test originales.
    def __init__(self, *dice):
        self.dice = list(dice)

    @staticmethod
    def chance(*dice):
        return sum(dice)

    @staticmethod
    def yatzy(*dice):
        if dice.count(dice[0]) != len(dice):
            return Yatzy.ZERO
        return Yatzy.FIFTY

    @staticmethod
    def ones(*dice):
        ONE = Pips.ONE.value
        return dice.count(ONE) * ONE

    @staticmethod
    def twos(*dice):
        TWO = Pips.TWO.value
        return dice.count(TWO) * TWO

    @staticmethod
    def threes(*dice):
        THREE = Pips.THREE.value
        return dice.count(THREE) * THREE

    def fours(self):
        FOUR = Pips.FOUR.value
        return self.dice.count(FOUR) * FOUR

    def fives(self):
        FIVE = Pips.FIVE.value
        return self.dice.count(FIVE) * FIVE

    def sixes(self):
        SIX = Pips.SIX.value
        return self.dice.count(SIX) * SIX

    @staticmethod
    def pair(*dice):
        PAIR = Pips.TWO.value
        for pip in Pips.reversedValues():
            if dice.count(pip) >= PAIR:
                return PAIR * pip
        return Yatzy.ZERO

    @classmethod
    def two_pairs(cls, *dice):
        PAIR = Pips.TWO.value
        pips_pairs = cls.__filter_pips_repeated(dice, PAIR)
        return sum(pips_pairs) * PAIR if len(pips_pairs) == Pips.TWO.value else Yatzy.ZERO

    @classmethod
    def three_of_a_kind(cls, *dice):
        THREE = Pips.THREE.value
        pip = cls.__biggest_pip_repeated(dice, THREE)
        return pip * THREE if pip else Yatzy.ZERO

    @classmethod
    def four_of_a_kind(cls, *dice):
        FOUR = Pips.FOUR.value
        pip = cls.__biggest_pip_repeated(dice, FOUR)
        return pip * FOUR if pip else Yatzy.ZERO

    @classmethod
    def __biggest_pip_repeated(cls, dice, times):
        pips = cls.__filter_pips_repeated(dice, times)
        return pips[0] if pips else []

    @classmethod
    def __filter_pips_repeated(cls, dice, times):
        return list(filter(lambda pip: dice.count(pip) >= times, Pips.reversedValues()))

    @classmethod
    def small_straight(cls, *dice):
        return cls.chance(*dice) if not Pips.minus(Pips.SIX) - set(dice) else Yatzy.ZERO

    @classmethod
    def large_straight(cls, *dice):
        return cls.chance(*dice) if not Pips.minus(Pips.ONE) - set(dice) else Yatzy.ZERO

    @classmethod
    def fullHouse(cls, *dice):
        if cls.two_of_a_kind(*dice) and cls.three_of_a_kind(*dice):
            return cls.two_of_a_kind(*dice) + cls.three_of_a_kind(*dice)
        else:
            return Yatzy.ZERO

    @classmethod
    def two_of_a_kind(cls, *dice):
        PAIR = Pips.TWO.value
        for pip in Pips.reversedValues():
            if dice.count(pip) == PAIR:
                return PAIR * pip
        return Yatzy.ZERO
