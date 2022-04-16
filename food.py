from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.color("Blue")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.speed("fastest")
        self.new_location()

    def new_location(self):
        cord_x = random.randint(0, 210)
        cord_y = random.randint(0, 210)
        self.goto(x=cord_x, y=cord_y)