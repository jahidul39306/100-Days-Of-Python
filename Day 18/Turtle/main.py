from turtle import Turtle, Screen
import random

turtle = Turtle()
screen = Screen()

# drawing square
# for _ in range (4):
#     turtle.forward(100)
#     turtle.left(90)

# dash line code
"""
for _ in range (15):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
"""
# drawing triangle to decagon

colors = ["rosy brown", "cyan", "chartreuse", "indigo", "dark slate blue", "dodger blue", "purple", "indian red"]

def draw_shape(number_of_sides):
    angle = 360 / number_of_sides
    turtle.color(random.choice(colors))
    for _ in range(number_of_sides):
        turtle.forward(100)
        turtle.left(angle)


screen.bgcolor("grey")
for number_of_sides in range(3, 11):
    draw_shape(number_of_sides)

screen.exitonclick()
