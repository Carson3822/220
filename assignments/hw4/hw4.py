"""
Name: Carson Shields
Hw4.py

Problem: Hw 4 problems

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""
import math

from graphics import *


def squares():
 # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)
    win.setBackground("white")

    num_clicks = 5

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to Draw Squares")
    instructions.draw(win)

    shape = Rectangle(Point(225, 175), Point(175, 225))  # center of circle
    shape.draw(win)
    shape.setFill("white")
    shape.setOutline("white")

    for i in range(num_clicks):
        click = win.getMouse()
        change_x = click.getX()
        change_y = click.getY()

        shape = Rectangle(Point(change_x - 25, change_y - 25), Point(change_x + 25, change_y + 25))
        shape.draw(win)
        shape.setFill("red")
        shape.setOutline("red")

        i += 1

    message = Text(Point(200, 350), "Click to close window")
    message.draw(win)

    win.getMouse()
    win.close()

def rectangle():
    width = 400
    height = 400
    win = GraphWin("Rectangle", width, height)
    win.setBackground("white")

    click_1 = win.getMouse()
    p_1 = Point(click_1.getX(), click_1.getY())
    click_2 = win.getMouse()
    p_2 = Point(click_2.getX(), click_2.getY())

    shape = Rectangle(p_1, p_2)
    shape.draw(win)
    shape.setFill("green")
    shape.setOutline("green")
    base = abs(click_1.getX() - click_2.getX())
    hght = abs(click_1.getY() - click_2.getY())

    area = (base * hght)
    perimeter = (2 * base + 2 * hght)

    Text(Point(180, 350), "Area:").draw(win)
    Text(Point(180, 375), "Perimeter:").draw(win)
    Text(Point(220,350), area).draw(win)
    Text(Point(223.4, 375), perimeter).draw(win)



    Text(Point(200,330), "Click Again to Close").draw(win)

    win.getMouse()
    win.close()



def circle():
    width = 400
    height = 400
    win = GraphWin("Rectangle", width, height)
    win.setBackground("white")

    click_1 = win.getMouse()
    p_1 = Point(click_1.getX(), click_1.getY())
    x_1 = click_1.getX()
    y_1 = click_1.getY()

    click_2 = win.getMouse()
    x_2 = click_2.getX()
    y_2 = click_2.getY()

    dist = ((((x_2 - x_1) ** 2) + (y_2 - y_1) ** 2) ** (1 / 2))

    shape = Circle(p_1, dist)
    shape.draw(win)
    shape.setFill("light blue")
    shape.setOutline("light blue")

    r_msg = Text(Point(100,350), "Radius:")
    r_msg.draw(win)
    Text(Point(200,350), (dist/2)).draw(win)


    end_msg = Text(Point(200,330), "Click Again to Close")
    end_msg.draw(win)

    win.getMouse()
    win.close()







def pi2():
    num_inp = eval(input("how many terms are there?: "))
    acum_pi = 0
    numerator = 4
    denomenator = 1
    sign = 1

    for i in range(0, num_inp):

        acum_pi += sign * (numerator/denomenator)
        denomenator += 2
        sign = sign * -1

        i += 1

    print("pi approximation: ", acum_pi)
    print("accuracy:", abs(math.pi-acum_pi))



if __name__ == '__main__':

