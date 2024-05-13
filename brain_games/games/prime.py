from random import randint
import math
RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def get_question_and_right_answer():
    question = randint(1, 15)
    return question, 'yes' if is_prime(question) else 'no'
