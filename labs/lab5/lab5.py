"""
Name: Carson Shields
lab5.py

Problem: text processing and graphics
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *

def triangle():
    win = GraphWin("Triangle", 1000, 1000)

    msg = "Click in the window 3 times to draw a triangle"
    inst = Text(Point(500, 100), msg)
    inst.draw(win)

    click = win.getMouse()
    point = Point(click.getX(), click.getY())

    click_2 = win.getMouse()
    point_2 = Point(click_2.getX(), click_2.getY())

    click_3 = win.getMouse()
    point_3 = Point(click_3.getX(), click_3.getY())

    tri = Polygon(point, point_2, point_3).draw(win)
    tri.setFill("green")
    tri.setOutline("green")

    len_side_ax = click_2.getX()-click.getX()
    len_side_ay = click_2.getY()-click.getY()
    len_a = (len_side_ax + len_side_ay) ** (1/2)

    len_side_bx = click_3.getX() - click.getX()
    len_side_by = click_3.getY() - click.getY()
    len_b = (len_side_bx + len_side_by) ** (1 / 2)

    len_side_cx = click_2.getX() - click_3.getX()
    len_side_cy = click_2.getY() - click_3.getY()
    len_c = (len_side_cx + len_side_cy) ** (1 / 2)

    s = (len_a + len_b + len_c) / 2

    area = ((s*(s-len_a)) * (s*(s-len_b)) * (s*(s-len_c))) ** (1/2)
    parameter = len_c + len_b + len_a

    Text(Point(400, 150), "area: ").draw(win)
    Text(Point(550, 150), area).draw(win)

    Text(Point(400, 175), "parameter: ").draw(win)
    Text(Point(550, 175), parameter).draw(win)

    Text(Point(500, 900), "click to close window").draw(win)
    win.getMouse()
    win.close()


def color_shape():
    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    red_amnt = Entry(Point(win_width / 2 + 25, win_height / 2 + 40), 10).draw(win)
    green_amnt = Entry(Point(win_width / 2 + 25, win_height / 2 + 70), 10).draw(win)
    blue_amnt = Entry(Point(win_width / 2 + 25, win_height / 2 + 100), 10).draw(win)

    for i in range(1):
        win.getMouse()

        r_a = eval(red_amnt.getText())
        g_a = eval(green_amnt.getText())
        b_a = eval(blue_amnt.getText())

        color = color_rgb(r_a, g_a, b_a)
        shape.setFill(color)

    # Wait for another click to exit
    inst = Text(Point(win_width / 2, win_height - 45), "click again to close window")
    inst.draw(win)

    win.getMouse()
    win.close()


def process_string():
    txt = input("What is the text you wish to process?: ")
    f_char = txt[0]
    l_char = txt[-1]
    char_2_5 = txt[2:6]
    concat_f_l = f_char + l_char
    f_3_char = txt[0:3] * 10
    lst_val = [f_char, l_char, char_2_5, concat_f_l, f_3_char]

    for i in range(len(lst_val)):
        print(lst_val[i])
        i += 1

    for i in range(len(txt)):
        print(txt[i])
        i += 1

    print(len(txt))


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]

    x = values[1]+values[3]
    print(x)

    x = values[0]+values[2]
    print(x)

    x = values[1]*values[0]
    print(x)

    x = values[2:5]
    print(x)

    x = values[2:4]
    x.append(values[0])
    print(x)

    x = [values[2]] + [values[0]]
    x.append(values[-1])
    print(x)

    x = values[2] + values[0] + float(values[-1])
    print(x)

    x = len(values)
    print(x)


def another_series():
    num_terms = eval(input("how many terms?:"))
    sum_terms = 0

    for i in range(num_terms):
        order = 2 + 2 * (i % 3)
        print(order, end=" ")
        sum_terms += order
    print("\n", "sum =", sum_terms)


def target():
    width = 1000
    hieght = 1000
    r = (width / 2)
    center = Point(500, 500)
    win = GraphWin("Target", width, hieght)

    white = Circle(center, r)
    white.setFill("white")
    white.setOutline("white")
    white.draw(win)

    black = Circle(center, (r * (4/5)))
    black.setFill("black")
    black.setOutline("black")
    black.draw(win)

    blue = Circle(center, r * (3/5))
    blue.setFill("blue")
    blue.setOutline("blue")
    blue.draw(win)

    red = Circle(center, r * (2/5))
    red.setFill("red")
    red.setOutline("red")
    red.draw(win)

    yellow = Circle(center, r * (1/5))
    yellow.setFill("yellow")
    yellow.setOutline("yellow")
    yellow.draw(win)

    win.getMouse()
    win.close()
