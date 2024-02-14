from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
MIN_Y = -250
MAX_Y = 250
DIRECTION = 180.0
STARTING_X = 310


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.create_car()
        self.position_car()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(choice(COLORS))

    def position_car(self):
        y_cor = randint(MIN_Y, MAX_Y)
        self.setheading(DIRECTION)
        self.goto(STARTING_X, y_cor)

    def move(self):
        self.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

