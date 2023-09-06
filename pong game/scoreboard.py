from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 14, 'normal')


class Score(Turtle):
    """"Pass X and Y Position Of The ScoreBoard While Initiating the class object"""
    def __init__(self, x_pos=0, y_pos=0):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(x_pos, y_pos)
        self.score = 0
        self.get_score()

    def get_score(self):
        self.clear()
        self.write(f'SCORE: {self.score}', move=False, align=ALIGNMENT, font=FONT)
        self.score += 1
