from brain_games.utils import get_random


def run_prime():
    result = ''

    number = get_random(0, 100)
    ask_string = str(number)

    for divider in range(2, number // 2):
        result = 'yes'
        if number % divider == 0:
            result = 'no'
            break
    if number <= 1:
        result = 'no'
    if number == 2 or number == 3:
        result = 'yes'
    correct_answer = result

    return ask_string, correct_answer
