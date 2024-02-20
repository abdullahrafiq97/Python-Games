import turtle
tim = turtle.Turtle()
screen = turtle.Screen()

def forward():
    tim.forward(5)

def backward():
    tim.back(5)

def clock():
    tim.right(10)

def antic():
    tim.left(10)

def clear():
    tim.clear()
    tim.home()
    tim.clear()

def obidient_turtle():
    screen.listen()
    screen.onkey(forward, "W")
    screen.onkey(backward, "S")
    screen.onkey(clock, "D")
    screen.onkey(antic, "A")
    screen.onkey(clear, "C")
obidient_turtle()
screen.exitonclick()