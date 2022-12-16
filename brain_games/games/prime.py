import random


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_LIMIT = 1
MAX_LIMIT = 100


def is_prime(x):
    if x == 1:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def question_generate():
    number = random.randint(MIN_LIMIT, MAX_LIMIT)
    if is_prime(number):
        return number, 'yes'
    else:
        return number, 'no'
