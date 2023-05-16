import random

from .settings import PROBABILITY_SCHOOL_LEVELS_MAN, PROBABILITY_SCHOOL_LEVELS_WOMAN, SCHOOL_LEVELS
from .settings import SALARY_BY_EDUCATION
from .settings import COST_OF_UNIVERSAL_HEALTH_SYSTEM_PER_CAPITA

from .constants import AGE_DEAD, AGE_BORN_CHILD, INVEST, SAVE_MONEY, CREDIT, SEX, MARRIAGE, STUDY, DEAD_CAUSE_NATURAL, DEAD_CAUSE_CANT_PROVIDE_BASIC_NEEDS

from .helpers import gene
from .helpers import living_cost
from .helpers import random_variation_salary

class Person:
    def __init__(self):
        self.age = 0
        self.money = 0
        self.is_working = False
        self.is_studing = False
        self.is_alive = True
        self.childs = []
        self.is_married = False
        self.other_person = None
        self.DNA = {
            AGE_DEAD: gene(AGE_DEAD), # implemented
            AGE_BORN_CHILD: gene(AGE_BORN_CHILD),# implemented
            INVEST: gene(INVEST),# implemented
            SAVE_MONEY: gene(SAVE_MONEY),# implemented
            CREDIT: gene(CREDIT),# implemented
            SEX: gene(SEX),# implemented
            MARRIAGE: gene(MARRIAGE),
        }
        self.will_study()
        #only women can give birth
        if self.DNA[SEX] == 'M':
            self.DNA[AGE_BORN_CHILD] = []

        self.years_without_basic_needs = 0
        self.dead_cause = None
        self.children = []
        self.partner = None
    def will_study(self):
        sex = self.DNA[SEX]
        if sex == 'M':
            self.DNA[STUDY] = random.choices(SCHOOL_LEVELS, weights=PROBABILITY_SCHOOL_LEVELS_MAN)[0]
        else:
            self.DNA[STUDY] = random.choices(SCHOOL_LEVELS, weights=PROBABILITY_SCHOOL_LEVELS_WOMAN)[0]

    def studing_state(self):
        if self.DNA[STUDY] == 'Nenhum':
            self.is_studing = False
            return

        elif self.DNA[STUDY] == 'Ensino básico':
            if self.age >= 6 and self.age < 15:
                self.is_studing = True
                return
            else:
                self.is_studing = False
        elif self.DNA[STUDY] == 'Ensino secundário e pós secundário':
            if self.age >= 15 and self.age < 18:
                self.is_studing = True
                return
            else:
                self.is_studing = False
        elif self.DNA[STUDY] == 'Ensino superior':
            if self.age > 18 and self.age < 23:
                self.is_studing = True
                return
            else:
                self.is_studing = False
    def life_state(self):
        if self.age >= self.DNA[AGE_DEAD]:
            self.is_alive = False
            self.dead_cause = DEAD_CAUSE_NATURAL
        if self.years_without_basic_needs > 3:
            self.is_alive = False
            self.dead_cause = DEAD_CAUSE_CANT_PROVIDE_BASIC_NEEDS
        return
    def working_state(self):
        if self.is_studing == False and self.age > 14:
            self.is_working = True
        elif self.age < 67:
            self.is_working = False
    def get_salary(self):
        if self.is_studing == False and self.is_working == True:
            education = self.DNA[STUDY]
            salary = SALARY_BY_EDUCATION[education] * random_variation_salary()
            self.money += salary
            return
    def pay_for_living(self):
        #family_number = len(self.childs) + 1
        if self.is_working == True:
            amount = living_cost(family_number=1 + len(self.children)) * 12
            if self.is_married:
                amount = amount / 1.25
            if self.money < amount:
                self.years_without_basic_needs += 1
            else:
                self.years_without_basic_needs = 0
                self.money -= amount
            return
    def pay_health(self):
        if self.is_working:
            self.money -= COST_OF_UNIVERSAL_HEALTH_SYSTEM_PER_CAPITA



    def give_birth(self):
        if self.age in self.DNA[AGE_BORN_CHILD]:
            child = Person()
            self.children.append(child)
            if self.is_married:
                self.partner.children.append(child)
            return child
        return None



