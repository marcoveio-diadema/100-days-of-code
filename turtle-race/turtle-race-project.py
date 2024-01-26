from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
positions = [-125, -75, -25, 25, 75, 125]
all_turtles = []

for turtle_pos in range(0, 6):
    turtle_racer = Turtle("turtle")
    turtle_racer.color(colors[turtle_pos])
    turtle_racer.penup()
    turtle_racer.goto(-230, positions[turtle_pos])
    all_turtles.append(turtle_racer)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            if user_bet == turtle.pencolor():
                print(f"The {turtle.pencolor()} turtle was the first to arrive! You've won!")
            else:
                print(f"You chose the {user_bet} turtle, but the first to arrive was the {turtle.pencolor()} "
                      f"turtle. You lost!")
        else:
            distance = random.randint(0, 10)
            turtle.forward(distance)



screen.exitonclick()