from turtle import Turtle
from ball import Ball

ALIGNMENT = "center"
FONT = ('courier', 80, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 220)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.l_score} x {self.r_score}", False, ALIGNMENT, FONT)

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def l_point(self):
        self.l_score += 1
        self.update_score()



