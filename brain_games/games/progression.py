import random

from brain_games.games.engine import engine

rule = 'What number is missing in the progression?'


def generate_progression():
    PROGRESSION_START = random.randint(1, 25)
    PROGRESSION_STEP = random.randint(1, 10)
    PROGRESSION = [
        PROGRESSION_START + index * PROGRESSION_STEP
        for index in range(10)
    ]
    return PROGRESSION


def generate_question_and_correct_answer():
    PROGRESSION = generate_progression()
    hidden_element_index = random.randint(0, 9)
    correct_answer = str(PROGRESSION[hidden_element_index])
    PROGRESSION[hidden_element_index] = '..'
    PROGRESSION = " ".join(str(element) for element in PROGRESSION)
    question = f'Question: {PROGRESSION}'
    return question, correct_answer


def progression_game():
    engine(rule, generate_question_and_correct_answer)
