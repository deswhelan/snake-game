from turtle import Turtle

# TODO: implement a snake class
def get_body_segment():
    """Creates and returns a new body segment"""
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    return new_segment

class Snake(list):
    def __init__(self):
        self.create_starting_snake()

    def create_starting_snake(self):
        """Initialise snake of length 3X body segments"""
        for _ in range(3):
            self.add_body_segment()

    def add_body_segment(self):
        """Adds a new body segment to the snake"""
        if len(self) == 0:
            self.append(get_body_segment())
        else:
            new_segment = get_body_segment()
            # TODO: account for current direction
            xcor = (self[len(self) - 1].xcor() - 20)
            new_segment.setpos(xcor, 0)
            self.append(new_segment)

    def move(self):
        """Moves the snake smoothly and continuously forwards"""
        for idx, body_segment in enumerate(reversed(self)):
            # if current body segment is the head, move it forward
            if idx == (len(self) - 1):
                body_segment.fd(20)
            # otherwise, move segment to the current position of the segment immediately in front of it
            else:
                body_segment.goto(self[-idx + 1].pos())
