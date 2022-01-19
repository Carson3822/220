"""
Name: Carson Shields
hw1.py

Problem: HW1 problems

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width

    print("Area =", area)

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the hieght: "))
    volume = length * width * height
    print("volume =", volume)



def shooting_percentage():
    tot_shots = eval(input("enter total shots: "))
    tot_made = eval(input("enter total shots made: "))

    shot_percentage = (tot_made / tot_shots) * 100


    print("shooting percentage: ", shot_percentage)


def coffee():
    lbs_coffee = eval(input("How many lbs of coffee would you like?"))
    cost_coffee = round((10.50 + 0.86) * lbs_coffee + 1.50, 2)

    print("your total is: ", cost_coffee)

def kilometers_to_miles():
    kilometers = eval(input("enter number of kilometers: "))
    miles = kilometers / 1.61
    print("that's equal to", miles, "miles.")

if __name__ == '__main__':
    pass
