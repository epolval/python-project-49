from brain_games.utils import (
    ask_name_dialog,
    correct_dialog,
    finish_dialog,
    greeting_dialog,
    instruction_dialog,
    question_dialog,
)


def run_game(instruction_string, run_func):
    name = ask_name_dialog()
    instruction_dialog(instruction_string)
    for i in range(3):
        ask_string, correct_answer = run_func()
        user_answer = question_dialog(ask_string)
        if user_answer != correct_answer:
            finish_dialog(name, user_answer, correct_answer)
            return
        correct_dialog()
    greeting_dialog(name)
    return




