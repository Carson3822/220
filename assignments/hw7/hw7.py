"""
Name: Carson Shields
hw7.py

Problem: hw7 problem

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from encryption import encode_better, encode

def number_words(in_file_name: str, out_file_name: str):

    file_object = open(in_file_name, 'r')
    file_object_out = open(out_file_name, 'w')
    lines = file_object.readlines()
    word_num = 1

    for line in lines:
        line = line.split()
        for word in line:
            file_object_out.write(f"{word_num} {word}\n")
            word_num += 1

    file_object.close()
    file_object_out.close()


def hourly_wages(in_file_name: str, out_file_name: str):

    file_object = open(in_file_name, 'r')
    file_object_out = open(out_file_name, 'w')
    lines = file_object.readlines()

    for line in lines:
        line = line.split()
        hr_wage = int(line[2])
        hr_worked = int(line[3])
        file_object_out.write(f"{line[0]} {line[1]}: {((hr_wage * 1.65) * hr_worked):.2f}\n")

    file_object.close()
    file_object_out.close()


def calc_check_sum(isbn: str):
    isbn = isbn.replace("-", "")
    nums = []
    for i in range(10, 0, -1):
        nums += [i]
    sum = 0
    for i in range(len(isbn)):
        part_sum = int(isbn[i]) * nums[i]
        sum += part_sum

    return sum



def send_message(file_name, friend_name):
    file_object = open(file_name, "r")
    out_file_name = friend_name + ".txt"
    friend_file = open(out_file_name, "w")
    words_in_file = file_object.read().strip()
    print(words_in_file, file=friend_file)


def send_safe_message(file_name, friend_name, key):
    file_object = open(file_name, 'r')
    out_file_name = friend_name + ".txt"
    friend_file_object = open(out_file_name, "w")
    file = file_object.read()
    file_new = encode(file, key)
    new_line_ord = ord("\n") + key
    new_line_chr = chr(new_line_ord)
    file_new = file_new.replace(new_line_chr, "\n")

    print(file_new.strip(), file=friend_file_object)


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    file = open(file_name, "r")
    out_file_name = friend_name + ".txt"
    friend_file = open(out_file_name, "w")
    pad_file_import = open(pad_file_name, "r")
    file = file.read()
    pad_file = pad_file_import.read()
    new_file = encode_better(file, pad_file)
    print(new_file, file=friend_file)

if __name__ == '__main__':
    pass
