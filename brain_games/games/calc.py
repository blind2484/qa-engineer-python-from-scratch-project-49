import random

from brain_games.games.engine import engine

rule = 'What is the result of the expression?'


def generate_question_and_correct_answer():
    NUMBER1 = random.randint(1, 99)
    NUMBER2 = random.randint(1, 99)
    OPERATOR = random.choice(['+', '-', '*'])
    question = f'Question: {NUMBER1} {OPERATOR} {NUMBER2}'
    match OPERATOR:
        case '+':
            correct_answer = NUMBER1 + NUMBER2
        case '-':
            correct_answer = NUMBER1 - NUMBER2
        case '*':
            correct_answer = NUMBER1 * NUMBER2
    correct_answer = str(correct_answer)
    return question, correct_answer


def calc_game():
    engine(rule, generate_question_and_correct_answer)
