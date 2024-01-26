from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "z")
screen.onkey(l_paddle.down, "s")

R_SCORE = 0
L_SCORE = 0


game_on = True

while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # make ball bounce
        ball.y_bounce()

    # detect collision with paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < - 320 and ball.distance(l_paddle) < 50:
        ball.x_bounce()

    # detect right paddle missed
    if ball.xcor() > 380:
        score.l_point()
        score.update_score()
        ball.reset_position()

    # detect left paddle missed the ball
    if ball.xcor() < -380:
        score.r_point()
        score.update_score()
        ball.reset_position()





























screen.exitonclick()
