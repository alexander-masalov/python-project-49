import random


rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def question_generate():
    number = random.randint(1, 99)
    if number % 2 == 0:
        return number, 'yes'
    elif number % 2 != 0:
        return number, 'no'
