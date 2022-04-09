"""
Name: Carson Shields
hw10.py

Problem: hw10 problem

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""

def fibonacci(num: int):
    num1, num2 = 1,1
    seq = []
    count = 0
    while count < num and num > 1:
        seq.append(num1)
        result = num1 + num2
        num1 = num2
        num2 = result
        count += 1
    return seq[num -1]


def double_investment(principle: float, rate: float): #good good
    px2 = principle * 2
    a_1 = principle * (1 + rate)
    b_1 = 1

    while a_1 <= px2:
        new_val = a_1
        a_1 = new_val * (1 + rate)
        b_1 += 1

    else:
        return b_1


def syracuse(num: int):
    nums = [num]
    while num != 1:
        if num % 2 == 0:
            num = num // 2
            nums.append(num)

        else:
            num = 3 * num + 1
            nums.append(num)

    return nums


def goldbach(num):
    prime = []
    value = 1
    while value <= num:
        count = 0
        i = 2
        while i <= value // 2:
            if value % i == 0:
                count = count + 1
                break
            i = i + 1
        if count == 0 and value != 1:
            prime.append(value)
        value += 1

        if num % 2 != 0:
            return None

        index_1 = 0
        index_2 = 0

        prime_1 = prime[index_1]
        prime_2 = prime[index_2]

        while prime_1 + prime_2 != num:
            if prime_2 == prime[-1]:
                index_1 += 1
                index_2 += 1
                prime_1 = prime[index_1]
                prime_2 = prime[index_2]
            else:
                index_2 += 1
                prime_2 = prime[index_2]

        return [prime_1, prime_2]
