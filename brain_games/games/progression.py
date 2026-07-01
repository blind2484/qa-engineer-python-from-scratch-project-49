import random

from brain_games.games.engine import engine

rule = 'What number is missing in the progression?'


def generate_progression():
    progression_start = random.randint(1, 25)
    progression_step = random.randint(1, 10)
    progression = [
        progression_start + index * progression_step
        for index in range(10)
    ]
    return progression


def generate_question_and_correct_answer():
    progression = generate_progression()
    hidden_element_index = random.randint(0, 9)
    correct_answer = str(progression[hidden_element_index])
    progression[hidden_element_index] = '..'
    progression = " ".join(str(element) for element in progression)
    question = f'Question: {progression}'
    return question, correct_answer


def progression_game():
    engine(rule, generate_question_and_correct_answer)
