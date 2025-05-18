#!/bin/python3
# MasterMind
# by Roc. N (https://github.com/ictrocn/master_Mind/tree/main)
# Forked by:
#  A-A-Tel (https://github.com/a-a-tel)
#  Luuk Müskens (https://github.com/luukmuskens/)
# v1.01
# 15-8-2024
# Last mod by DevJan : added loop for replay
print("MasterMind")

import random


def generate_code(length=4, digits=6):
    return [str(random.randint(1, digits)) for _ in range(length)]


def get_feedback(secret, guess):
    black_pegs = sum(s == g for s, g in zip(secret, guess))

    # Count whites by subtracting black and calculating min digit frequency match
    secret_counts = {}
    guess_counts = {}

    for s, g in zip(secret, guess):
        if s != g:
            secret_counts[s] = secret_counts.get(s, 0) + 1
            guess_counts[g] = guess_counts.get(g, 0) + 1

    white_pegs = sum(min(secret_counts.get(d, 0), guess_counts.get(d, 0)) for d in guess_counts)

    return black_pegs, white_pegs


def show_secret(mystery):
    print(mystery)


def play_mastermind():
    print("Welcome to Mastermind!")
    print("Guess the 4-digit code. Each digit is from 1 to 6. You have 10 attempts.")
    secret_code = generate_code()
    attempts = 10

    for attempt in range(1, attempts + 1):
        guess = ""
        valid_guess = False
        while not valid_guess:
            guess = input(f"Attempt {attempt}: ").strip()
            valid_guess = len(guess) == 4 and all(c in "123456" for c in guess)
            if not valid_guess:
                print("Invalid input. Enter 4 digits, each from 1 to 6.")
            show_secret(secret_code) if guess == "cheat" else False

        black, white = get_feedback(secret_code, guess)
        print(f"Black pegs (correct position): {black}, White pegs (wrong position): {white}")

        if black == 4:
            print(f"Congratulations! You guessed the code: {''.join(secret_code)}")
            return

    print(f"Sorry, you've used all attempts. The correct code was: {''.join(secret_code)}")


if __name__ == "__main__":
    again = 'Y'
    while again == 'Y':
        play_mastermind()
        again = input(f"Play again (Y/N) ?").upper()
