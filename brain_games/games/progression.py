import random


RULES = 'What number is missing in the progression?'
MIN_START = 1
MAX_START = 20
STOP = 100
MIN_STEP = 1
MAX_STEP = 9
MIN_LEN = 5
MAX_LEN = 10


def question_generate():
    start = random.randint(MIN_START, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)
    len_progression = random.randint(MIN_LEN, MAX_LEN)
    progression = []
    for item in range(start, STOP, step):
        progression.append(str(item))
        if len(progression) > len_progression:
            break
    random_index = random.randint(0, len(progression) - 1)
    correct_answer = progression[random_index]
    progression[random_index] = '..'
    question = ' '.join(progression)
    return question, correct_answer
