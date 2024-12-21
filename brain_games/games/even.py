from brain_games.utils import get_random


def run_even():
    number_for_check = get_random(0, 100)
    ask_string = str(number_for_check)
    result = 'yes' if number_for_check % 2 == 0 else 'no'
    correct_answer = result

    return ask_string, correct_answer
