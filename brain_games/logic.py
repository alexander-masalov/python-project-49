import prompt


def play(game):
    COUNT = 3
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.rules)

    while COUNT > 0:
        question, correct_answer = game.question_generate()
        print('Question: ', end='')
        print(f'{question}')
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
        COUNT -= 1
        if COUNT == 0:
            print(f'Congratulations, {name}!')
