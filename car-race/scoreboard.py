from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-230, 270)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Level: {self.level}", False, "center", FONT)

    def update_level(self):
        self.level += 1
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, "center", FONT)






