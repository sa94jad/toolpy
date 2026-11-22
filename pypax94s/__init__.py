"""Pypax94s: a small Python utility library by Sajjad."""

import random

__version__ = "1.3.1"
__author__ = "Saj94ad"


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
from colorama import init , Fore , Style
def select_color():
	choose_color = input("RED , GREEN , WHITE , CYAN , BLUE:  ")
	wordds = input("کلمه یا جمله ای که میخواهید رنگی شود.")
	if choose_color == "RED":
		print(Fore.RED + wordds)
	
	elif choose_color == "BLUE":
		print(Fore.BLUE + wordds)
	
	elif choose_color == "CYAN":
		print(Fore.CYAN + wordds)
	
	elif choose_color == "GREEN":
		print(Fore.GREEN + wordds)
	
	elif choose_color == "WHITE":
		print(Rore.WHITE + wordds)
	
	else:
		print("رنگ پشتیبان نمی شود!")
def len_word():
	word_len = input("کلمه:  ")
	print(len(word_len))
def calculator():
	try:
	#سه متغیر
		o = int(input("عدد اول:   "))
		n = input("علامت:  ")
		s = int(input("عدد آخر:   "))
		if n == "+":
			print(o + s)
	
		elif n == "×":
			print(o * s)
	
		elif n == "-":
			print(o - s)
	
		elif n == "÷":
			print(o // s)
	
		elif n == "/":
			print(o / s)
	
		else:
			print("علامت یا در ماشین حساب نیست یا عدد نامعتبر است!")
	except:
		print("لطفا عدد وارد کنید")
def amk():
	try:
		num= int(input("عددتان:  "))
	
		if num % 2 == 0:
			print("زوج")
	
		else:
			print("فرد")
	

		
	except:
		print("عدد وارد کنید!")
amk()
# Compatibility aliases for names used in earlier releases.
game_randomac = game_random
randomat_randiout = random_randiout
