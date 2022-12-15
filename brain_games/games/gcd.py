import random
import math


RULES = 'Find the greatest common divisor of given numbers.'
MIN_LIMIT = 1
MAX_LIMIT = 100


def question_generate():
    number_1 = random.randint(MIN_LIMIT, MAX_LIMIT)
    number_2 = random.randint(MIN_LIMIT, MAX_LIMIT)
    return f'{number_1} {number_2}', math.gcd(number_1, number_2)
