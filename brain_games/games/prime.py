import random

from brain_games.games.engine import engine

rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_number_prime():
    NUMBER = random.randint(1, 99)
    if NUMBER < 2:
        return NUMBER, 'no'
    for divider in range(2, NUMBER // 2 + 1):
        if NUMBER % divider == 0:
            return NUMBER, 'no'
    return NUMBER, 'yes'
        

def generate_question_and_correct_answer():
    NUMBER, prime = is_number_prime()
    question = f'Question: {NUMBER}'
    correct_answer = prime
    return question, correct_answer


def prime_game():
    engine(rule, generate_question_and_correct_answer)
