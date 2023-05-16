import random
import scipy.stats as stats
from scipy.stats import truncnorm
from scipy.stats import poisson, uniform

from .settings import PROBABILITY_SEX,  SEXS_TYPE
from .settings import PROBABILITY_INVEST
from .settings import PROBABILITY_SAVE
from .settings import PROBABILITY_AGE_DEAD, DEAD_AGES
from .settings import NUMBER_CHILDS, PROBABILITY_NUMBER_CHILDS
from .settings import PROBABILITY_CREDIT
from .settings import PROBABILITY_MARRIED
from .settings import LIVING_COST_PARAMETER_M, LIVING_COST_PARAMETER_B, RENT_T1_HOUSE_MEAN

from .constants import AGE_DEAD, AGE_BORN_CHILD, INVEST, SAVE_MONEY, CREDIT, SEX, MARRIAGE, STUDY


def gene(gene_type):
    if gene_type == SEX:
        return  random.choices(SEXS_TYPE, PROBABILITY_SEX)[0]
    elif gene_type == AGE_DEAD:
        return int(random.choices(DEAD_AGES, weights=PROBABILITY_AGE_DEAD)[0])
    elif gene_type == AGE_BORN_CHILD:
        number_of_children = random.choices(NUMBER_CHILDS, weights=PROBABILITY_NUMBER_CHILDS)[0]

        if number_of_children == 3:
            # sample number of children equal or greater than 3 from exponential distribution
            lower, upper, scale = 3, 16, 1/0.5
            X = stats.truncexpon(b=(upper-lower)/scale, loc=lower, scale=scale)
            number_of_children = X.rvs(1)

        number_of_children = int(number_of_children)

        sample_size = 1
        maxval = 49
        mu = 26.8 # mean age of first child in 2001
        age_first_child = 0
        while age_first_child < 15 or age_first_child > 49:
            age_first_child = random.gauss(mu, sigma=10)

        lower, upper, scale = age_first_child, 49, 1/.25
        X = stats.truncexpon(b=(upper-lower)/scale, loc=lower, scale=scale)
        list_aux = sorted( [int(i) for i in X.rvs(1000)])
        try:
            ages_born_child = sorted(random.sample(list(set(list_aux)), number_of_children))
        except ValueError:
            ages_born_child = list(set(list_aux))
        return ages_born_child
    elif gene_type == INVEST:
        return random.choices([True, False], weights=PROBABILITY_INVEST)[0]
    elif gene_type == SAVE_MONEY:
        return random.choices([True, False], weights=PROBABILITY_SAVE)[0]
    elif gene_type == CREDIT:
        return random.choices([True, False], weights=PROBABILITY_CREDIT)[0]
    elif gene_type == MARRIAGE:
        return random.choices([True, False], weights=PROBABILITY_MARRIED)[0]


def living_cost(family_number):
    return LIVING_COST_PARAMETER_M*family_number + \
           LIVING_COST_PARAMETER_B + RENT_T1_HOUSE_MEAN

def random_variation_salary():
    a = 0.9
    b = 5
    return truncnorm.rvs(a, b, size=1)[0]




