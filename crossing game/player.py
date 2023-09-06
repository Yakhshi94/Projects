from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.color('white')
        self.penup()
        self.shape('turtle')
        self.setheading(90)
        self.setpos(STARTING_POSITION)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def goto_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() >= 280:
            return True
        else:
            return False
