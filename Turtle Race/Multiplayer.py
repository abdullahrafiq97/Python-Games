import turtle
import random


class MyTurtleRace:
    def create_turtles(self, colors):
        turtles_list = []
        xcor = 0
        ycor = -150
        for turtles in range(0, 6):
            timmy = turtle.Turtle(shape='turtle')
            turtles_list.append(timmy)
            timmy.penup()
            timmy.color(colors[xcor])
            timmy.goto(-230, ycor)
            xcor += 1
            ycor += 50
        return turtles_list

    def player_registration(self):
        players_list = []
        number_of_players = int(turtle.Screen().textinput("Player Registration", "How many players are playing today?"))
        for _ in range(number_of_players):
            name = turtle.Screen().textinput("Player Registration", "What is the player's name?")
            bet = turtle.Screen().textinput("Make your bet on the Turtle Race!", f"Hi {name}. Which turtle will win the race? Enter a color: ")
            player_info = {'name': name, 'bet': bet.lower()}
            players_list.append(player_info)
        return players_list

    def race(self, turtles_list, players_list):
        ycor = -150
        is_race_on = True
        while is_race_on:
            for turtle_obj in turtles_list:
                if turtle_obj.xcor() > 230:
                    is_race_on = False
                    winner_color = turtle_obj.pencolor()
                    winners = [player_info['name'] for player_info in players_list if winner_color.lower() == player_info['bet'].lower()]
                    if winners:
                        again = turtle.Screen().textinput("Game Over!",
                                                          f"{', '.join(winners)} won the bet. The winner is {winner_color} colored turtle! Would you like to play again? ")
                    else:
                        again = turtle.Screen().textinput("Game Over!",
                                                          f"Sorry! Hard luck. The winner is {winner_color} colored turtle! Would you like to play again? ")

                    if again.lower() == 'yes':
                        for turtle_obj in turtles_list:
                            turtle_obj.goto(-230, ycor)
                            ycor += 50
                        players_list = self.player_registration()
                        self.race(turtles_list, players_list)
                    else:
                        return  # End the race if not playing again

                rand_dist = random.randint(0, 10)
                turtle_obj.forward(rand_dist)
