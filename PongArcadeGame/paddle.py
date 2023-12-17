from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def move_up(self):
        new_ycor = self.ycor() + 20
        new_position = (self.xcor(), new_ycor)
        self.goto(new_position)

    def move_down(self):
        new_ycor = self.ycor() - 20
        new_position = (self.xcor(), new_ycor)
        self.goto(new_position)
