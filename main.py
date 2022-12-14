import time
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

screen = Screen()
ball = Ball()
l_player = Paddle(-350,0)
r_player = Paddle(350,0)
scoreboard = Scoreboard()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()
screen.onkey(r_player.up, "Up")
screen.onkey(r_player.down," Down")
screen.onkey(l_player.up,"w")
screen.onkey(l_player.down,"s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with top
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_player) < 50 and ball.xcor() > 320 or ball.distance(l_player) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect r paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect l paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()

