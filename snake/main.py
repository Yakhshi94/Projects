# Snake game creation procedure
# 1 Create a Snake Body
# 2 Move the snake
# 3 Control the snake
# 4 Detect collision with food
# 5 Create a scoreboard
# 7 Detect collision with wall
# 8 Detect collision with tail

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    # Detect collision with Food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall
    xcor = snake.segments[0].xcor()
    ycor = snake.segments[0].ycor()
    if xcor > 280 or xcor < -280 or ycor > 280 or ycor < -280:
        for segment in snake.segments:
            segment.goto(450, 0)
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
