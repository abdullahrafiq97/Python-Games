# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 00:17:14 2024

@author: Abdullah
"""

from utility import logo, stages, word_list



def Hangman():
  import random
  chosen_word = random.choice(word_list)
  word_list.remove(chosen_word)
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
  print("Welcome to Hangman!")
  print(logo)
  Hangman()
  Play_again = input('Do you want to play again? Type "yes" or "no": ').lower()
  if Play_again == 'no':
    Play_game = False
    print('Thanks for playing Hangman by Abdullah Rafiq!')
        
  
  
  
  
  
  
  
  

  

    