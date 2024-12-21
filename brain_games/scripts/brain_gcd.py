#!/usr/bin/env python3
from brain_games.const import GCD_INSTRUCTION
from brain_games.core import run_game
from brain_games.games.gcd import run_gcd


def main():
    run_game(GCD_INSTRUCTION, run_gcd)


if __name__ == '__main__':
    main()
