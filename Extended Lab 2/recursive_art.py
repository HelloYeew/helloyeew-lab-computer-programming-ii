import turtle
import random

color = ["red", "green", "blue", "yellow", "magenta", "white", "linen", "cyan", "beige", "medium purple", "hot pink",
         "rosy brown", "orange", "gold", "spring green", "light blue"]

def recursive_art(n, size):
    if n == 0:
        for i in range(6):
            turtle.forward(size)
            turtle.left(60)
    else:
        recursive_art(n - 1, size - 10)
        turtle.color(random.choice(color))
        turtle.left(10)
        recursive_art(n - 1, size - 10)
        turtle.color(random.choice(color))
        turtle.left(10)




turtle.bgcolor("black")
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.speed(0)
# turtle.setheading(90)
turtle.pensize(2)
turtle.color(random.choice(color))
# run function here
recursive_art(5, 100)
recursive_art(5, 150)
recursive_art(5, 200)
recursive_art(5, 250)
recursive_art(5, 300)
recursive_art(5, 400)
recursive_art(5, 550)
turtle.done()
