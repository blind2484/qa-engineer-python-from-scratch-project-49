import random

from brain_games.games.engine import engine

rule = 'Find the greatest common divisor of given numbers.'


def generate_question_and_correct_answer():
    NUMBER1 = random.randint(1, 99)
    NUMBER2 = random.randint(1, 99)
    question = f'Question: {NUMBER1} {NUMBER2}'
    while NUMBER2 != 0:
        tmp_number = NUMBER2
        NUMBER2 = NUMBER1 % NUMBER2
        NUMBER1 = tmp_number
    correct_answer = str(NUMBER1)
    return question, correct_answer


def gcd_game():
    engine(rule, generate_question_and_correct_answer)
