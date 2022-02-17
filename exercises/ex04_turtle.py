"""A happy forest with happy little trees. It turns from day to night randomly."""

__author__ = "730308277"

from random import randint
from turtle import Turtle, colormode, done 
leo: Turtle = Turtle()
air: Turtle = Turtle()
shine: Turtle = Turtle()
dirt: Turtle = Turtle()
root: Turtle = Turtle()
colormode(255)
MAX_SPEED: int = 10000000000000000000


def main() -> None:
    """The entrypoint of my scene."""
    tod: int = randint(0, 1)
    sky(tod, air) 
    stump(-250, -185, root)
    stump(-80, -185, root)
    stump(75, -185, root)
    stump(225, -185, root)
    ground(dirt)
    sun(tod, shine)
    tree_top(-300, -150, 115, leo)
    tree_top(-125, -150, 115, leo)
    tree_top(25, -150, 115, leo)
    tree_top(175, -150, 115, leo)


def ground(dirt: Turtle) -> None: 
    """Creates a nice pile of grass or dirt for my trees."""
    dirt.penup()
    dirt.goto(-310, -260)
    dirt.pendown()
    dirt.begin_fill()
    dirt.color(147, 229, 51)
    dirt.speed(MAX_SPEED)
    i: int = 0
    while i < 2:
        dirt.forward(620)
        dirt.left(90)
        dirt.forward(75)
        dirt.left(90)
        i += 1 
    dirt.end_fill()
    dirt.penup()


def sky(time: int, air: Turtle) -> None:
    """This will either make it night or day!"""
    air.speed(MAX_SPEED)
    air.penup()
    air.goto(-310, -260)
    air.pendown()
    i: int = 0
    if time > 0:
        air.color("blue")
    else:   
        air.color("black")
    air.begin_fill()
    while i < 2:
        air.forward(620)
        air.left(90)
        air.forward(520)
        air.left(90)
        i += 1 
    air.end_fill()


def sun(time: int, shine: Turtle) -> None:
    """Creates either a spiky sun or moon depending on a randint."""
    shine.speed(MAX_SPEED)
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
    """Creates a lil' stump for my trees to sit upon."""
    root.penup()
    root.goto(base, height)
    root.pendown()
    root.begin_fill()
    root.color(161, 93, 7)
    root.speed(MAX_SPEED)
    i: int = 0
    while i < 2:
        root.forward(20)
        root.left(90)
        root.forward(35)
        root.left(90)
        i += 1 
    root.end_fill()


def tree_top(base: int, height: int, size: int, leo: Turtle) -> None:
    """Will draw a (happy) green triangle."""
    i: int = 0
    n: int = 0
    leo.speed(MAX_SPEED)
    leo.color("green")
    leo.penup()
    leo.goto(base, height)
    leo.pendown()
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
    leo.penup()


main()
done()