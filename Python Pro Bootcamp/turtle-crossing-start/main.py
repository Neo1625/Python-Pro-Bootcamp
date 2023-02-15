import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(key="Up", fun=player.move_up)

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect when the turtle collides with a car
    if car_manager.detect_collision(player):
        scoreboard.game_over()
        game_is_on = False

    #Detect when the player has reached the other side
    if player.is_at_finish_line():
        player.reset_position()
        car_manager.increase_speed()
        scoreboard.level_up()



screen.exitonclick()