from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.color("blue")
        self.turtlesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()

    def refresh(self):
        x_cor = random.randint(-275, 275)
        y_cor = random.randint(-275, 275)
        self.goto(x_cor, y_cor)