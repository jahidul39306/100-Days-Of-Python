# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("hirst_painting.jpg", 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle
from turtle import Turtle, Screen
import random

color_list = [(201, 164, 112), (239, 246, 241), (152, 75, 50), (221, 201, 138),
              (57, 95, 126), (170, 152, 44), (138, 31, 20), (135, 163, 183), (196, 94, 75), (49, 121, 88),
              (143, 177, 149),
              (95, 75, 77), (76, 39, 32), (164, 146, 157), (16, 98, 71), (232, 176, 165), (54, 46, 48), (32, 61, 76),
              (22, 83, 89),
              (182, 204, 176), (141, 22, 25), (86, 147, 127), (45, 66, 85), (8, 68, 53), (177, 94, 97), (222, 177, 182),
              (109, 128, 151)]

turtle.colormode(255)

my_turtle = Turtle()
screen = Screen()
turtle.speed("fastest")
my_turtle.hideturtle()

x = -200
y = -200


def set_position(x, y):
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()


for _ in range(0, 10):
    set_position(x, y)
    for _ in range(0, 10):
        my_turtle.dot(20, random.choice(color_list))
        my_turtle.penup()
        my_turtle.forward(50)
        my_turtle.pendown()
    y += 50


screen.exitonclick()
