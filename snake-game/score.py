from turtle import Turtle

ALIGNMENT = "center"
FONT = ('courier', 24, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.file_path = "snake-game/data.txt"
        with open(self.file_path) as data:
            content = data.read()
            if content.strip():
                self.high_score = int(content)
            else:
                self.high_score = 0

        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}. Highest score: {self.high_score}", False, ALIGNMENT, FONT)

    def new_point(self):
        self.score += 1
        self.update_score()

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snake-game/data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()






