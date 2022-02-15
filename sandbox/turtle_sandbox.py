"""a sandboxy thing."""




from turtle import Turtle, colormode, done 
leo: Turtle = Turtle()

colormode(255)

#maybe to shell
def main() -> None:
    """The entrypoint of my scene."""
    # TODO: Declare your Turtle variable(s) here.
    # TODO: Call the procedures you define and pass your Turtle(s) as an argument.

    tree_top(-250, -150 ,40, leo)
  

# TODO: Define the procedures for other components in your scene here.
i: int = 0 
def tree_top(base :int, height :int, size :int, leo: Turtle) -> None:
    """Will draw a (happy) green triangle."""
    i: int = 0
    n: int = 0
    # leo.speed(10000000)
    leo.color("green")
    leo.penup()
    leo.goto(base, height)
    leo.pendown()
    while (n < 4):
        leo.begin_fill()
        while (i < 3):
            leo.left(180)
            leo.forward(base)
            leo.left(120)
            i = i + 1
        height += 40
        leo.penup()
        leo.goto(-250, height)
        leo.pendown()
        i = 0
        n += 1
        leo.end_fill()   


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

