from brain_games.utils import (
    ask_name_dialog,
    correct_dialog,
    finish_dialog,
    greeting_dialog,
    instruction_dialog,
    question_dialog,
)


def run_game(ask_string, correct_answer, instruction_string):
    name = ask_name_dialog()
    instruction_dialog(instruction_string)
    for i in range(3):
        user_answer = question_dialog(ask_string[i])
        if not check_answer(user_answer, correct_answer[i], name):
            return

    greeting_dialog(name)


def check_answer(user_answer, correct_answer, name):
    if user_answer != correct_answer:
        finish_dialog(name, user_answer, correct_answer)
        return False
    else:
        correct_dialog()
        return True
