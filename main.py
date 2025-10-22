from food import Food
from scoreboard import Scoreboard
from snake import Snake
from turtle import Screen
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.listen()
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_over = False

screen.onkey(snake.face_north, "Up")
screen.onkey(snake.face_south, "Down")
screen.onkey(snake.face_east, "Right")
screen.onkey(snake.face_west, "Left")

while not game_is_over:
    if snake.head.distance(food) < 15:
        food.drop_food()
        scoreboard.update_score()
        # TODO: implement
        # snake.add_body_segment()
    screen.update()
    # TODO: iterate speed over time (?)
    time.sleep(.1)
    snake.move()

screen.exitonclick()