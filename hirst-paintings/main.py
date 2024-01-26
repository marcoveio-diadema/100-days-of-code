

import turtle
from turtle import Screen, Turtle
import random

color_list = [(235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]

bob = Turtle()
bob.hideturtle()
bob.speed(0)
turtle.colormode(255)
bob.penup()
bob.setheading(225)
bob.penup()
bob.forward(320)
bob.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    bob.dot(20, random.choice(color_list))
    bob.penup()
    bob.forward(50)
    if dot_count % 10 == 0:
        bob.left(90)
        bob.forward(50)
        bob.setheading(180)
        bob.forward(500)
        bob.setheading(0)


#
# bob.penup()
# bob.goto(-250, -200)
#
# for _ in range(10):
#     my_color_rgb = random.choice(color_list)
#     color_string = "#{:02x}{:02x}{:02x}".format(*my_color_rgb)
#     bob.color(color_string)
#     bob.dot(20)
#     bob.penup()
#     bob.forward(50)
#     bob.pendown()
#
#
# bob.penup()
# bob.goto(-250, -150)
#
# for _ in range(10):
#     my_color_rgb = random.choice(color_list)
#     color_string = "#{:02x}{:02x}{:02x}".format(*my_color_rgb)
#     bob.color(color_string)
#     bob.dot(20)
#     bob.penup()
#     bob.forward(50)
#     bob.pendown()






screen = Screen()
screen.exitonclick()






