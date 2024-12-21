#!/usr/bin/env python3
from brain_games.const import EVEN_INSTRUCTION
from brain_games.core import run_game
from brain_games.games.even import run_even


def main():
    run_game(EVEN_INSTRUCTION, run_even)


if __name__ == '__main__':
    main()
