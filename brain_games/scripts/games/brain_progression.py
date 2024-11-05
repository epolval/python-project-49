#!/usr/bin/env python3
from brain_games.games_functions import dialog_with_user
from brain_games.games_functions import is_wrong_for_progression
from random import randint


def main():
    play_counter: int = 0
    dialog_with_user('welcome')
    name: str = dialog_with_user('hellow')
    dialog_with_user('rules_progressions')
    while play_counter < 3:
        start_of_prog: int = randint(0, 100)
        step_of_prog: int = randint(1, 10)
        len_of_prog: int = randint(5, 15)
        gap_pos: int = randint(1, len_of_prog)
        gap_value: str = ''
        list_for_ask: list[str] = []
        for n in range(1, len_of_prog + 1):
            if n == gap_pos:
                list_for_ask.append('..')
                gap_value = str(start_of_prog + (n - 1) * step_of_prog)
            else:
                list_for_ask.append(str(start_of_prog + (n - 1) * step_of_prog))
        string_for_ask: str = ' '.join(list_for_ask)
        dialog_with_user('question', string_for_ask)
        answer = dialog_with_user('answer')
        if is_wrong_for_progression(gap_value, answer, name):
            return
        play_counter += 1
        dialog_with_user('correct')
    dialog_with_user('greeting', name)
    return


if __name__ == '__main__':
    main()
