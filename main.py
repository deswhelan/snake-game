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
    # Detect game over scenarios
    if (snake.head.xcor() >= 295
        or snake.head.xcor() <= -305
        or snake.head.ycor() >= 305
        or snake.head.ycor() <= -295):
        game_is_over = True
        scoreboard.display_final_score()
        # TODO: ask if player wants to play again and, if so, start a new game (?)
    else:
        if snake.head.distance(food) < 15:
            food.drop_food()
            scoreboard.update_score()
            snake.add_body_segment()
        snake.move()
        screen.update()
        # TODO: iterate speed over time (?)
        time.sleep(.1)

screen.exitonclick()