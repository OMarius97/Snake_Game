from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x=0, y=220)
        self.hideturtle()
        self.score = 0
        self.highscore_truck()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}   High Score: {self.highscore}", move=False, align="Center", font=("Arial", 15, "normal"))

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write(arg="Game Over", move=False, align="Center", font=("Arial", 15, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()

    def increse_score(self):
        self.score += 1
        self.update_scoreboard()

    def highscore_truck(self):
        with open("data.txt") as file:
            self.highscore = int(file.read())
