"""

Name: Carson Shields
lab6.py

Problem: text processing and graphics
Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""
from graphics import *


def vigenere():
    win = GraphWin("Vigenere", 500, 500)
    msg_1 = Text(Point(75, 50), "Message to Code")
    msg_1.draw(win)
    msg_2 = Text(Point(75, 100), "Enter Keyword")
    msg_2.draw(win)

    box_1 = Entry(Point(267, 50), 40).draw(win)
    box_2 = Entry(Point(180, 100), 15).draw(win)

    button = Rectangle(Point(200, 200), Point(300, 150))
    button.draw(win)

    button_txt = Text(button.getCenter(), "Encode")
    button_txt.draw(win)

    win.getMouse()
    button.undraw()
    button_txt.undraw()

    msg = box_1.getText()
    key = box_2.getText()
    msg = msg.upper()
    key = key.upper()
    msg = msg.replace(" ", "")
    key.replace(" ", "")

    encoded = ""
    for i in range(len(msg)):

        value = ord(msg[i]) - 65
        k_val = ord(key[i % len(key)]) - 65
        val_2 = ((k_val + value) % 26) + 65

        letter = chr(val_2)
        encoded += letter

    Text(Point(250, 250), "Resulting Message").draw(win)
    Text(Point(250, 275), encoded).draw(win)

    Text(Point(250, 400), "click again to close window").draw(win)
    win.getMouse()
    win.close()

