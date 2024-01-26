from turtle import Turtle


class Square(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(290, 270)
        self.speed(0)
        self.hideturtle()
        self.make_line()

    def make_line(self):
        self.setheading(180)
        self.pendown()
        self.forward(590)


