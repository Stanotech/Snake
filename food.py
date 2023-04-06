from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.setpos(21 * random.randint(-10, 10), 21 * random.randint(-10, 10))
        self.shape("circle")
        self.color("white")
        self.penup()
