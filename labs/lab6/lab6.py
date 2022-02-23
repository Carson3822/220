"""
Name: Carson Shields
hw6.py

Problem: hw6 problem

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math
def cash_converter():
    integer = eval(input("enter an integer: "))
    dollar_amnt = "that is ${:.2f}".format(integer)
    print(dollar_amnt)


def encode():
    msg = input("enter a message: ")
    key = eval(input("enter a key: "))
    new_msg = ""

    for i in range(len(msg)):
        character = msg[i]
        new_msg += chr(ord(character) + key)

    print(new_msg)


def sphere_area(radius: float):
    area = (4 * math.pi) * (radius ** 2)

    return area


def sphere_volume(radius: float):
    volume = (4.0/3.0) * math.pi * radius ** 3.0

    return volume


def sum_n(number: int):
    total = 0
    for i in range(number+1):
        total += i

    return total


def sum_n_cubes(number: int):
    total = 0
    for i in range(number + 1):
        total += i**3

    return total


def encode_better():


    msg = input("enter a message: ")
    key = input("enter a key: ")
    key_length = 

    for i in range(len(msg)):
        for j in key
        key += j

        i+1
    #for i in range(len(cypher)):
        #print(cypher[i], end=": ")
        #print(i)
    #print(len(cypher))


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
