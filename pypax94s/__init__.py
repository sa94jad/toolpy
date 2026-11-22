"""Pypax94s: a small Python utility library by Sajjad."""

import random

__version__ = "0.2.0"
__author__ = "Sajjad"


def prt(name):
    """Print the value passed to the function."""
    print(name)


def game_random():
    """Guess a random integer from 1 to 10."""
    try:
        answer = int(input("عددتان از ۱ تا ۱۰: "))
    except ValueError:
        print("لطفاً یک عدد صحیح وارد کنید.")
        return

    if not 1 <= answer <= 10:
        print("فقط عددهای ۱ تا ۱۰ مجاز هستند!")
        return

    number = random.randint(1, 10)
    if answer == number:
        print("درسته!")
    else:
        print("غلطه!")
        print("عدد درست:", number)


def random_randiout():
    """Print a random floating-point number from 0.0 up to (but not including) 1.0."""
    print(random.random())


def random_game_sqw():
    """Play rock-paper-scissors against the computer."""
    choices = ["سنگ", "کاغذ", "قیچی"]
    player = input("سنگ / کاغذ / قیچی: ").strip()

    if player not in choices:
        print("لطفاً فقط از بین سنگ، کاغذ و قیچی استفاده کنید!")
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
    """Print pi."""
    print(3.14159265)
