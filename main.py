from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600,width=800)
screen.bgcolor('black')
screen.title('Pong!')
screen.tracer(0)

ball = Ball()
scoreboard = Scoreboard()

l_paddle = Paddle(('L'))
r_paddle = Paddle(('R'))

screen.listen()
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    if ball.xcor() > 340:
        scoreboard.l_point()
        ball.refresh()
    elif ball.xcor() < -340:
        scoreboard.r_point()
        ball.refresh()


screen.exitonclick()