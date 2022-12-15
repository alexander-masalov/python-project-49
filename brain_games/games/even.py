import random


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_LIMIT = 1
MAX_LIMIT = 100


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


def question_generate():
    number = random.randint(MIN_LIMIT, MAX_LIMIT)
    if is_even(number):
        return number, 'yes'
    else:
        return number, 'no'
