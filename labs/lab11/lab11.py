"""

Name: Carson Shields
lab11.py

Problem: 3 door game
Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""

from graphics import GraphWin, Point, Rectangle
from button import Button
from door import Door


def three_door_game():
    win = GraphWin("Test", 900, 900)
    win.setBackground("light gray")
    bbutton = Button(Rectangle(Point(300,100), Point(600, 200)), "EXIT")
    ddoor = Door(Rectangle(Point(300, 300), Point(600, 800)), "CLOSED")
    bbutton.color_button("light gray")
    ddoor.color_door("red")
    bbutton.draw(win)
    ddoor.draw(win)

    point = win.getMouse()
    while not bbutton.is_clicked(point):
        if ddoor.is_clicked(point):
            if ddoor.get_label() == 'OPEN':
                ddoor.close("red", 'CLOSED')
                print(ddoor.get_label())

            else:
                ddoor.open("white", 'OPEN')
                print(ddoor.get_label())

        point = win.getMouse()
    win.close()


three_door_game()
