import prompt


COUNT_TRY = 3


def play(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES)

    for i in range(0, COUNT_TRY):
        question, correct_answer = game.question_generate()
        print('Question: ', end='')
        print(f'{question}')
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            exit()

    print(f'Congratulations, {name}!')
