"""a sandboxy thing."""




from random import randint
from turtle import Turtle, colormode, done 
air: Turtle = Turtle()
colormode(255)


#why no work. :()
def sky(time: int, air :Turtle) -> None:
    """This will either make it night or day"""
    air.penup()
    air.goto(-100,-200)
    air.pendown()
    i: int = 0
    if time > 0:
        print("day")
        air.begin_fill()
        air.color("blue")
        while i > 4:
            air.forward(200)
            air.left(90)
            i =+ 1

n: int = 1    #randint (0,1)
air.penup()
air.goto(-100,-200)
air.pendown()
i: int = 0
if n > 0:
    air.begin_fill()
    air.color("blue")
    while i > 4:
        air.forward(200)
        air.left(90)
        i =+ 1  
else:
    air.begin_fill()
    air.color("black")
    while i > 4:
        air.forward(200)
        air.left(90)
        i =+ 1  
air.end_fill()


done()
# leo.penup()
# leo.goto(-200, -150)
# leo.pendown()


#   tree_top(-225, -150 ,40, leo)
#     tree_top(-200, -150 ,40, leo)
#     tree_top(-175, -150 ,40, leo)
#     tree_top(-170, -150 ,40, leo)
#     done()


# i: int = 0
# while (i < 3):
    
#     leo.begin_fill()
#     leo.color("green", "yellow")
#     leo.color(99, 204, 250)
#     leo.forward(115)
#     leo.left(120)
#     leo.end_fill()
#     i = i + 1

