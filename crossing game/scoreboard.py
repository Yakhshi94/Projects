from turtle import Turtle

FONT = ("courier", 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(-265, 265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Level: {self.level}', align='left', font=FONT)

    def increase_leve(self):
        self.level += 1
        self.update_scoreboard()

    def reset(self):
        self.goto(0, 0)
        self.write(f'Game Over', align='center', font=FONT)
