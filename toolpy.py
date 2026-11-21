"""ToolPy 0.4
Beginner-friendly Python utility functions.
Created by Sajjad (@saj94jad).
"""

import random
import secrets
import string
import time as _time


def print_Ln():
    text = input("Enter your print: ")
    answer = input("Do you want to see your println? (yes/no): ").strip().lower()

    if answer == "yes":
        print(text)
    elif answer == "no":
        print("ok!")
    else:
        print("Unknown!")


def pay():
    print(3.14)


def time_sleep():
    seconds = int(input("زمان تایم چقدر باشه: "))
    if seconds < 0:
        print("زمان نمی‌تواند منفی باشد.")
        return
    _time.sleep(seconds)


def time_year():
    print(_time.strftime("%Y"))


def wait_time_loop():
    seconds = int(input("زمان ماندگاری (ثانیه): "))
    if seconds < 0:
        print("زمان نمی‌تواند منفی باشد.")
        return
    _time.sleep(seconds)


def len_word():
    word = input("اسم: ")
    print(len(word))


def random_number():
    print(random.randint(1, 9_999_999_999_999))


def println():
    text = input("نام: ")
    print(text)


def local_time():
    print(_time.strftime("%m/%d-%H-%M-%S"))


def for_in():
    count = int(input("یک عدد انتخاب کنید: "))
    if count < 0:
        print("عدد نمی‌تواند منفی باشد.")
        return
    for number in range(count):
        print(number)


def random_randert():
    print(random.random())


def AI():
    print(
        "هوش مصنوعی سیستمی است که برای پردازش اطلاعات، "
        "تولید متن و تصویر و کمک به حل مسئله استفاده می‌شود."
    )


def random_houl():
    print(random.randint(1, 6))


def Print_numbee():
    number = int(input("عددتان را وارد کنید: "))
    print(number)


def make_password():
    length = int(input("طول رمز (حداقل 8): "))
    if length < 8:
        print("برای امنیت، طول رمز باید حداقل 8 باشد.")
        return

    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(alphabet) for _ in range(length))
    print("رمز جدید:", password)


def game_random():
    system_number = random.randint(1, 10)
    guess = int(input("انتخاب کنید از 1 تا 10: "))

    if guess == system_number:
        print("درسته!")
    else:
        print("غلطه! عدد درست:", system_number)


def sleep_on():
    _time.sleep(10)


def time():
    print(_time.strftime("%H-%M-%S"))


def logout():
    # Placeholder function; it currently performs no action.
    pass


def internetofiran():
    print("متصل")


__version__ = "0.4"
__author__ = "Sajjad (@saj94jad)"


if __name__ == "__main__":
    print("2026 / @saj94jad / ToolPy / 0.4")
