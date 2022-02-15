"""TODO: Describe your scene program."""

__author__ = "730308277"

from turtle import Turtle, colormode, done 
leo: Turtle = Turtle()

colormode(255)

#maybe to shell
def main() -> None:
    """The entrypoint of my scene."""
    # TODO: Declare your Turtle variable(s) here.
    # TODO: Call the procedures you define and pass your Turtle(s) as an argument.
    tree_top(115, -150 ,40, leo)
    done()

# TODO: Define the procedures for other components in your scene here.
i: int = 0 
def tree_top(base :int, height :int, size :int, leo: Turtle) -> None:
    """Will draw a (happy) green triangle."""
    
    i: int = 0
    n: int = 0
    leo.color("green")
    leo.penup()
    leo.goto(-250, height)
    leo.pendown()
    
    while (n < 4):
        leo.begin_fill()
        while (i < 3):
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

        # if i == 3: 
        #     leo.penup()
        #     leo.goto(-250, (height  + 40))
        #     leo.pendown()
        #     i = 0



#mapping

main()


done()

# TODO: Use the __name__ is "__main__" idiom shown in 


# background blue
#Sunset
