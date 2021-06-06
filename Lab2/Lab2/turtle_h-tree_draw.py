# turtle_h-tree_draw.py
import turtle


def tree_draw(level, size):
    if level == 0:
        return
    turtle.forward(size)
    turtle.left(90)
    tree_draw(level - 1, size * 0.7)
    turtle.right(90)
    turtle.right(90)
    tree_draw(level - 1, size * 0.7)
    turtle.left(90)
    turtle.forward(-1 * size)


turtle.penup()
turtle.goto(0, -350)
turtle.pendown()
turtle.speed(0)
turtle.setheading(90)
turtle.pensize(5)
turtle.color('deeppink4')
tree_draw(10, 300)

turtle.done()
