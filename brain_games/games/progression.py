import random


rules = 'What number is missing in the progression?'


def question_generate():
    start = random.randint(1, 20)
    stop = 100
    step = random.randint(1, 9)
    progression = []
    for item in range(start, stop, step):
        progression.append(str(item))
        if len(progression) > random.randint(5, 10):
            break
    random_index = random.randint(0, len(progression) - 1)
    correct_answer = progression[random_index]
    progression[random_index] = '..'
    question = ' '.join(progression)
    return question, correct_answer
