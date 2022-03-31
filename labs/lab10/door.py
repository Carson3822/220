"""

Name: Carson Shields
lab10.py

Problem: DOOR and BUTTON
Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""

from graphics import *


class Door:
    def __init__(self, shape: object, label: object) -> object:
        self.shape = shape
        self.text = Text(self.shape.getCenter(), label)
        self.secret = False

    def get_label(self):
        return repr(self.text)

    def set_label(self, new_label):
        self.text = Text(self.shape.getCenter(), new_label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        p1, p2 = self.shape.getP1(), self.shape.getP2()
        p1_y, p2_y = p1.getY(), p2.getY()
        p1_x, p2_x = p1.getX(), p2.getX()
        pc_x, pc_y = point.getX(), point.getY()

        y_range = p1_y <= pc_y <= p2_y
        x_range = p1_x <= pc_x <= p2_x

        if x_range and y_range:
            return True
        else:
            return False

    def open(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def close(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def color_door(self, color):
        self.shape.setFill(color)

    def is_secret(self):
        if self.secret:
            return True
        else:
            return False

    def secret_door(self, secret):
        self.secret = secret

