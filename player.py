from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
NORTH = 90.0


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(NORTH)

    def move(self):
        self.forward(MOVE_DISTANCE)
