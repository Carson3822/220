"""

Name: Carson Shields
lab12.py

Problem: lab12 problems
Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""

from random import randint


def find_and_remove_first(lst, value):
    i = -1
    while i != 'Carson' and i < len(lst):
        i += 1
        if value == lst[i]:
            lst.pop(value)
            lst.insert(i, 'Carson')
            i = 'Carson'


def good_input():
    value = eval(input("enter a number between 1 and 10: "))
    while not 10 >= value >= 1:
        if value > 10:
            value = eval(input(("value is too high, enter a value between 1 and 10: ")))
        if value < 1:
            value = eval(input(("value too low, enter a value between 1 and 10: ")))
    return value


def num_digits():
    val = eval(input("enter a positive value greater than zero: "))
    while val > 0:
        div_val = val
        cnt = 0
        while div_val > 0:
            div_val = div_val // 10
            cnt += 1
        print(f"the number of digits in {val} is {cnt}")
        val = eval(input("enter a value that is positive and greater than zero to continue: "))


def hi_lo_game():
    rand_num = randint(1, 100)
    guess = eval(input("guess a number between 1 and 100: "))
    cnt = 1
    cnt_guesses = 0
    while cnt <= 7 and guess != rand_num:
        if guess > rand_num:
            print("your guess was too high")
            cnt += 1
            cnt_guesses += 1
            guess = eval(input("guess again: "))
        elif guess < rand_num:
            print("your guess was too low")
            cnt += 1
            cnt_guesses += 1
            guess = eval(input("guess again: "))
    if rand_num == guess:
        print("correct")
    else:
        print(f"you ran out of guesses, the number was {rand_num}")


if __name__ == '__main__':
    pass
    # good_input()
    # num_digits()
    # hi_lo_game()
