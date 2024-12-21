from random import randint
import prompt


def ask_name_dialog():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def instruction_dialog(instruction_string):
    print(instruction_string)


def question_dialog(ask_string):
    print(f'Question: {ask_string}')
    answer = prompt.string('Your answer: ')
    return answer


def correct_dialog():
    print('Correct!')


def finish_dialog(name, user_answer, correct_answer):
    print(f"'{user_answer}' is wrong answer ;"
          f"(. Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {name}!")


def greeting_dialog(name):
    print(f'Congratulations, {name}!')


def get_random(start_value=0, finish_value=100):
    return randint(start_value, finish_value)
