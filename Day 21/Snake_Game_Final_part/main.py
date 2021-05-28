from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")

screen.tracer(0)

my_snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)

    # detect collision with food
    if my_snake.head.distance(food) < 15:
        food.refresh()
        score.update()
        my_snake.increase_snake()

    # detect collision with wall
    if my_snake.head.xcor() > 270 or my_snake.head.xcor() < -285 or my_snake.head.ycor() > 280\
            or my_snake.head.ycor() < -275:
        game_is_on = False
        score.game_over()

    # detect collision with tail
    for segment in my_snake.squares_list[1:]:
        if my_snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

    screen.onkey(my_snake.up, "Up")
    screen.onkey(my_snake.down, "Down")
    screen.onkey(my_snake.left, "Left")
    screen.onkey(my_snake.right, "Right")
    my_snake.move()

screen.exitonclick()
