# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 03:55:33 2024

@author: Abdullah
"""

from game_data import data
from art import logo, vs
import random
import os
continue_game = True

def compare(a,b):
  if a["follower_count"] > b["follower_count"]:
    return a
  else:
    return b

def check(guess, answer):
  if guess == answer:
    return True
  else:
    return False
    
a = random.choice(data)
score=0
while continue_game:
  
  b = random.choice(data)
  print("Welcome to Higher Lower Game by Abdullah Rafiq!\nThe goal of this game is to guess which of the two celebrities has more followers on Instagram.\nGood luck!")
  print(logo)
  higher = compare(a, b)
  
  guess = input(f"Compare A: {a['name']}, a {a['description']}, from {a['country']} \n {vs} \n Against B: {b['name']}, a {b['description']}, from {b['country']}. \n Who has more followers? Type 'A' or 'B': ").lower()
  if guess == "a":
    guess = a
  elif guess == "b":
    guess = b
  
  answer = check(guess['name'], higher['name'])
  if answer == True:
    os.system('cls')
    print(f"You're right! Current score: {score}")
    a = higher
    score+=1
  elif answer == False:
    continue_game = False
    print(f"Sorry, that's wrong. Final score: {score}")
  
  