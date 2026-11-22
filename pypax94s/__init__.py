"""Pypax94s: a tiny Python utility module by Sajjad."""

import random
import time

__version__ = "0.2.0"
__author__ = "Sajjad"


def prt(name):
    """Print the given value."""
    print(name)


def game_random():
    """Play a number-guessing game using a number from 1 to 10."""
    try:
        answer = int(input("عددتان از ۱ تا ۱۰: "))
    except ValueError:
        print("لطفاً یک عدد صحیح وارد کنید.")
        return

    if not 1 <= answer <= 10:
        print("فقط عددهای ۱ تا ۱۰ مجاز هستند.")
        return

    number = random.randint(1, 10)
    if answer == number:
        print("درسته!")
    else:
        print("غلطه!")
        print("عدد درست:", number)


def random_randiout():
    """Return a random float in the range [0.0, 1.0)."""
    return random.random()


def random_game_sqw():
    """Play rock-paper-scissors against the computer."""
    choices = ["سنگ", "کاغذ", "قیچی"]
    player = input("سنگ / کاغذ / قیچی: ").strip()

    if player not in choices:
        print("لطفاً فقط از بین سنگ، کاغذ و قیچی انتخاب کنید!")
        return

    computer = random.choice(choices)
    print("انتخاب کامپیوتر:", computer)

    if player == computer:
        print("مساوی!")
    elif (
        (player == "سنگ" and computer == "قیچی")
        or (player == "کاغذ" and computer == "سنگ")
        or (player == "قیچی" and computer == "کاغذ")
    ):
        print("بردی!")
    else:
        print("باختی!")


def pay():
    """Print the value of pi to eight decimal places."""
    print(3.14159265)
