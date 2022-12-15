import random


RULES = "What is the result of the expression?"
MIN_LIMIT = 1
MAX_LIMIT = 100


def question_generate():
    operations = ['+', '-', '*']
    operation = random.choice(operations)
    number_1 = random.randint(MIN_LIMIT, MAX_LIMIT)
    number_2 = random.randint(MIN_LIMIT, MAX_LIMIT)
    if operation == '+':
        return f'{number_1} + {number_2}', number_1 + number_2
    elif operation == '-':
        return f'{number_1} - {number_2}', number_1 - number_2
    elif operation == '*':
        return f'{number_1} * {number_2}', number_1 * number_2
