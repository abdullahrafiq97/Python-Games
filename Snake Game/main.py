from turtle import Screen
from snake import Snake
from food import Food
from Score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

curr = 0
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        curr+=1
        snake.grow()
        food.refresh()
        score.track_score(current=curr)

    if snake.head.xcor()>290 or snake.head.xcor() < -290 or snake.head.ycor() >290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    for segs in snake.segments[1:]:
        if snake.head.distance(segs) < 15:
            game_is_on=False
            score.game_over()




screen.exitonclick()