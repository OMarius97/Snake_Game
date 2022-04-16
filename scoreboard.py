from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x=0, y=220)
        self.hideturtle()
        self.score = 0
        self.write(arg=f"Score: {self.score}", move=False, align="Center", font=("Arial", 15, "normal"))

    def points(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align="Center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="Game Over", move=False, align="Center", font=("Arial", 15, "normal"))