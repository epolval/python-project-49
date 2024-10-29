#!/usr/bin/env python3
from games_functions import dialog_with_user
from games_functions import is_wrong_for_calc
from random import randint
from random import choices


def main():
    play_counter: int = 0
    dialog_with_user('welcome')
    name: str = dialog_with_user('hellow')
    dialog_with_user('rules_calc')
    while play_counter < 3:
        num1_for_ask: str = str(randint(0, 100))
        num2_for_ask: str = str(randint(0, 100))
        sign_for_ask: list[str] = choices('+-*')
        string_for_ask = f'{num1_for_ask } {sign_for_ask[0]} {num2_for_ask}'
        dialog_with_user('question', string_for_ask)
        answer: str = dialog_with_user('answer')
        if is_wrong_for_calc(eval(string_for_ask), answer, name):
            return
        play_counter += 1
        dialog_with_user('correct')
    dialog_with_user('greeting', name)
    return


if __name__ == '__main__':
    main()
