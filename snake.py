from turtle import Turtle

COLOUR = "white"
SHAPE = "square"

def get_body_segment():
    """Creates and returns a new body segment"""
    new_segment = Turtle(SHAPE)
    new_segment.color(COLOUR)
    new_segment.penup()
    return new_segment

class Snake(list):
    def __init__(self):
        super().__init__()
        self.create_starting_snake(length=3)
        self.head = self[0]

    def create_starting_snake(self, length):
        """Creates a new snake of specified length"""
        self.append(get_body_segment())
        for _ in range(length - 1):
            self.add_body_segment()

    def add_body_segment(self):
        """Adds a new body segment to the end of the snake"""
        new_segment = get_body_segment()
        # TODO: account for current direction
        xcor = (self[len(self) - 1].xcor() - 20)
        new_segment.setpos(xcor, 0)
        self.append(new_segment)

    def move(self):
        """Moves the snake forwards by 20 steps"""
        for idx, body_segment in enumerate(reversed(self)):
            # if current body segment is the head, move it forward
            if idx == (len(self) - 1):
                body_segment.fd(20)
            # otherwise, move segment to the current position of the segment immediately in front of it
            else:
                body_segment.goto(self[-idx + 1].pos())

    # TODO: stretch - refactor "turn" methods into one metho which takes an "orientation" argument
    # TODO: stretch - handle bug where invalid turns allowed if two turns performed quickly (e.g. face_east+face_south when heading north)
    def face_north(self):
        if self.head.heading() == 270:
            return
        self.head.setheading(90)

    def face_south(self):
        if self.head.heading() == 90:
            return
        self.head.setheading(270)

    def face_east(self):
        if self.head.heading() == 180:
            return
        self.head.setheading(0)

    def face_west(self):
        if self.head.heading() == 0:
            return
        self.head.setheading(180)

    # TODO: clear snake on game over(?)