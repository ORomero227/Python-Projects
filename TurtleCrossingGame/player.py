from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.start_position()

    def move(self):
        self.forward(10)

    def start_position(self):
        self.setheading(90)
        self.goto(0, -250)
