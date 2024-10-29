#!/usr/bin/env python3
from games_functions import dialog_with_user
from games_functions import is_wrong_for_even
from random import randint


def main():
    play_counter: int = 0
    dialog_with_user('welcome')
    name: str = dialog_with_user('hellow')
    dialog_with_user('rules_even')
    while play_counter < 3:
        number_for_ask: int = randint(0, 100)
        dialog_with_user('question', str(number_for_ask))
        answer: str = dialog_with_user('answer')
        if is_wrong_for_even(number_for_ask, answer, name):
            return
        play_counter += 1
        dialog_with_user('correct')
    dialog_with_user('greeting', name)
    return


if __name__ == '__main__':
    main()
