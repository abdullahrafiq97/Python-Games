# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 00:08:46 2024

@author: Abdullah
"""

def add(a, b):
  result=a+b
  return result
def sub(a, b):
  result=a-b
  return result
def mul(a, b):
  result=a*b
  return result
def div(a, b):
  result=a/b
  return result

operations = {
  '+':add,
  '-':sub,
  '*':mul,
  '/':div
}
import os
def calculator():
  os.system('clear')
  first_number=float(input("Enter the first number: "))
  for symbol in operations:
    print(symbol)

  should_continue=True
  while should_continue:
    operation=input("Pick an operation: ")
    second_number=float(input("Enter the next number: "))
    operate=operations[operation]
    answer=operate(first_number, second_number)
    print(f"{first_number} {operation} {second_number} = {answer}")
    ask=input(f"Type 'y' to continue calculating with {answer}, type 'n' to start over, or type e to exit: ")
    if ask == 'y':
      first_number=answer
    elif ask == 'e':
      print('Thank you for using the Abdullah Rafiq calculator!')
      should_continue=False
    elif ask == 'n':
      should_continue=False
      calculator()
calculator()