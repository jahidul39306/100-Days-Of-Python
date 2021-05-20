import turtle
from turtle import Turtle, Screen
import random

my_turtle = Turtle()
screen = Screen()
turtle.colormode(255)


def color_picker():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


my_turtle.speed(0)


def draw_spirograph(gap):
    for _ in range(int(360 / gap)):
        my_turtle.color(color_picker())
        my_turtle.circle(100)
        my_turtle.setheading(my_turtle.heading() + gap)


draw_spirograph(5)
screen.exitonclick()
