import random

from brain_games.games.engine import engine

rule = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_and_correct_answer():
    NUMBER = random.randint(1, 99)
    question = f'Question: {NUMBER}'
    correct_answer = 'yes' if NUMBER % 2 == 0 else 'no'
    return question, correct_answer


def even_game():
    engine(rule, generate_question_and_correct_answer)
