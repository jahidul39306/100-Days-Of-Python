from turtle import Turtle, Screen
import random

turtle_colors = ["red", "green", "blue", "yellow", "purple", "black"]
turtle_position = [-100, -60, -20, 20, 60, 100]
turtles_list = []

screen = Screen()
screen.setup(width=500, height=400)

user_input = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ")

for turtle_index in range(0, 6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(turtle_colors[turtle_index])
    new_turtle.goto(-230, turtle_position[turtle_index])
    turtles_list.append(new_turtle)

race_on = True

while race_on:
    for turtle in turtles_list:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 222:
            winner = turtle.pencolor()
            race_on = False
            break

if winner == user_input:
    print(f"The winner is {winner}")
    print("You won!!!")
else:
    print(f"The winner is {winner}")
    print("you lost")

screen.exitonclick()
