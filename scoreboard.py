from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color('black')
        self.goto(-210, 260)
        self.update_display(f'LEVEL: {self.level}', 'center')

    def update_display(self, msg, alignment):
        if self.position() == (-210.0, 260.0):
            self.clear()
        self.write(arg=msg, align=alignment, font=FONT)

    def increase_level(self):
        self.level += 1
        # if self.position != (-210.0, 260.0):
        #     self.goto(-210, 260)
        self.update_display(f'LEVEL: {self.level}', 'left')

    def game_over(self):
        text = 'GAME OVER'
        self.goto(0, 0)
        self.update_display(text, alignment='center')

