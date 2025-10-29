import time
from turtle import Turtle

ALIGN = "center"
COLOUR = "white"
FONT = ("Courier", 16, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.color(COLOUR)
        self.hideturtle()
        self.penup()
        self.setpos(0, 275)
        self.display_current_score()

    @staticmethod
    def get_high_score():
        """Retrieves and returns the high score from the high score log"""
        with open("high_score_log.txt") as high_score_log:
            high_score = int(high_score_log.read())
        return high_score

    def display_current_score(self):
        self.clear()
        self.write(f"Score: {self.score}     High Score: {self.high_score}", align=ALIGN, font=FONT)

    def update_score(self):
        self.score += 1
        self.display_current_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score_log.txt", "w") as high_score_log:
                high_score_log.write(str(self.score))
        self.score = 0
        self.display_current_score()