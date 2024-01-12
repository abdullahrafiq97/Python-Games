# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 13:21:31 2024

@author: Abdullah
"""
from art import logo

import random
def get_num():
    """Gets you a random number between 1 and 100"""
    number=random.randint(1, 100)
    return number


def compare(benchmark,guess):
    if benchmark>guess:
        return 'low'
    elif benchmark<guess:
        return 'high'
    else:
        return 'correct'



def game():
    print("Welcome to Roulette by Abdullah Rafiq!")
    game_over = False
    difficulty = input('Choose a difficulty between Easy, Medium or Hard: ')
    if difficulty == 'Easy' or difficulty == 'easy':
        lives = 10
    elif difficulty == 'Medium' or difficulty == 'medium':
        lives = 7
    elif difficulty == 'Hard' or 'hard':
        lives = 5
    print(f"In {difficulty} difficulty, you get {lives} tries to guess the number!")
    benchmark = get_num()
    while not game_over and lives>0:
        
        guess = int(input("Guess a number between 1 and 100: "))
        result = compare(benchmark, guess)
        if result == 'low':
            print("Your guess is too low!")
            lives-=1
            if lives == 0:
                print('You are out of tries. You lose!')
            else:
                print(f"You have {lives} tries left")
        elif result == 'high':
            print('Your guess is too high!')
            lives-=1
            if lives == 0:
                print('You are out of tries. You lose!')
            else:
                print(f"You have {lives} tries left")
            
            
        else:
            print('Bingo! You win!')
            game_over= True
Play_again = True
while Play_again:
    print (logo)
    game()
    print("Thank you for playing roulette by Abdullah Rafiq!")
    again=input("Do you want to play again? Yes or No: ")
    if again=='Yes' or again == 'yes':
        game()
    elif again == 'No' or again == 'no':
        Play_again = False