"""
Name: Carson Shields
lab4.py

Problem: Create valentines Card
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *

def greeting_card():
    width = 800
    height = 800
    win = GraphWin("Valentines", width , height)

    win.setBackground("pink")

    message_1 = Text(Point(400,200), "Happy Valentines Day! Have a Heart")
    message_1.draw(win)

    lft_hrt = Circle(Point(350,275), 50)
    rht_hrt = Circle(Point(450,275), 50)
    lft_hrt.setFill("red")
    rht_hrt.setFill(("red"))
    lft_hrt.setOutline("red")
    rht_hrt.setOutline("red")
    lft_hrt.draw(win)
    rht_hrt.draw(win)


    triangle = Polygon(Point(300, 275),Point(400, 425), Point(500, 275))
    triangle.setFill("red")
    triangle.setOutline("red")
    triangle.draw(win)

    a_1 = Point(50, 750)
    a_2 = Point(110, 675)
    p_1 = Point(102, 672)
    p_2 = Point(113, 685)

    arrow_hd_lft = Line(p_1, a_2)
    arrow_hd_rht = Line(p_2, a_2)
    arrow = Line(a_1, a_2)
    arrow_hd_rht.draw(win)
    arrow_hd_lft.draw(win)
    arrow.draw(win)

    for frame in range(10):
        arrow.move(60, -75)
        arrow_hd_lft.move(60, -75)
        arrow_hd_rht.move(60, -75)
        time.sleep(0.20)

    message_2 = Text(Point(400, 500), "click to close (:")
    message_2.draw(win)

    win.getMouse()
    win.close()
