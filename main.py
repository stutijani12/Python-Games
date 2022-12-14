import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
counter = 0
game_on = True



while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # detect collision between food and snake
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # detect collision with wall
    if snake.head.xcor()> 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:

        score.reset()
        snake.reset()

    # detect collision with tail
    for segment in range(len(snake.segments))[1:]:
        if snake.head.distance(snake.segments[segment]) < 10:
            score.reset()
            snake.reset()
screen.exitonclick()
