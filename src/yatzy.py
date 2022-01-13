from src.pips import Pips

class Yatzy:

    # No es necesario.
    # Lo mantengo para no romper la interfaz
    # publica de la clase segun los
    # casos test originales.
    def __init__(self, *dice):
        self.dice = list(dice)

    @staticmethod
    def chance(*dice):
        score = 0
        for die in dice:
            score += die
        return score

    @staticmethod
    def yatzy(*dice):
        if dice.count(dice[0]) != len(dice):
            return 0
        return 50

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
        PAIR = 2
        for pip in Pips.reversedValues():
            if dice.count(pip) >= PAIR:
                return PAIR * pip
        return 0

    @staticmethod
    def two_pairs(*dice):
        PAIR = 2
        pips_pairs = list(filter(lambda pip: dice.count(pip) >= PAIR, Pips.reversedValues()))
        return sum(pips_pairs) * PAIR if len(pips_pairs) == 2 else 0

    @staticmethod
    def three_of_a_kind(*dice):
        THREE = 3
        for pip in Pips.reversedValues():
            if dice.count(pip) >= THREE:
                return THREE * pip
        return 0

    @staticmethod
    def four_of_a_kind(*dice):
        FOUR = 4
        for pip in Pips.reversedValues():
            if dice.count(pip) >= FOUR:
                return FOUR * pip
        return 0

    @staticmethod
    def small_straight(*dice):
        for pip in Pips.minus(Pips.SIX):
            if dice.count(pip) != 1:
                return 0
        return Yatzy.chance(*dice)

    @staticmethod
    def large_straight(*dice):
        for pip in Pips.minus(Pips.ONE):
            if dice.count(pip) != 1:
                return 0
        return Yatzy.chance(*dice)

    @staticmethod
    def fullHouse(*dice):
        if Yatzy.__par_bajo(*dice) and Yatzy.three_of_a_kind(*dice):
            return Yatzy.__par_bajo(*dice) + Yatzy.three_of_a_kind(*dice)
        else:
            return 0

    @staticmethod
    def __par_bajo(*dice):
        PAIR = 2
        for pip in Pips.reversedValues():
            if dice.count(pip) == PAIR:
                return PAIR * pip
        return 0
