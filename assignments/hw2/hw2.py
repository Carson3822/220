"""
Name: <your name goes here – Carson Shields
hw2.py

Problem: Homework 2 problems
Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""
import math


def sum_of_threes():
    ubound = eval(input("what is the upper bound?: "))
    sum3 = 0
    for i in range(0, ubound):
        if (i*3) <= ubound:
            sum3 += i*3


    print(sum3)



def multiplication_table():
    for x_1 in range( 1 , 11 ):
        for y_1 in range( 1 , 11 ):
            print(str(x_1 * y_1), end="\t")
        print()


def triangle_area():
    length_a = eval(input("enter side a length: "))
    length_b = eval(input("enter side b length: "))
    length_c = eval(input("enter side c length: "))

    s_1 = ((length_a + length_b + length_c)/ 2)

    tot_area = math.sqrt(s_1*((s_1-length_a)*(s_1-length_b)*(s_1-length_c)))

    print(tot_area)



def sum_squares():
    low_lim = eval(input("Enter lower range: "))
    up_lim = eval(input("Enter upper range: "))

    sum_1 = 0
    for i in range(low_lim, up_lim+1):
        sum_1 += (i ** 2)

    print(sum_1)


def power():
    base = eval(input("Enter Base:"))
    pow_ = eval(input("Enter Power: "))

    answer = base ** pow_

    print(answer)






if __name__ == '__main__':
    pass
