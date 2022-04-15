"""

Name: Carson Shields
lab12.py

Problem: lab12 problems
Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""


def read_data(filename):
    file_object = open(filename, "r")
    read = file_object.read()
    read = read.replace('\n', ' ')
    cnt = 0
    while read:
        words = read.split(" ")
        while cnt < len(words):
            words[cnt] = int(words[cnt])
            cnt += 1
        return words
    file_object.close()


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if values[i] == search_val:
            return True
        i += 1
        return False
