import random


rules = "What is the result of the expression?"


def question_generate():
    operations = ['+', '-', '*']
    operation = random.choice(operations)
    number_1 = random.randint(1, 99)
    number_2 = random.randint(1, 99)
    if operation == '+':
        return f'{number_1} + {number_2}', number_1 + number_2
    elif operation == '-':
        return f'{number_1} - {number_2}', number_1 - number_2
    elif operation == '*':
        return f'{number_1} * {number_2}', number_1 * number_2
