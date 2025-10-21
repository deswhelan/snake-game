from turtle import Screen, Turtle

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("SNAKE")

# TODO: remove commented code
# TODO: implement a snake class(?)
# class Snake(Turtle()):
#     def __init__(self):
#         self.length = 3
#         self.color("white")
#         self.shape("square")
#         self.name

def add_body_segment():
    global snake
    current_length = len(snake)

    if current_length == 0:
        snake.append(get_body_segment())
    else:
        # print(f"adding segment {len(snake) + 1}")
        new_segment = get_body_segment()
        # TODO: account for current direction
        xcor = (snake[len(snake) - 1].xcor() - 20)
        # print(f"xcor for previous segment: {snake[len(snake) - 1].xcor()}")
        # print(f"xcor for segment {len(snake) + 1}: {xcor}")
        new_segment.setpos(xcor, 0)
        snake.append(new_segment)
        # print(f"snake now has {len(snake)} segments!")

def get_body_segment():
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    return new_segment

snake = []
for _ in range(3):
    add_body_segment()

# for body_segment in snake:
#     body_segment.fd(20)

screen.exitonclick()