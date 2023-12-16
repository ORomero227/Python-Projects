from turtle import Turtle
ALIGNMENT = "center"
FONT_STYLE = ("Arial", 14, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score = {self.score}", False, align=ALIGNMENT, font=FONT_STYLE)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, ALIGNMENT, FONT_STYLE)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
