import turtle
import random
turtle.colormode(255)
colors =  [(224, 233, 227), (207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78), (80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169)]

y = -50
for u in range (10):
    y+=50
    turtle.penup()
    turtle.setposition(0.00, y)
    turtle.pendown()
    for i in range (10):
        turtle.dot(10, random.choice(colors))
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()

turtle.exitonclick()