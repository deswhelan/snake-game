from turtle import Screen, Shape, Turtle

from food import circle_points

SHAPE = "snake_body"
HEAD_SHAPE = "snake_head"
HEAD_TONGUE_SHAPE = "snake_head_tongue"
STARTING_LENGTH = 3

SCALE_COLOUR = "#9c7f4a"
SCALE_OUTLINE = "#6b5530"
DIAMOND_COLOUR = "#4a3320"
DIAMOND_CENTRE_COLOUR = "#d8c48c"

RATTLE_SHAPE = "rattle"
# How far (in degrees) the rattle shakes from side to side as the snake moves
RATTLE_SHAKE = 20

NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

def get_body_segment():
    """Creates and returns a new body segment"""
    new_segment = Turtle(SHAPE)
    new_segment.penup()
    return new_segment

def make_head_shape(with_tongue):
    """Builds a rattlesnake head, pointing in the segment's heading (+y)"""
    head = Shape("compound")
    if with_tongue:
        head.addcomponent(((-0.7, 9), (0.7, 9), (0.7, 15), (3, 18), (2, 18.5), (0, 16),
                           (-2, 18.5), (-3, 18), (-0.7, 15)), "red", "red")
    head.addcomponent(((-8, -10), (8, -10), (10, -2), (8, 6), (3, 10), (-3, 10), (-8, 6), (-10, -2)),
                      SCALE_COLOUR, SCALE_OUTLINE)
    head.addcomponent(((-4, -9), (4, -9), (0, 0)), DIAMOND_COLOUR, DIAMOND_COLOUR)
    for side in (-1, 1):
        head.addcomponent(circle_points(side * 5, 3, 2.2, points=8), "gold", "black")
        head.addcomponent(((side * 5 - 0.5, 1), (side * 5 + 0.5, 1), (side * 5 + 0.5, 5), (side * 5 - 0.5, 5)),
                          "black", "black")
        head.addcomponent(circle_points(side * 1.8, 8, 0.6, points=6), "black", "black")
    return head

def register_snake_shapes():
    """Registers the head, body and rattle shapes, each pointing in the segment's heading (+y)"""
    screen = Screen()
    screen.register_shape(HEAD_SHAPE, make_head_shape(with_tongue=False))
    screen.register_shape(HEAD_TONGUE_SHAPE, make_head_shape(with_tongue=True))

    # Slightly longer than the 20 step spacing so neighbouring segments overlap into one body
    body = Shape("compound")
    body.addcomponent(((-7, -11), (7, -11), (9, -8), (9, 8), (7, 11), (-7, 11), (-9, 8), (-9, -8)),
                      SCALE_COLOUR, SCALE_COLOUR)
    body.addcomponent(((0, 9), (8, 0), (0, -9), (-8, 0)), DIAMOND_COLOUR, SCALE_OUTLINE)
    body.addcomponent(((0, 4.5), (4, 0), (0, -4.5), (-4, 0)), DIAMOND_CENTRE_COLOUR, DIAMOND_CENTRE_COLOUR)
    screen.register_shape(SHAPE, body)

    rattle = Shape("compound")
    rattle.addcomponent(circle_points(0, 6, 7, 4.5), "burlywood", "saddle brown")
    rattle.addcomponent(circle_points(0, 0, 6, 4), "tan", "saddle brown")
    rattle.addcomponent(circle_points(0, -5.5, 5, 3.5), "burlywood", "saddle brown")
    rattle.addcomponent(circle_points(0, -10, 3.5, 2.5), "tan", "saddle brown")
    screen.register_shape(RATTLE_SHAPE, rattle)

class Snake(list):
    def __init__(self):
        super().__init__()
        register_snake_shapes()
        self.rattle_tilt = RATTLE_SHAKE
        self.create_starting_snake(length=STARTING_LENGTH)
        self.head = self[0]

    def create_starting_snake(self, length):
        """Creates a new snake of specified length"""
        head = get_body_segment()
        head.shape(HEAD_SHAPE)
        self.append(head)
        for _ in range(length - 1):
            self.add_body_segment()

    def update_rattle(self):
        """Gives the tail segment a rattle, and turns any previous rattle back into a body segment"""
        for body_segment in self[1:-1]:
            if body_segment.shape() == RATTLE_SHAPE:
                body_segment.shape(SHAPE)
                body_segment.tiltangle(0)
        self[-1].shape(RATTLE_SHAPE)

    def shake_rattle(self):
        """Shakes the rattle from side to side"""
        self.rattle_tilt = -self.rattle_tilt
        self[-1].tiltangle(self.rattle_tilt)

    def flick_tongue(self):
        """Flicks the tongue in and out"""
        if self.head.shape() == HEAD_SHAPE:
            self.head.shape(HEAD_TONGUE_SHAPE)
        else:
            self.head.shape(HEAD_SHAPE)

    # TODO: stretch - refactor so that current tail is simply duplicated in the same position (i.e. don't worry about direction) ?
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
        self.update_rattle()

    def move(self):
        """Moves the snake forwards by 20 steps"""
        # Move each segment (except the head) to the position of the segment in front
        for x in range((len(self) - 1), 0, -1):
            self[x].goto(self[x - 1].pos())
            # Update the direction of the segment to the direction of the segment in front
            self[x].setheading(self[x - 1].heading())
        self.head.fd(20)
        self.shake_rattle()
        self.flick_tongue()

    # TODO: stretch - refactor "turn" methods into one method which takes an "orientation" argument
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

    def head_has_hit_body(self):
        # Do not include head in this check
        for body_segment in self[1:]:
            if self.head.distance(body_segment) < 15:
                return True
        return False

    # TODO:
    def reset_game(self):
        for body_segment in self:
            body_segment.goto(1000, 1000)
        self.clear()
        self.create_starting_snake(STARTING_LENGTH)
        self.head = self[0]


    # TODO: clear snake on game over(?) and/or reset(?)