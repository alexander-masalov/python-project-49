import random


rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def question_generate():
    number = random.randint(2, 100)
    for item in range(2, number):
        if number % item == 0:
            return number, 'no'
    return number, 'yes'
