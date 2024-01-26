
from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score
from square import Square

# create screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

square = Square()
score = Score()
snake = Snake()
food = Food()



screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.new_point()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 260 or snake.head.ycor() < -280:
        score.reset_game()
        # score.play_again()
        snake.snake_reset()
        snake.move()

    # detect collision with its tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10 :
            score.reset_game()
            # score.play_again()
            snake.snake_reset()
            snake.move()

















screen.exitonclick()