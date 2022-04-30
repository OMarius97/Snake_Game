from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("Black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")

food = Food()
scoreboard = Scoreboard()
game_on = True


while game_on is True:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.new_location()
        snake.tail()
        scoreboard.increse_score()


    # Detect collision with wall
    if snake.head.xcor() > 230 or snake.head.xcor() < -230 or snake.head.ycor() > 230 or snake.head.ycor() < -230:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for element in snake.parts[1:]:
        if snake.head.distance(element) < 10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()
