from const import GCD_INSTRUCTION
from core import run_game
from utils import get_random


def run_gcd():
    ask_string = []
    correct_answer = []

    for i in range(3):
        num1 = get_random(0, 100)
        num2 = get_random(0, 100)
        ask_string.append(f'{str(num1)} {str(num2)}')
        numbers = [num1, num2]
        numbers.sort()
        if numbers[0] == 0:
            gcd = numbers[1]
        for gcd in list(range(numbers[0], 0, -1)):
            if numbers[0] % gcd == 0 and numbers[1] % gcd == 0:
                break
        correct_answer.append(str(gcd))

    run_game(ask_string, correct_answer, GCD_INSTRUCTION)
