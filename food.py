import random
from turtle import Turtle

COLOUR = "blue"
SHAPE = "circle"

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOUR)
        self.shapesize(0.5)
        self.penup()
        self.drop_food()

    def drop_food(self):
        """Drops a morsel of food in a random position on the screen"""
        self.setpos(random.randint(-290, 290), random.randint(-290, 290))
