"""
projekt_2.py: Druhý projekt do Engeto Online Python Akademie

author = Petr Kulig
email: petrkg@centrum.cz
discord: Petr Kulig#4490
"""

import random

def generate_number():
    digits = list(range(1, 10))
    random.shuffle(digits)
    number = ''.join(map(str, digits[:4]))
    return number

def number_guess(guess, number):
    bulls = 0
    cows = 0
    for i, digit in enumerate(guess):
        if digit == number[i]:
            bulls += 1
        elif digit in number:
            cows += 1
    return bulls, cows

def is_valid_guess(guess):
    if len(guess) != 4:
        print("Your tip has to have only 4 digits.")
        return False
    if len(set(guess)) != 4:
        print("All digits have to be unique.")
        return False
    if not guess.isdigit():
        print("Your tip have to have  only digits.")
        return False
    if guess[0] == '0':
        print("Please, don´t let number '0'  at the beginning.")
        return False
    return True

def play_game():
    print("Hello in game Bulls and Cows!")
    number = generate_number()
    while True:
        guess = input("Please, put your 4 digits without '0' at the beginning: ")
        if not is_valid_guess(guess):
            continue
        bulls, cows = number_guess(guess, number)
        print(f"You have  {bulls} bull{'s' if bulls != 1 else ''} and {cows} cow{'s' if cows != 1 else ''}.")
        if bulls == 4:
            print("Congratulation! You guess right  number!")
            break

play_game()
