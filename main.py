# import colorgram

import random
from turtle import Turtle, Screen, colormode

# This part was used to extract similar colours to the 
# app as a digital Hirst painting has.
# colors = colorgram.extract('2.jpg',30)
#
# print(len(colors))
# print(colors)
#
# color_list = []
# second_color = colors[1].rgb
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)
#
#
# print(color_list)
# print(second_color)

# turtle.screensize(canvwidth=None, canvheight=None, bg=None)

colormode(255)

extracted_colors = [(248, 232, 236), (232, 142, 77), (230, 65, 102), (246, 220, 81), (7, 175, 214), (210, 232, 238), (161, 53, 106), (233, 77, 60), (2, 132, 168), (86, 186, 211), (232, 125, 156), (143, 211, 221), (154, 77, 55), (41, 168, 106), (117, 191, 152), (1, 153, 92), (174, 147, 60), (240, 156, 177), (179, 199, 194), (27, 84, 62), (75, 53, 85), (20, 61, 122), (36, 65, 86), (75, 67, 48), (0, 109, 114), (245, 166, 153), (101, 125, 163), (175, 190, 213)]

tim = Turtle()
tim.speed("fastest")
tim.hideturtle()

tim.up()
tim.left(90)
tim.forward(285)
tim.left(90)
tim.forward(320)
tim.setheading(0)


def circle_and_move():
    tim.dot(30, random.choice(extracted_colors))
    tim.forward(70)

for _ in range(9):
    for _ in range(10):
        circle_and_move()
    tim.setheading(270)
    tim.forward(70)
    tim.setheading(180)
    tim.forward(700)
    tim.setheading(0)

screen = Screen()
screen.exitonclick()

