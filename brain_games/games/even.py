import random

from brain_games.games.engine import engine

rule = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_and_correct_answer():
    number = random.randint(1, 99)
    question = f'Question: {number}'
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return question, correct_answer


def even_game():
    engine(rule, generate_question_and_correct_answer)
