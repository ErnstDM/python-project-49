from random import randint
RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_right_answer():
    question = randint(1, 10)

    if is_even(question):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer


def is_even(question):
    return question % 2 == 0
