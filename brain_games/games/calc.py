from brain_games.const import CALC_INSTRUCTION
from brain_games.core import run_game
from brain_games.utils import get_random


def run_calc():
    operators = ('+', '-', '*')
    ask_string = []
    correct_answer = []
    for i in range(3):
        num1 = str(get_random(0, 100))
        num2 = str(get_random(0, 100))
        oper_idx = get_random(0, 2)
        result = f'{num1} {operators[oper_idx]} {num2}'
        ask_string.append(result)
        correct_answer.append(str(eval(result)))

    run_game(ask_string, correct_answer, CALC_INSTRUCTION)
