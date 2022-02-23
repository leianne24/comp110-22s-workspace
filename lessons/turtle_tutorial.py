"""Experimenting with Turtle."""
from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
colormode(255)

leo.speed(50)
# leo.hideturtle()



# leo.forward(50)
# leo.left(90)
# leo.forward(50)
# leo.left(90)
# leo.forward(50)
# leo.left(90)
# leo.forward(50)

leo.penup()
leo.goto(310, 260)
leo.pendown()

i: int = 0
leo.begin_fill()
while (i < 3):
    leo.color("green", "yellow")
    leo.color(99, 204, 250)
    leo.forward(115)
    leo.left(120)
    i = i + 1
leo.end_fill()



bob: Turtle = Turtle ()
bob.color("pink", "purple")
bob.speed(10000000)
bob.penup()
bob.goto(45, 60)
bob.pendown()
i: int = 0
while (i < 121):
    side_length: float = 300
    bob.forward(side_length)
    bob.left(121)
    side_length = side_length * 0.97
    i += 1



bob.speed(10000000)
bob.penup()
bob.goto(-40, 60)
bob.pendown()
i: int = 0
bob.begin_fill()
bob.color("yellow")
while (i < 36):
    side_length: float = 100
    bob.forward(side_length)
    bob.left(175)
    side_length = side_length * 0.97
    i += 1


done()


# To set only pen color: <turtlevariable>.pencolor(<color>)
# To set only fill color: <turtlevariable>.fillcolor(<color>)
# To set fill and pen color: <turtlevariable>.color(<pencolor>, <fillcolor>)

# to make the turtle do something
#turtle_object_variable.method_name()
# to import a specific function or class
# from turtle import [function_name]
# to set up a turle object
# <_turtlevariable_> : Turtle = Turtle()