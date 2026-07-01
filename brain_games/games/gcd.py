import random

from brain_games.games.engine import engine

rule = 'Find the greatest common divisor of given numbers.'


def generate_question_and_correct_answer():
    number1 = random.randint(1, 99)
    number2 = random.randint(1, 99)
    question = f'Question: {number1} {number2}'
    while number2 != 0:
        tmp_number = number2
        number2 = number1 % number2
        number1 = tmp_number
    correct_answer = str(number1)
    return question, correct_answer


def gcd_game():
    engine(rule, generate_question_and_correct_answer)
