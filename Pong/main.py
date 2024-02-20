from turtle import Turtle, Screen
from Paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(height=600,width=1000)
screen.title("Pong by Abdullah")

r_paddle = Paddle(xcor=-350)
l_paddle = Paddle(xcor=350)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.goup,"W")
screen.onkey(r_paddle.godown,"S")
screen.onkey(l_paddle.goup,"Up")
screen.onkey(l_paddle.godown,"Down")

game = True
while game:
    time.sleep(ball.setspeed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor()<-280:
        ball.bounce_y()
    if ball.distance(l_paddle)<50 and ball.xcor() > 320 or ball.distance(r_paddle)<50 and ball.xcor() < -320:
        ball.setspeed *= 0.9
        ball.bounce_x()
    if ball.xcor() > 380:
        score.l_point()
        ball.origin()
    if ball.xcor() < -380:
        score.r_point()
        ball.origin()


screen.exitonclick()