import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(0.5)
        self.penup()
        self.drop_food()

    def drop_food(self):
        """Drops a morsel of food in a random position on the screen"""
        self.setpos(random.randint(-290, 290), random.randint(-290, 290))
