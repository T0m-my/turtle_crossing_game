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


tim = Player()
FINISH_LINE_Y = 280
car = CarManager()
cars = []
cars.append(car)

screen.listen()
screen.onkey(quit_game, key='q')
screen.onkey(tim.move, 'Up')

game_is_on = True
counter = 6
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for car in cars:
        car.move()

        # stop game if car hits turtle player
        if car.distance(tim) < 20:
            game_is_on = False
            break

        # Detect when turtle player crosses finish line, return player to starting position and increase cars' speed
        if tim.ycor() >= FINISH_LINE_Y:
            tim.start_pos()
            car.increase_speed()
            print(car.move_distance)

    if counter == 0:
        counter = 6
        new_car = CarManager()
        cars.append(new_car)
    counter -= 1

screen.exitonclick()