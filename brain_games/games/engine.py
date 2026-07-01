import prompt

from brain_games.cli import welcome_user


def engine(rule, generate_question_and_correct_answer):
    name = welcome_user()
    print(rule)

    correct_answers_count = 0
    rounds_to_win = 3

    while correct_answers_count < rounds_to_win:
        question, correct_answer = generate_question_and_correct_answer()
        print(question)
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            correct_answers_count += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {name}!"
            )
            break
    else:
        print(f'Congratulations, {name}!')
