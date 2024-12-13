from const import PRIME_INSTRUCTION
from core import run_game
from utils import get_random


def run_prime():
    ask_string = []
    correct_answer = []

    for i in range(3):
        number = get_random(0, 100)
        ask_string.append(str(number))

        for divider in range(2, number // 2):
            result = 'yes'
            if number % divider == 0:
                result = 'no'
                break

        correct_answer.append(result)

    run_game(ask_string, correct_answer, PRIME_INSTRUCTION)
