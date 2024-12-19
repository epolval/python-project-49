from brain_games.const import PROGRESSION_INSTRUCTION
from brain_games.core import run_game
from brain_games.utils import get_random


def run_progression():
    ask_string = []
    correct_answer = []

    for i in range(3):
        start_num = get_random(0, 100)
        step = get_random(1, 10)
        length = get_random(5, 15)
        gap_position = get_random(1, length)
        list_for_ask = []
        gap_value = 0

        for n in range(1, length + 1):
            if n == gap_position:
                list_for_ask.append('..')
                gap_value = start_num + (n - 1) * step
            else:
                list_for_ask.append(str(start_num + (n - 1) * step))
        ask_string.append(' '.join(list_for_ask))
        correct_answer.append(str(gap_value))

    run_game(ask_string, correct_answer, PROGRESSION_INSTRUCTION)
