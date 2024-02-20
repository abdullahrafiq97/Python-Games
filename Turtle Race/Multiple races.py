import turtle
import random
from utility import MyTurtleRace

rec = MyTurtleRace()

screen = turtle.Screen()
screen.setup(500,400)
colors = ['red', 'blue', 'green', 'purple', 'pink', 'orange']
is_race_on = False
all_turtles = []


rec.createturtles(list=all_turtles,colors=colors)

rec.race(list=all_turtles)




screen.exitonclick()

