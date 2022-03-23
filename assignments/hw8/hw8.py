"""
Name: Carson Shields
hw8.py

Problem: hw8 problem

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""
import math
from graphics import GraphWin, Circle, Text, Point



def add_ten(nums: list[int]):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10
        i += 1


def square_each(nums: list[int]):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
        i += 1


def sum_list(nums: list[[]]):
    summ = 0
    for i in range(len(nums)):
        summ += nums[i]
        i += 1

    return summ


def to_numbers(nums: list[[str]]):
    for i in range(len(nums)):
        nums[i] = float(nums[i])


def sum_of_squares(nums: list[[str]]):
    for i in range(len(nums)):
        print(nums[i])
        print(type(nums[i]))
        # print(nums)
        if len(str(nums[i])) > 1:
            nums[i] = nums[i].split(" ")
            nums[i] = nums[i].replace(",", "")

    # nums = to_numbers(nums)
    # print(nums)
    # nums = square_each(nums)
    # print(nums)
    # nums = sum_list(nums)
    # print(nums)

    # return(nums)


def starter(weight, wins: int):
    if (150 <= weight < 160) and wins >= 5:
        return True

    return weight > 199 or wins >= 20



def leap_year(year: int):
    return year % 400 == 0 or year % 100 and year % 4 == 0



def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    cent_1 = win.getMouse()
    circ_pnt_1 = win.getMouse()
    rad_1 = math.sqrt((cent_1.getX() - circ_pnt_1.getX()) ** 2 + (cent_1.getY() - circ_pnt_1.getY()) ** 2)
    circle_one = Circle(cent_1, rad_1)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    cent_2 = win.getMouse()
    circ_pnt_2 = win.getMouse()
    rad_2 = math.sqrt((cent_2.getX() - circ_pnt_2.getX()) ** 2 + (cent_2.getY() - circ_pnt_2.getY()) ** 2)
    circle_two = Circle(cent_2, rad_2)
    circle_two.setFill("light green")
    circle_two.draw(win)

    if did_overlap(circle_one, circle_two) is True:
        txt_2 = Text(Point(cent_2.getX() - (rad_2 / 3), (cent_2.getY() - (rad_2 / 3))), "the circles overlap")
        txt_2.draw(win)

    else:
        txt = Text(Point(cent_2.getX() - (rad_2 / 3), (cent_2.getY() - (rad_2 / 3))),
        "the circles do not overlap")
        txt.draw(win)

    Text(Point(cent_2.getX() - (rad_2 / 2), (cent_2.getY() - (rad_2 / 2))), "click again to close").draw(win)
    win.getMouse()
    win.close()


def did_overlap(circle_one, circle_two):
    rad_1 = circle_one.getRadius()
    rad_2 = circle_two.getRadius()
    cent_1 = circle_one.getCenter()
    cent_2 = circle_two.getCenter()

    dist = math.sqrt((cent_2.getX() - cent_1.getX()) ** 2 + (cent_2.getY() - cent_1.getY()) ** 2)

    return dist <= (rad_2 + rad_1)


if __name__ == '__main__':
    pass
