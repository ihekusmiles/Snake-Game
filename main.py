from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Create screen and adjust paremeters
screen = Screen()
screen.setup(width=610, height=610)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Create Snake Game objects: Snake, Food, Scoreboard 
snake = Snake()
food = Food()
score = Scoreboard()

# Event listeners eg. onkey, to listen to user key presses
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Set a while loop and setting it up to True to keep the game running
while True:
    # Allow the screen to update and sleep while moving the snake segments
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        score.increase_score()
        food.refresh()
        snake.extend()
    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
    # Detect collision tail with segment or wall, then reset game
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()

