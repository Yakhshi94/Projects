from turtle import Turtle

MOVE_BY = 30


class Paddle(Turtle):

    def __init__(self, x=0, y=0):
        super().__init__()
        self.shape("square")
        self.setheading(90)
        self.color("white")
        self.penup()
        self.speed(20)
        self.setpos(x, y)
        self.shapesize(1, 5)

    def move_paddle_up(self):
        if self.ycor() < 270:
            self.forward(MOVE_BY)

    def move_paddle_down(self):
        if self.ycor() > -270:
            self.forward(-MOVE_BY)
