from const import EVEN_INSTRUCTION
from core import run_game
from utils import get_random


def run_even():
    ask_string = []
    correct_answer = []
    for i in range(3):
        number_for_check = get_random(0, 100)
        ask_string.append(str(number_for_check))
        result = 'yes' if number_for_check % 2 == 0 else 'no'
        correct_answer.append(result)

    run_game(ask_string, correct_answer, EVEN_INSTRUCTION)
