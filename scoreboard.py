from turtle import Turtle

ALIGN = "center"
COLOUR = "white"
FONT = ("Courier", 16, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color(COLOUR)
        self.hideturtle()
        self.penup()
        self.setpos(0, 275)
        self.display_current_score()

    def display_current_score(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.display_current_score()

    def display_final_score(self):
        self.home()
        self.clear()
        self.write(f"GAME OVER! FINAL SCORE: {self.score}", align=ALIGN, font=FONT)