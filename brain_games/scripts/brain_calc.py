#!/usr/bin/env python3
from brain_games.const import CALC_INSTRUCTION
from brain_games.core import run_game
from brain_games.games.calc import run_calc


def main():
    run_game(CALC_INSTRUCTION, run_calc)


if __name__ == '__main__':
    main()
