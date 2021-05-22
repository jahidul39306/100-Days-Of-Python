from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    squares_list = []

    def __init__(self):
        self.create_snake()
        self.head = self.squares_list[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            new_square = Turtle("square")
            new_square.color("white")
            new_square.penup()
            new_square.goto(position)
            self.squares_list.append(new_square)

    def move(self):
        # for loop range(start= , stop= , range= )
        for square_index in range(len(self.squares_list) - 1, 0, -1):
            new_x = self.squares_list[square_index - 1].xcor()
            new_y = self.squares_list[square_index - 1].ycor()

            self.squares_list[square_index].goto(new_x, new_y)

        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
