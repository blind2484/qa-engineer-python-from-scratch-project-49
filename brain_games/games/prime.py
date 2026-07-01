import random

from brain_games.games.engine import engine

rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_number_prime():
    number = random.randint(1, 99)
    if number < 2:
        return number, 'no'
    for divider in range(2, number // 2 + 1):
        if number % divider == 0:
            return number, 'no'
    return number, 'yes'
        

def generate_question_and_correct_answer():
    number, prime = is_number_prime()
    question = f'Question: {number}'
    correct_answer = prime
    return question, correct_answer


def prime_game():
    engine(rule, generate_question_and_correct_answer)
