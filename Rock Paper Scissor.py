images= {'rock' : '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',

'paper' : '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',

'scissor' : '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''}

#Write your code below this line 👇
import random

choices = ['rock', 'paper', 'scissor']
yourchoice= input("What do you choose?")
print(images[yourchoice])
computerchoose = random.choice(choices)
print(f'Computer chooses {computerchoose}')
print(images[computerchoose])
if yourchoice == 'rock':
  if computerchoose == 'rock':
    print("It's a tie")
  elif computerchoose == 'paper':
    print ("You lose")
  elif computerchoose == 'scissor':
    print ("You win")
elif yourchoice == 'paper':
  if computerchoose == 'rock':
    print("You win")
  elif computerchoose == 'paper':
    print ("It's a tie")
  elif computerchoose == 'scissor':
    print ("You lose")
elif yourchoice == 'scissor':
  if computerchoose == 'rock':
    print("You lose")
  elif computerchoose == 'paper':
    print ("You win")
  elif computerchoose == 'scissor':
    print ("It's a tie")