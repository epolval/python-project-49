#!/usr/bin/env python3
from brain_games.const import PROGRESSION_INSTRUCTION
from brain_games.core import run_game
from brain_games.games.progression import run_progression


def main():
    run_game(PROGRESSION_INSTRUCTION, run_progression)


if __name__ == '__main__':
    main()
