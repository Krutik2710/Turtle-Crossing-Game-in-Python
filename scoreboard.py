from turtle import Turtle, Screen
ALIGNMENT = "center"
FONT = ("Courier",18,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0

        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.update_score()

    def update_score(self):
        self.write(f"SCORE: {self.score}",align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.write(f"GAME OVER",align=ALIGNMENT,font=FONT)