"""

Name: Carson Shields
lab8.py

Problem: bumper
Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""

from random import randint
from graphics import color_rgb, GraphWin, Circle, Point
import time

def get_random(move_amount):
    rand_num = randint(-move_amount, move_amount)
    return rand_num

def did_collide(circ_1, circ_2):
    center_circ_1 = circ_1.getCenter()
    center_circ_2 = circ_2.getCenter()
    radius_circ_1 = circ_1.getRadius()
    radius_circ_2 = circ_2.getRadius()
    radius_sum = radius_circ_2 + radius_circ_1
    center_circ_1_x = center_circ_1.getX()
    center_circ_1_y = center_circ_1.getY()
    center_circ_2_x = center_circ_2.getX()
    center_circ_2_y = center_circ_2.getY()
    dist_1 = (center_circ_2_x - center_circ_1_x) ** 2
    dist_2 = (center_circ_2_y - center_circ_1_y) ** 2
    dist_tot = (dist_2 + dist_1) ** (1/2)

    if dist_tot <= radius_sum:
        return True
    else:
        return False

def hit_vertical(circ, win):
    height = win.getHeight()
    center_circ = circ.getCenter()
    center_circ_y = center_circ.getY()
    rad = circ.getRadius()
    return center_circ_y <= rad or center_circ_y >= height - rad

def hit_horizontal(circ, win):
    width = win.getWidth()
    center_circ = circ.getCenter()
    center_circ_x = center_circ.getX()
    rad = circ.getRadius()
    return center_circ_x <= rad or center_circ_x >= width - rad

def get_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color = color_rgb(red, green, blue)
    return color

def bumper():
    win = GraphWin("Bumper", 500, 500)
    circ_1 = Circle(Point(randint(0, 500), randint(0, 500)), 30)
    circ_2 = Circle(Point(randint(0, 500), randint(0, 500)), 30)
    circ_1.setFill(get_random_color())
    circ_2.setFill(get_random_color())
    circ_2.draw(win)
    circ_1.draw(win)

    circ_1_move_x = get_random(30)
    circ_1_move_y = get_random(30)
    circ_2_move_x = get_random(30)
    circ_2_move_y = get_random(30)


    while not win.checkMouse():
        circ_1_move = circ_1.move(circ_1_move_x, circ_1_move_y)
        circ_2_move = circ_2.move(circ_2_move_x, circ_2_move_y)


        if did_collide(circ_1, circ_2):
            circ_1_move_x = - circ_1_move_x
            circ_1_move_y = - circ_1_move_y
            circ_2_move_x = - circ_2_move_x
            circ_2_move_y = - circ_2_move_y

        if hit_vertical(circ_1, win):
            circ_1_move_x = - circ_1_move_x
            circ_1_move_y = - circ_1_move_y

        if hit_vertical(circ_2, win):
            circ_2_move_x = - circ_2_move_x
            circ_2_move_y = - circ_2_move_y

        if hit_horizontal(circ_1, win):
            circ_1_move_x = - circ_1_move_x
            circ_1_move_y = - circ_1_move_y

        if hit_horizontal(circ_2, win):
            circ_2_move_x = - circ_2_move_x
            circ_2_move_y = - circ_2_move_y

        time.sleep(.20)

    win.getMouse()
    win.close()