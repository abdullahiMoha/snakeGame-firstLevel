from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time

# setting up screen related things
screen = Screen()
screen.setup(height = 600, width = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# creating the snake and its food
snake = Snake()
food = Food()
score = Scoreboard()

# Game Manager Variable
is_game_on = True


# Stopping the game by a keypress
def stop_game():
    global is_game_on
    is_game_on = False


# listening the user action to know where he is going to
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(stop_game, "s")

# running the game
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detecting if the snake eat the food
    if snake.head.distance(food) < 15:
        food.refresh()  # refreshing the food position
        snake.extend()  # growing the snakes
        score.increase_score()  # increasing the game score

    # Detect the collision of snake to the wall snake.is_head_hit_wall()
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        # is_game_on = False
        score.reset_score()
        snake.rest_snake()

    # detecting if the hits its self
    for segment in snake.snake[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            # is_game_on = False
            score.reset_score()
            snake.rest_snake()

screen.exitonclick()  # it allows us the screen to be visible until we close it
