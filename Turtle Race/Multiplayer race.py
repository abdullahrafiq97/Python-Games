import turtle
from Multiplayer import MyTurtleRace

rec = MyTurtleRace()

screen = turtle.Screen()
screen.setup(500,400)
colors = ['red', 'blue', 'green', 'purple', 'pink', 'orange']
is_race_on = False
all_turtles = rec.create_turtles(colors=colors)
players = rec.player_registration()

rec.race(turtles_list=all_turtles, players_list=players)




screen.exitonclick()

