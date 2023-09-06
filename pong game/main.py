from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("PONG GAME")
screen.bgcolor("black")
screen.tracer(0)

left_paddle = Paddle(x=-390, y=0)
right_paddle = Paddle(x=390, y=0)

ball = Ball()
left_score = Score(x_pos=-60, y_pos=240)
right_score = Score(x_pos=60, y_pos=240)

screen.listen()
screen.onkey(left_paddle.move_paddle_up, "w")
screen.onkey(left_paddle.move_paddle_down, "s")

screen.onkey(right_paddle.move_paddle_up, "Up")
screen.onkey(right_paddle.move_paddle_down, "Down")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall and bounce
    if ball.ycor() > 260 or ball.ycor() < -260:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 40 and ball.xcor() > 340 or ball.distance(left_paddle) < 40 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.reset_ball()
        screen.update()
        time.sleep(0.5)
        left_score.get_score()
    elif ball.xcor() < -400:
        ball.reset_ball()
        screen.update()
        time.sleep(0.5)
        right_score.get_score()




screen.exitonclick()