import random

from brain_games.games.engine import engine

rule = 'What is the result of the expression?'


def generate_question_and_correct_answer():
    number1 = random.randint(1, 99)
    number2 = random.randint(1, 99)
    operator = random.choice(['+', '-', '*'])
    question = f'Question: {number1} {operator} {number2}'
    match operator:
        case '+':
            correct_answer = number1 + number2
        case '-':
            correct_answer = number1 - number2
        case '*':
            correct_answer = number1 * number2
    correct_answer = str(correct_answer)
    return question, correct_answer


def calc_game():
    engine(rule, generate_question_and_correct_answer)
