# """a sandboxy thing."""

# i: int = 0 
# def tree_top(base: int, height: int, size:int, leo: Turtle) -> None:
#     """Will draw a (happy) green triangle."""
#     i: int = 0
#     n: int = 0
#     x: int = 0
#     h: int = height
#     leo.speed(10000000)
#     leo.color("green")
#     leo.penup()
#     leo.goto(base, height)
#     leo.pendown()
#     while (x < 4):
#         n = 0
#         height = h
#         while (n < 4):
#             leo.begin_fill()
#             while (i < 3):
#                 leo.forward(size)
#                 leo.left(120)
#                 i = i + 1
#             height += 40 
#             leo.penup()
#             leo.goto(base, height)
#             leo.pendown()
#             i = 0
#             n += 1
#             leo.end_fill()
#         base += 150
#         x += 1




# from random import randint
# from turtle import Turtle, colormode, done 
# dirt: Turtle = Turtle()
# colormode(255)


# dirt.penup()
# dirt.goto(-310,-260)
# dirt.pendown()
# dirt.begin_fill()
# dirt.color ("brown")
# i:int = 0
# while i < 2:
#     dirt.forward(620)
#     dirt.left(90)
#     dirt.forward(100)
#     dirt.left(90)
#     i += 1 
# dirt.end_fill()

# # #why no work. :()
# # def sky(time: int, air :Turtle) -> None:
# #     """This will either make it night or day"""
# #     air.penup()
# #     air.goto(-100,-200)
# #     air.pendown()
# #     i: int = 0
# #     if time > 0:
# #         print("day")
# #         air.begin_fill()
# #         air.color("blue")
# #         while i > 4:
# #             air.forward(200)
# #             air.left(90)
# #             i =+ 1

# # n: int = 1    #randint (0,1)
# # air.penup()
# # air.goto(-100,-200)
# # air.pendown()
# # i: int = 0
# # if n > 0:
# #     air.begin_fill()
# #     air.color("blue")
# #     while i > 4:
# #         air.forward(200)
# #         air.left(90)
# #         i =+ 1  
# # else:
# #     air.begin_fill()
# #     air.color("black")
# #     while i > 4:
# #         air.forward(200)
# #         air.left(90)
# #         i =+ 1  
# # air.end_fill()


# done()
# # leo.penup()
# # leo.goto(-200, -150)
# # leo.pendown()


# #   tree_top(-225, -150 ,40, leo)
# #     tree_top(-200, -150 ,40, leo)
# #     tree_top(-175, -150 ,40, leo)
# #     tree_top(-170, -150 ,40, leo)
# #     done()


# # i: int = 0
# # while (i < 3):
    
# #     leo.begin_fill()
# #     leo.color("green", "yellow")
# #     leo.color(99, 204, 250)
# #     leo.forward(115)
# #     leo.left(120)
# #     leo.end_fill()
# #     i = i + 1

