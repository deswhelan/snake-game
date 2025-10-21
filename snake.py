from turtle import Turtle

def get_body_segment():
    """Creates and returns a new body segment"""
    new_segment = Turtle("square")
    new_segment.color("white")
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

    # TODO: stretch - refactor "turn" methods into one take an "orientation" argument
    # TODO: check for valid turns (e.g. cannot turn south if currently facing north)
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