from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

my_snake = Snake()
screen.listen()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)

    screen.onkey(my_snake.up, "Up")
    screen.onkey(my_snake.down, "Down")
    screen.onkey(my_snake.left, "Left")
    screen.onkey(my_snake.right, "Right")
    my_snake.move()

screen.exitonclick()
