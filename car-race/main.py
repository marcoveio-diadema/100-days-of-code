import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# SET UP SCREEN FOR THE GAME
screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)


# INSTANCES
player = Player()
car_manager = CarManager()
score = Scoreboard()

# SCREEN LISTENER
screen.listen()
screen.onkey(player.move_up, "Up")

# WHILE LOOP FOR GAME TO RUN
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with a car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    # detect passage to next level
    if player.reached_end():
        player.reset_position()
        car_manager.next_level()
        score.update_level()
        score.show_score()








screen.exitonclick()