"""Experimenting with Turtle."""
from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

leo.forward(50)
leo.left(90)
leo.forward(50)
leo.left(90)
leo.forward(50)
leo.left(90)
leo.forward(50)



i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
done()


# to make the turtle do something
#turtle_object_variable.method_name()
# to import a specific function or class
# from turtle import [function_name]
# to set up a turle object
# <_turtlevariable_> : Turtle = Turtle()