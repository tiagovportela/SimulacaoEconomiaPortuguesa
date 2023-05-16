import random

from .settings import LEGAL_AGE_MARRIAGE

from simulator.person.constants import MARRIAGE

class State:
    def __init__(self):
        self.allow_marriage = True
        self.money = 0

    def marry_people(self, person, population):
        other = random.choice(population)
        if other.age > LEGAL_AGE_MARRIAGE and person.age > LEGAL_AGE_MARRIAGE:
            if person.is_married == False and other.is_married == False and person.DNA[MARRIAGE] == True and other.DNA[MARRIAGE] == True:
                person.is_married = True
                other.is_married = True
                person.partner = other
                other.partner = person

                return


