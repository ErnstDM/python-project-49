from random import randint
RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_right_answer():
    question = randint(1, 10)
    right_answer = is_even(question)
    return question, right_answer


def is_even(question):
    return 'yes' if question % 2 == 0 else 'no'
