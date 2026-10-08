import math
import random
from turtle import Screen, Shape, Turtle

# Food faces north so that shape coordinates map directly onto screen coordinates
FACING = 90


def circle_points(centre_x, centre_y, radius_x, radius_y=None, points=16):
    """Returns the points of a circle (or ellipse) as a polygon"""
    if radius_y is None:
        radius_y = radius_x
    return tuple(
        (centre_x + radius_x * math.cos(2 * math.pi * i / points),
         centre_y + radius_y * math.sin(2 * math.pi * i / points))
        for i in range(points)
    )


def make_shape(components):
    """Builds a multi-coloured turtle shape from (polygon, fill, outline) components"""
    shape = Shape("compound")
    for polygon, fill, outline in components:
        shape.addcomponent(polygon, fill, outline)
    return shape


FRUITS = {
    "apple": make_shape([
        (circle_points(0, -1, 8), "red", "dark red"),
        (((-1, 6), (1, 6), (2, 11), (0, 11)), "saddle brown", "saddle brown"),
        (((1, 9), (5, 12), (8, 10), (4, 8)), "green", "dark green"),
    ]),
    "orange": make_shape([
        (circle_points(0, 0, 8), "orange", "dark orange"),
        (((0, 7), (3, 11), (6, 10), (3, 7)), "green", "dark green"),
    ]),
    "banana": make_shape([
        (((-10, 4), (-6, -2), (0, -5), (6, -3), (10, 2), (6, 0), (0, -1), (-6, 2)), "yellow", "goldenrod"),
        (((9, 1), (10, 2), (11, 5), (10, 5)), "saddle brown", "saddle brown"),
    ]),
    "cherries": make_shape([
        (((-4, -4), (-3, -4), (2, 9), (1, 9)), "dark green", "dark green"),
        (((4, -3), (5, -3), (2, 9), (1, 9)), "dark green", "dark green"),
        (circle_points(-4, -5, 4.5), "crimson", "dark red"),
        (circle_points(5, -4, 4.5), "crimson", "dark red"),
    ]),
    "grapes": make_shape([
        (((0, 6), (1, 6), (1, 11), (0, 11)), "saddle brown", "saddle brown"),
        (circle_points(-4, 4, 3.5), "purple", "indigo"),
        (circle_points(3, 4, 3.5), "purple", "indigo"),
        (circle_points(-1, -1, 3.5), "purple", "indigo"),
        (circle_points(6, -1, 3.5), "purple", "indigo"),
        (circle_points(-7, -1, 3.5), "purple", "indigo"),
        (circle_points(2, -6, 3.5), "purple", "indigo"),
        (circle_points(-4, -6, 3.5), "purple", "indigo"),
    ]),
    "strawberry": make_shape([
        (((-8, 4), (8, 4), (5, -5), (0, -10), (-5, -5)), "red", "dark red"),
        (((-7, 4), (-3, 8), (0, 5), (3, 8), (7, 4)), "green", "dark green"),
    ]),
    "lemon": make_shape([
        (circle_points(0, 0, 9, 6.5), "yellow", "gold"),
        (circle_points(9, 0, 2, 1.5, points=8), "gold", "gold"),
    ]),
    "watermelon": make_shape([
        (((-10, 4), (10, 4), (7, -3), (0, -6), (-7, -3)), "green", "dark green"),
        (((-8, 4), (8, 4), (5, -2), (0, -4), (-5, -2)), "tomato", "tomato"),
        (((-3, 1), (-2, 1), (-2.5, -1)), "black", "black"),
        (((2, 1), (3, 1), (2.5, -1)), "black", "black"),
    ]),
}


def register_fruit_shapes():
    """Registers every fruit shape with the screen so turtles can use them"""
    screen = Screen()
    for name, shape in FRUITS.items():
        screen.register_shape(name, shape)


class Food(Turtle):
    def __init__(self):
        super().__init__()
        register_fruit_shapes()
        self.setheading(FACING)
        self.penup()
        self.drop_food()

    def drop_food(self):
        """Drops a random piece of fruit in a random position on the screen"""
        self.shape(random.choice(list(FRUITS)))
        self.setpos(random.randint(-290, 290), random.randint(-290, 290))
