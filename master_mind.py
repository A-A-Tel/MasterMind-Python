#!/bin/python3
# MasterMind
# by Roc. N (https://github.com/ictrocn/master_Mind/tree/main)
# Forked by:
#  A-A-Tel (https://github.com/a-a-tel)
#  Luuk Müskens (https://github.com/luukmuskens/)
# v1.01
# 15-8-2024
# Last mod by DevJan : added loop for replay

import random
from os import getenv

VALID_CHARACTERS = "123456RGBYOP"
CODE_LENGTH = 4


def generate_code():
    code = ""
    for _ in range(CODE_LENGTH):
        code += random.choice(VALID_CHARACTERS)

    return code


def get_feedback(secret_code, guess):
    black_pegs = sum(s == g for s, g in zip(secret_code, guess))

    # Count whites by subtracting black and calculating min digit frequency match
    secret_counts = {}
    guess_counts = {}

    for s, g in zip(secret_code, guess):
        if s != g:
            secret_counts[s] = secret_counts.get(s, 0) + 1
            guess_counts[g] = guess_counts.get(g, 0) + 1

    white_pegs = sum(min(secret_counts.get(d, 0), guess_counts.get(d, 0)) for d in guess_counts)

    return black_pegs, white_pegs


def play_mastermind():
    print("Welcome to Mastermind!")
    print("Guess the code! Valid characters: " + VALID_CHARACTERS + ", Code length: " + str(CODE_LENGTH))

    secret_code = generate_code()
    max_attempts = 10

    for attempt in range(1, max_attempts + 1):
        while True:
            guess = input(f"Attempt {attempt}: ").upper().strip()

            if guess.lower() == getenv("DEBUG_PASS"):
                print(secret_code)
                continue

            if len(guess) == CODE_LENGTH and all(c in VALID_CHARACTERS for c in guess):
                break

            print("Invalid input. Valid characters: " + VALID_CHARACTERS + ", Code length: " + str(CODE_LENGTH))

        black, white = get_feedback(secret_code, guess)
        print(f"Black pegs (correct position): {black}, White pegs (wrong position): {white}")

        if black == 4:
            print(f"Congratulations! You guessed the code: {''.join(secret_code)}")
            return

    print(f"Sorry, you've used all attempts. The correct code was: {''.join(secret_code)}")


if __name__ == "__main__":
    play_again = 'Y'
    print("MasterMind")
    while play_again == 'Y':
        play_mastermind()
        play_again = input("Play again (Y/N)? ").strip().upper()
