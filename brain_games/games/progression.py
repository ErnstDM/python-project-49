from random import randint
RULE = 'What number is missing in the progression?'


def get_question_and_right_answer():
    stop = randint(50, 100)
    step = randint(1, 5)
    result = list(range(randint(0, 9), stop, step))[: 5]
    random_index = randint(0, len(result) - 1)
    right_answer = result[random_index]
    result[random_index] = '..'
    question = " ".join(map(str, (result)))
    return question, str(right_answer)
