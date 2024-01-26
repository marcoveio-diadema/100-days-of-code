import turtle
import pandas
import csv


# create screen for the game
screen = turtle.Screen()
screen.title("U.S. States Game")

# set the background image as the turtle's shape
bg_image = "US-states/blank_states_img.gif"
screen.addshape(bg_image)
turtle.shape(bg_image)

# access the file
data = pandas.read_csv("US-states/50_states.csv")
state_list = data.state.to_list()
guessed_states = []

# initial score
SCORE = 0

while len(guessed_states) < 50:
    # question input
    answer = screen.textinput(f"Guess the State.    {SCORE}/50.", "What's the state's name?").title()

    if answer == "Exit":
        missed_states = [state for state in state_list if state not in guessed_states]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv('US-states/missed_states.csv')
        break

    # check answer and add points
    if answer in state_list:
        guessed_states.append(answer)
        s = turtle.Turtle()
        s.hideturtle()
        s.penup()
        state_row = data[data.state == answer]
        s.goto(int(state_row.x), int(state_row.y))
        s.write(answer)

        SCORE += 1

# create csv file for missing states









