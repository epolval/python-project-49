#!/usr/bin/env python3
from games_lib.games_functions import dialog_with_user
from games_lib.games_functions import is_wrong_for_gcd
from random import randint


def main():
    play_counter = 0
    dialog_with_user('welcome')
    name = dialog_with_user('hellow')
    dialog_with_user('rules')
    while play_counter < 3:
        num1_for_ask = randint(0, 100)
        num2_for_ask = randint(0, 100)
        string_for_ask = f'{num1_for_ask } {num2_for_ask}'
        dialog_with_user('question', string_for_ask)
        answer = dialog_with_user('answer')
        if is_wrong_for_gcd((num1_for_ask, num2_for_ask), answer, name):
            return
        play_counter += 1
        dialog_with_user('correct')
    dialog_with_user('greeting', name)
    return


if __name__ == '__main__':
    main()
