import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


def quit_game():
    global game_is_on
    game_is_on = False


screen.listen()
screen.onkey(quit_game, key='q')

tim = Player()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
