#!/usr/bin/env python3
from brain_games.const import PRIME_INSTRUCTION
from brain_games.core import run_game
from brain_games.games.prime import run_prime


def main():
    run_game(PRIME_INSTRUCTION, run_prime)


if __name__ == '__main__':
    main()
