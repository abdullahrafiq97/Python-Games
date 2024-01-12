# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 11:45:16 2024

@author: Abdullah
"""

from utility import logo, stages
import os
def Hangman(chosen_word):
  
  
  word=[]
  for letter in chosen_word:
    word.append('_')
  print(word)
  
  lives=6
  Gameover = False
  while not Gameover:
    guess= input('Guess a letter: ').lower()
    if guess in word:
      print('You have already guessed this letter')
    elif guess in chosen_word:
      for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
          word[i]=guess
    else:
      lives-=1
      print(guess + ' is not in the word. You lose a life')
    
    print(word)
    print(stages[lives])
    if '_' not in word:
      Gameover = True
      word.clear()
      print('You win')
    elif lives == 0:
      Gameover = True
      word.clear()
      print('You lose.'+' The word is ' + chosen_word)

Play_game = True
while Play_game:
  print("Welcome to Hangman by Abdullah Rafiq!")
  print('Player 1 turn')
  print(logo)
  chosen_word = input("What word would you like to give to your opponent? ")
  HintAsk = input("Do you want to give any hint? Type Y or N: ")
  if HintAsk == 'Y' or HintAsk=='y':
      Hint = input("What is the hint? ")
  else:
      Hint = 'No hint provided'
  
  os.system('cls')
    
  print("Welcome to Hangman by Abdullah Rafiq!")
  print('Player 2 turn')
  print(logo)
  print(Hint)
  Hangman(chosen_word)
  Play_again = input('Do you want to play again? Type "yes" or "no": ').lower()
  if Play_again == 'no':
    Play_game = False
    print('Thanks for playing Hangman by Abdullah Rafiq!')