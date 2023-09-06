from turtle import Screen
from player import Player
from cars import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Road Crossing Game")
screen.bgcolor('black')
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.reset()

    if player.is_at_finish_line():
        player.goto_start()
        car_manager.speed_up()
        scoreboard.increase_leve()


screen.exitonclick()