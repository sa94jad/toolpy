"""Pypax94s: a small Python utility library by Sajjad."""

import random

__version__ = "0.4.0"
__author__ = "Sajjad"


def prt(name):
    """Print the value passed to the function."""
    print(name)


def game_random():
    """Play a number-guessing game using a random number from 1 to 10."""
    try:
        answer = int(input("عددتان از ۱ تا ۱۰: "))
    except ValueError:
        print("لطفاً یک عدد صحیح وارد کنید.")
        return

    if not 1 <= answer <= 10:
        print("فقط از بین ۱ تا ۱۰ انتخاب کنید!")
        return

    number = random.randint(1, 10)
    if answer == number:
        print("درسته")
    else:
        print("غلطه")
        print(number)


def random_randiout():
    """Print a random float from 0.0 up to (but not including) 1.0."""
    print(random.random())


def random_game_sqw():
    """Play rock-paper-scissors against the computer."""
    choices = ["سنگ", "کاغذ", "قیچی"]
    player = input("سنگ / کاغذ / قیچی: ").strip()

    if player not in choices:
        print("لطفا فقط از بین سنگ، کاغذ و قیچی استفاده کنید!")
        return

    computer = random.choice(choices)
    print(computer)

    if player == computer:
        print("مساوی")
    elif (
        (player == "سنگ" and computer == "قیچی")
        or (player == "کاغذ" and computer == "سنگ")
        or (player == "قیچی" and computer == "کاغذ")
    ):
        print("بردی")
    else:
        print("باختی")


def pay():
    """Print pi to 8 decimal places."""
    print(3.14159265)

def run():
	while True:
		continue
def break_code():
	while True:
		break

# Compatibility aliases for names used in earlier releases.
game_randomac = game_random
randomat_randiout = random_randiout
