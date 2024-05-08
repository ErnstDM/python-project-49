from random import randint
import math
RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return 'no'
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return 'no'
    return 'yes'


def get_question_and_right_answer():
    question = randint(1, 15)
    right_answer = is_prime(question)
    return question, right_answer
