import random
import math


rules = 'Find the greatest common divisor of given numbers.'


def question_generate():
    number_1 = random.randint(1, 99)
    number_2 = random.randint(1, 99)
    return f'{number_1} {number_2}', math.gcd(number_1, number_2)
