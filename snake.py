from turtle import Turtle

COLOUR = "white"
SHAPE = "square"

NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

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
        current_tail = self[-1]
        current_tail_direction = current_tail.heading()

        new_segment = get_body_segment()
        new_segment.setheading(current_tail_direction)

        if current_tail_direction == NORTH:
            new_segment.setpos(current_tail.xcor(), current_tail.ycor() - 20)
        elif current_tail_direction == SOUTH:
            new_segment.setpos(current_tail.xcor(), current_tail.ycor() + 20)
        elif current_tail_direction == EAST:
            new_segment.setpos(current_tail.xcor() - 20, current_tail.ycor())
        elif current_tail_direction == WEST:
            new_segment.setpos(current_tail.xcor() + 20, current_tail.ycor())

        self.append(new_segment)

    def move(self):
        """Moves the snake forwards by 20 steps"""
        # Move each segment (except the head) to the position of the segment in front
        for x in range((len(self) - 1), 0, -1):
            self[x].goto(self[x - 1].pos())
            # Update the direction of the segment to the direction of the segment in front
            self[x].setheading(self[x - 1].heading())
        self.head.fd(20)

    # TODO: stretch - refactor "turn" methods into one metho which takes an "orientation" argument
    # TODO: stretch - handle bug where invalid turns allowed if two turns performed quickly (e.g. face_east+face_south when heading north)
    def face_north(self):
        if self.head.heading() == SOUTH:
            return
        self.head.setheading(NORTH)

    def face_south(self):
        if self.head.heading() == NORTH:
            return
        self.head.setheading(SOUTH)

    def face_east(self):
        if self.head.heading() == WEST:
            return
        self.head.setheading(EAST)

    def face_west(self):
        if self.head.heading() == EAST:
            return
        self.head.setheading(WEST)

    # TODO: clear snake on game over(?) and/or reset(?)