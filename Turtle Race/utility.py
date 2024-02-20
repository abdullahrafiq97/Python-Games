import turtle
import random

class MyTurtleRace:
    def createturtles(self, list, colors):
        xcor = 0
        ycor = -150
        for turtles in range(0, 6):
            timmy = turtle.Turtle(shape='turtle')
            list.append(timmy)
            timmy.penup()
            timmy.color(colors[xcor])
            timmy.goto(-230, ycor)
            xcor += 1
            ycor += 50

    def race(self, list):
        p = MyTurtleRace()
        ycor = -150
        userbet = turtle.Screen().textinput("Make your bet on the Turtle Race!", "Which turtle will win the race? Enter a color: ")
        is_race_on = True
        while is_race_on:
            for turtles in list:
                if turtles.xcor() > 230:
                    is_race_on = False
                    winner = turtles.pencolor()
                    if winner == userbet:
                        again =turtle.Screen().textinput("Game over!", f"You won the bet. The winner is {winner} colored turtle! Would you like to play again? ")
                        if again =='yes':
                            for turtles in list:
                                turtles.goto(-230, ycor)
                                ycor += 50
                            p.race(list=list)

                    else:
                        again = turtle.Screen().textinput("Game over!",
                                                          f"Sorry! Hard luck. The winner is {winner} colored turtle! Would you like to play again? ")
                        if again == 'yes':
                            for turtles in list:
                                turtles.goto(-230, ycor)
                                ycor += 50
                            p.race(list=list)


                rand_dist = random.randint(0, 10)
                turtles.forward(rand_dist)