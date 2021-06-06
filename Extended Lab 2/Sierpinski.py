import turtle


def sierpinski(n, size):
    if n == 0:
        for i in range(3):
            turtle.forward(size)
            turtle.left(120)
    else:
        sierpinski(n - 1, size / 2)
        turtle.forward(size / 2)
        sierpinski(n - 1, size / 2)
        turtle.backward(size / 2)
        turtle.left(60)
        turtle.forward(size / 2)
        turtle.right(60)
        sierpinski(n - 1, size / 2)
        turtle.left(60)
        turtle.backward(size / 2)
        turtle.right(60)


turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()
turtle.speed(0)
# turtle.setheading(90)
turtle.pensize(2)
turtle.color('green')
# run function here
sierpinski(5,400)
turtle.done()
