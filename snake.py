from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]


    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        snake_part = Turtle("square")
        snake_part.color("white")
        snake_part.speed("fastest")
        snake_part.penup()
        snake_part.setposition(position)
        self.parts.append(snake_part)

    def tail(self):
        self.add_segment(self.parts[-1].position())

    def move(self):
        for segment in range(len(self.parts) - 1, 0, -1):
            new_x = self.parts[segment - 1].xcor()
            new_y = self.parts[segment - 1].ycor()
            self.parts[segment].goto(new_x, new_y)
        self.head.forward(20)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def reset(self):
        for segment in self.parts:
            segment.hideturtle()
        self.parts.clear()
        self.create_snake()
        self.head = self.parts[0]