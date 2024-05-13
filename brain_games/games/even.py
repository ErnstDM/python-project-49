from random import randint
RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_right_answer():
    question = randint(1, 10)
    return question, 'yes' if is_even(question) else 'no'


def is_even(question):
    return question % 2 == 0
