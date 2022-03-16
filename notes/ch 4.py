my_range: range = range(10)
my_other_range: range = range(3,7)
# same data type and class but different objects because they store different data points.

x = 7
y = 9
# both int types but diff objects bc store different values.

import math
import graphics

math.sqrt(25)

my_point = graphics.Point(50, 70)
point_a = graphics.Point(70, 90)

# point is general class framework for data my_point is the object
xx = point_a.getX() # x = 70
print(point_a.getX())  #returns x value

point_a.getY()

print(point_a.getX(), point_a.getY())  # accessor methods (ways ot return values of instance variables)

point_a.move(10, 0) # takes point and moves it to the right by 10 (.move mutates the instance variable by its worth)


win = graphics.GraphWin("CSCI 220")
input("hit enter to close")


win = graphics.GraphWin("CSCI 220", 700,700)  # sat
point_a.draw(win)
input("hit enter to close")

middle = graphics.Point(350, 350)
middle.draw(win)
input("hit enter to close")



from graphics import Point, GraphWin, Circle
#now we dont have to put graphics.Point(x, y)  do this for hw

my_point = Point(70,80)

my_circle = Circle(middle, 70)
my_circle.draw(win)

input("hit enter to close")


