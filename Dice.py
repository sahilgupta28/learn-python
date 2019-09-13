import random


class Dice:
    def rolls(self):
        roll = [ ( random.randint(0, 6) ) for k in range(6) ]
        return roll


dice1 = Dice()
print(dice1.rolls())