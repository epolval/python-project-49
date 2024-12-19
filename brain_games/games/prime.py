from brain_games.const import PRIME_INSTRUCTION
from brain_games.core import run_game
from brain_games.utils import get_random


def run_prime():
    ask_string = []
    correct_answer = []
    result = ''

    for i in range(3):
        number = get_random(0, 100)
        ask_string.append(str(number))

        for divider in range(2, number // 2):
            result = 'yes'
            if number % divider == 0:
                result = 'no'
                break
        if number <= 1:
            result = 'no'
        if number == 2 or number == 3:
            result ='yes'
        correct_answer.append(result)

    run_game(ask_string, correct_answer, PRIME_INSTRUCTION)
