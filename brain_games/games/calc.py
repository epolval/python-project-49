from brain_games.utils import get_random


def run_calc():
    operators = ('+', '-', '*')

    num1 = str(get_random(0, 100))
    num2 = str(get_random(0, 100))
    oper_idx = get_random(0, 2)
    result = f'{num1} {operators[oper_idx]} {num2}'
    ask_string = result
    correct_answer = str(eval(result))

    return ask_string, correct_answer
