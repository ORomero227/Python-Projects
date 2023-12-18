from turtle import Turtle
import random
COLORS = ["red", "blue", "green", "orange", "yellow"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(180)
        self.move_speed = 10

    def run(self):
        self.forward(self.move_speed)
