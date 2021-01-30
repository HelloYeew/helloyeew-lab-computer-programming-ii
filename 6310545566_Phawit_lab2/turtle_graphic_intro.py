# You will learn about the import statement later;
# for now, think of import turtle as importing functions in the turtle module, containing graphic functions;
# see the document at https://docs.python.org/3/library/turtle.html
import turtle

# Set to slowest speed and east heading.
# Notice that before you invoke a function in the turtle module, the function name must be preceded by "turtle.".
# For example, turtle.speed(1) tells us that we want to use the speed function in the turtle module.
# If we want to use functions inside of a module, we must import that module first (like import turtle).
turtle.speed(1)
turtle.setheading(0)

# draw green circle
turtle.penup()
turtle.color("green")
turtle.fillcolor("green")
turtle.goto(0, 0)
turtle.pendown()
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

# draw blue circle
turtle.penup()
turtle.color("blue")
turtle.fillcolor("blue")
turtle.goto(0, -200)
turtle.pendown()
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

# draw red square
turtle.penup()
turtle.color("red")
turtle.fillcolor("red")
turtle.goto(-200, 0)
turtle.pendown()
turtle.begin_fill()
turtle.circle(100, 360, 4)
turtle.end_fill()

# draw yellow hexagon no fill
turtle.penup()
turtle.color("yellow")
turtle.goto(-200, -200)
turtle.pensize(5)
turtle.pendown()
turtle.circle(100, 360, 6)

# draw brown rectangle no fill
turtle.penup()
turtle.color("brown")
turtle.goto(100, 0)
turtle.pensize(1)
turtle.pendown()
turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.left(90)

# draw magenta half-circle
turtle.penup()
turtle.color("magenta")
turtle.fillcolor("magenta")
turtle.goto(200, -200)
turtle.pendown()
turtle.begin_fill()
turtle.circle(100, 180)
turtle.end_fill()

# draw a random polygon
turtle.setheading(90)
turtle.penup()
turtle.goto(200, 100)
turtle.color("black")
turtle.fillcolor("magenta")
turtle.pensize(10)
turtle.pendown()
turtle.begin_fill()
turtle.forward(100)
turtle.left(20)
turtle.forward(30)
turtle.left(60)
turtle.forward(50)
turtle.goto(200, 100)
turtle.end_fill()
turtle.setheading(0)

# hold the window; close it by clicking the window close 'x' mark
turtle.done()
