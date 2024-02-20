from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()

    def track_score(self, current):
        self.clear()
        self.penup()
        self.goto((0, 270))
        self.color('white')
        self.hideturtle()
        self.write(arg = f"Score: {current}", move=False, align='center', font=('Arial', 14, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over", move=False, align='center', font=('Arial', 24, 'bold'))