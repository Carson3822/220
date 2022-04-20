"""

Name: Carson Shields
lab13.py

Problem: lab13 problems
Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""


def trade_alert(file_name):
    file_object = open(file_name, "r")
    str = file_object.read()
    nums = str.split(" ")

    for i in range(len(nums)):
        if int(nums[i]) == 500:
            print(f"Alert trade volume for this stock reached 500 units/sec at time {i+1}")
        elif int(nums[i]) > 830:
            print(f"Warning trade volume for this stock reached above 830 units/sec at time {i+1}")
    file_object.close()


def star_find(file_name):
    file_object = open(file_name, "r")
    str = file_object.read()
    freq = str.split(" ")
    acc = 0
    cnt_i = 0
    star = []

    while acc < 5 or (cnt_i < len(freq)):
        if 4000 <= int(freq[cnt_i]) <= 5000:
            acc += 1
            cnt_i += 1
            star.append([acc, cnt_i, int(freq[cnt_i])])
        else:
            cnt_i += 1

    if acc >= 5:
        print(f"Congrats! you have found a neutron star {star}")
    else:
        print(f'unfortunately no neutron star was found {star}')
    file_obj
