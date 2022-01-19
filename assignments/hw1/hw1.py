"""
Name: Carson Shields
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
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

    shooting_percentage = tot_made / tot_shots


print("shooting percentage: ", shooting_percentage)


def coffee():
    lbs_coffee = eval(input("How many lbs of coffee would you like?"))
    cost_coffee = (10.50 + 0.86) * lbs_coffee + 1.50

print("your total is: ", cost_coffee)

def kilometers_to_miles():
    pass


if __name__ == '__main__':
    pass
