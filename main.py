from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)

# TODO: remove commented code
# TODO: implement a snake class(?)
# class Snake(Turtle()):
#     def __init__(self):
#         self.length = 3
#         self.color("white")
#         self.shape("square")
#         self.name

def add_body_segment():
    """Adds a new body segment to the snake"""
    global snake
    current_length = len(snake)

    if current_length == 0:
        snake.append(get_body_segment())
    else:
        new_segment = get_body_segment()
        # TODO: account for current direction
        xcor = (snake[len(snake) - 1].xcor() - 20)
        new_segment.setpos(xcor, 0)
        snake.append(new_segment)

def get_body_segment():
    """Creates and returns a new body segment"""
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    return new_segment

# Initialise snake of length 3X body segments
snake = []
for _ in range(3):
    add_body_segment()

game_is_over = False

while not game_is_over:
    screen.update()
    # TODO: iterate speed over time (?)
    time.sleep(.25)
    for idx, body_segment in enumerate(reversed(snake)):
        # if current body segment is the head, move it forward
        if idx == (len(snake) - 1):
            body_segment.fd(20)
        # otherwise, move segment to the current position of the segment immediately in front of it
        else:
            body_segment.goto(snake[-idx + 1].pos())

screen.exitonclick()