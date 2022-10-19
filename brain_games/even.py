import random
from unicodedata import name
import prompt


def welcome_user():
    global name
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")


def is_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count_try = 0
    correct_answer = ''
    while count_try >= 0:
        random_number = random.randint(0, 99)

        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        print("Question: ", random_number)

        print("Your answer: ", end ='')
        answer = input()

        if (answer == "yes" and random_number % 2 == 0) or (answer == "no" and random_number % 2 != 0):
            print("Correct!")
            count_try += 1

        if answer != "yes" and answer != "no":
            print(f"'{answer}' is not wrong answer ;(. Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            break

        if (answer == "yes" and random_number % 2 != 0):
            print(f"'{answer}' is not wrong answer ;(. Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            break

        elif (answer == "no" and random_number % 2 == 0):
            print(f"'{answer}' is not wrong answer ;(. Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            break

        if count_try == 3:
            print(f"Congratulation, {name}!")
            break