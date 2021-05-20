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


angle = [0, 90, 180, 270]

screen.bgcolor("white")
my_turtle.pensize(5)
my_turtle.speed(0)

for _ in range(300):
    my_turtle.color(color_picker())
    my_turtle.forward(30)
    my_turtle.setheading(random.choice(angle))

screen.exitonclick()
