from food import Food
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

game_is_over = False

screen.onkey(snake.face_north, "Up")
screen.onkey(snake.face_south, "Down")
screen.onkey(snake.face_east, "Right")
screen.onkey(snake.face_west, "Left")

while not game_is_over:
    # TODO: implement
    if food.pos() == snake.head.pos():
        food.drop_food()
    # TODO: iterate speed over time (?)
    time.sleep(.1)
    snake.move()

screen.exitonclick()