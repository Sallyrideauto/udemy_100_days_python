import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# main UI
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
step_count = 0  # game counter

while game_is_on:
    screen.update()
    time.sleep(0.1)

    step_count += 1

    if step_count % 6 == 0:
        car_manager.create_car()

    # move all cars any frame
    car_manager.move_cars()

    # detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
            break

    # check approach finish line
    if player.is_at_finish_line():
        player.reset_position()
        scoreboard.increase_level()
        car_manager.level_up()

screen.exitonclick()