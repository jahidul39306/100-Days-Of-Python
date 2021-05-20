import turtle
from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()

screen.listen()


def move_forward():
    my_turtle.forward(10)


def move_backward():
    my_turtle.backward(10)


def move_anti_clockwise():
    my_turtle.setheading(my_turtle.heading() + 10)


def move_clockwise():
    my_turtle.setheading(my_turtle.heading() - 10)


def clear_screen():
    my_turtle.reset()


turtle.onkey(move_forward, "w")
turtle.onkey(move_backward, "s")
turtle.onkey(move_anti_clockwise, "a")
turtle.onkey(move_clockwise, "d")
turtle.onkey(clear_screen, "c")
screen.exitonclick()
