from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.setspeed = 0.1
    def move(self):
        newx = self.xcor()+self.x_move
        newy = self.ycor()+self.y_move
        self.goto(newx,newy)
    def bounce_y(self):
        self.y_move *=  -1

    def bounce_x(self):
        self.x_move *= -1

    def origin(self):
        self.goto(0,0)
        self.setspeed = 0.1
        self.bounce_x()