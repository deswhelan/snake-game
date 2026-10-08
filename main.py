from food import Food
from scoreboard import Scoreboard
from snake import Snake
from sound import play_chomp
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

def close_game():
    """Ends the game loop when the window is closed, so the window isn't destroyed mid-move"""
    global game_is_over
    game_is_over = True

screen.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", close_game)

screen.onkey(snake.face_north, "Up")
screen.onkey(snake.face_south, "Down")
screen.onkey(snake.face_east, "Right")
screen.onkey(snake.face_west, "Left")

while not game_is_over:
    if (snake.head_has_hit_body()
        # Detect collision with wall
        or snake.head.xcor() >= 295
        or snake.head.xcor() <= -305
        or snake.head.ycor() >= 305
        or snake.head.ycor() <= -295):
        scoreboard.reset_score()
        snake.reset_game()
        # scoreboard.display_final_score()
        # TODO: ask if player wants to play again and, if so, start a new game (?)
    else:
        # Detect collision with food
        if snake.head.distance(food) < 15:
            play_chomp()
            food.drop_food()
            scoreboard.update_score()
            snake.add_body_segment()
        snake.move()
        screen.update()
        # TODO: iterate speed over time (?)
        time.sleep(.1)

# Save the current score if it's a new high score, then close the window
scoreboard.reset_score()
screen.bye()