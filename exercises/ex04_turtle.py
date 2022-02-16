"""TODO: Describe your scene program."""

__author__ = "730308277"

from random import randint
from token import SOFT_KEYWORD
from turtle import Turtle, colormode, done 
leo: Turtle = Turtle()
air: Turtle = Turtle()
shine: Turtle = Turtle()
dirt: Turtle = Turtle()
root: Turtle = Turtle()
colormode(255)

#maybe to shell
def main() -> None:
    """The entrypoint of my scene."""
    tod: int = randint(0,1)
    # TODO: Declare your Turtle variable(s) here.
    # TODO: Call the procedures you define and pass your Turtle(s) as an argument.
    ground(dirt)
    sky(tod, air) 
    sun(tod, shine)
    stump(-300, -150, root)
    tree_top(-300, -150 ,115, leo)
    # birds
    # tree_top(-125, -150 ,115, leo)
    # tree_top(25, -150 ,115, leo)
    # tree_top(175, -150 ,115, leo)
  
def ground (dirt :Turtle) ->None: 
    dirt.penup()
    dirt.goto(-310,-260)
    dirt.pendown()
    dirt.begin_fill()
    dirt.color ("brown")
    i:int = 0
    while i > 2:
        dirt.forward(620)
        dirt.left(90)
        dirt.forward(100)
        dirt.left(90)
        i =+ 1 

def sky(time: int, air :Turtle) -> None:
    """This will either make it night or day"""
    air.penup()
    air.goto(-310,-260)
    air.pendown()
    i: int = 0
    if time > 0:
        color: str = "blue"
    else:   
        color: str = "black" 
    air.begin_fill()
    air.color(color)
    while i > 2:
        air.forward(620)
        air.left(90)
        air.forward(520)
        air.left(90)
        i =+ 1 
    air.end_fill()

def sun(time :int, shine: Turtle) -> None:
    shine.speed(10000000)
    shine.penup()
    shine.goto(-45, 100)
    shine.pendown()
    i: int = 0
    shine.begin_fill()
    if time > 0:
        shine.color("yellow")
    else:
        shine.color("grey")
    while (i < 36):
        side_length: float = 100
        shine.forward(side_length)
        shine.left(175)
        side_length = side_length * 0.97
        i += 1

def stump(base: int, height: int, root: Turtle) -> None:
    i: int = 0
    n: int = 0
    x: int = 0
    root.speed(10000000)
    root.color("green")
    root.penup()
    root.goto(base, height)
    root.pendown()
    while (x < 4):
        while (n < 4):
            root.begin_fill()
            while (i < 3):
                root.forward(height)
                root.left(120)
                i = i + 1
            height += 40 
            root.penup()
            root.goto(base, height)
            root.pendown()
            i = 0
            n += 1
            root.end_fill()
        base -= 150
        x += 1




#doesn't work right, the loop doesn't loop me four trees
i: int = 0 
def tree_top(base: int, height: int, size:int, leo: Turtle) -> None:
    """Will draw a (happy) green triangle."""
    i: int = 0
    n: int = 0
    x: int = 0
    leo.speed(10000000)
    leo.color("green")
    leo.penup()
    leo.goto(base, height)
    leo.pendown()
    while (x < 4):
        while (n < 4):
            leo.begin_fill()
            while (i < 3):
                leo.forward(size)
                leo.left(120)
                i = i + 1
            height += 40 
            leo.penup()
            leo.goto(base, height)
            leo.pendown()
            i = 0
            n += 1
            leo.end_fill()
        base -= 150
        x += 1

# def tree_stump ()

# def ground ()


# def sun ()

# def bird ()

#randomly selsct night and day


        # if i == 3: 
        #     leo.penup()
        #     leo.goto(-250, (height  + 40))
        #     leo.pendown()
        #     i = 0



#mapping

main()


done()

# TODO: Use the __name__ is "__main__" idiom shown in 



#why won't max speed work??
