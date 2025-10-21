from snake import Snake
from turtle import Screen
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)

snake = Snake()
game_is_over = False

while not game_is_over:
    screen.update()
    # TODO: iterate speed over time (?)
    time.sleep(.25)
    snake.move()

screen.exitonclick()