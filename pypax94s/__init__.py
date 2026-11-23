"""Pypax94s: a small Python utility library by Sajjad."""

import random
import secrets
import datetime
import math
from ping3 import ping
__version__ = "2.1.1"
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


def pi():
    """Print pi to 8 decimal places."""
    print(3.14159265)


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

def make_password():
	t = secrets.randbelow(999999)
	print(t)

def readfile():
	try:
		read = input("نام فایلتان:  ")
		with open(read , "r") as f:
			text = f.read()
			print(text)
	except:
		print("فایل یافت نشد!")


def time_H_new():
	print(datetime.datetime.now().hour)
time_H_new()

def data_library():
	print("سلام به کتاب خونه pypax خوش اومیدید.")
	print("نسخه: 2.1.1")
	print("اطلاعات کتاب خانه:")
	print("prt("")" , "برای چاپ متن: ")
	print("game_random()" , "بازی حدس عدد")
	print("random_randiout()" , "عدد رندوم بین 0 . 1")
	print("random_game_sqw()" , "بازی سنگ کاغذ غیچی")
	print("pi()" , "نمایش عدد پی")
	print("run()" , "حلقه ای بی اتمام ایجاد میکند")
	print("break_code()" , "به کد پایان میدهد")
	print("len_word()" , "میتوانید بعد اجرای این تابع کلمه ای توی ترمینال بزنید و تعداد حروف هایش را بگیرید")
	print("calculator()", "در ترمینال به شما ماشین حساب آماده ای میدهد")
	print("amk" , "بعد اجرا عددتان را میتوانید داخل ترمینال وارد کنید و سیستم زوج یا فرد بودن را به شما بدهد.")
	print("make_password()" , "داخل ترمینال رمز ۶ رقمی میسازد.")
	print("time_H_new()" , "ساعت را چاپ میکند.")
	print("readfile()" , "در ترمینال به شما اجازه وارد کردن نام فایل میدهد که اگر فایل باشد متن های داخل فایل را میدهد به شما.")
	print("توجه داشته باشید. در پرانتز دستور ها چیزی وارد نکنید!")
	print("اما تنها در دستور prt() میتوانید داخل پرانتز چیزی وارد کنید برای چاپ")
	print("my_ping()" , "این دستور پینگ شما را نشان میدهد")
	print("sqrt_rand() " , "این تابع میتواند از شما در ترمینال عدد مورد نظر برای رادیکال کردن بگیرد و نتیجه را بدهد!")
def my_ping():
	t = ping("8.8.8.8")
	print(f"Your ping:  {round(t * 1000)} ms" if t else "درخواست نیومد")

def sqrt_rand():
	try:
		sqrt = int(input("عدد مورد نظر برای دریافت رادیکال:   "))
		print(math.sqrt(sqrt))
	except:
		print("لطفا عدد وارد کنید! ")
# Compatibility aliases for names used in 