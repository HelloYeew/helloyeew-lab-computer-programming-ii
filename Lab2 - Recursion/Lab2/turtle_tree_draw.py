import turtle

def tree_draw(level, size):
    if level == 0:
        return
    turtle.forward(size)
    turtle.left(25)
    tree_draw(level - 1, size*0.65)
    turtle.right(25)
    turtle.right(35)
    tree_draw(level - 1, size*0.85)
    turtle.left(35)
    turtle.forward(-1*size)

turtle.speed(0)
turtle.setheading(90)
turtle.pensize(4)
turtle.color('red')
tree_draw(5, 100)

turtle.done()
