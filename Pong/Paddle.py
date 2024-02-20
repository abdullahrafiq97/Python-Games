from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, xcor):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(xcor, 0)

    def goup(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    def godown(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)