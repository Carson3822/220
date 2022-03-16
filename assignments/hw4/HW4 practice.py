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

    shape = Rectangle(Point(225, 175), Point(175,225))  # center of circle
    shape.draw(win)
    shape.setFill("white")
    shape.setOutline("white")

    for i in range(num_clicks):
        click = win.getMouse()
        center = shape.getCenter()
        change_x = click.getX()
        change_y = click.getY()

        shape = Rectangle(Point(change_x - 25, change_y - 25), Point(change_x + 25, change_y + 25))
        shape.draw(win)
        shape.setFill("red")
        shape.setOutline("red")

    message = Text(Point(200, 350), "Click to close window")
    message.draw(win)

    win.getMouse()
    win.close()
