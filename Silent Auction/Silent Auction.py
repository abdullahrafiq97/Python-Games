# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 00:11:24 2024

@author: Abdullah
"""


from art import logo
import os

auction_dict = {}
def auction(name, bid):
  auction_dict[name] = bid

new=True

print("Welcome to the silent auction hosted by Mr. Abdullah Rafiq!")
print(logo)
name = input("What is your name? ")
bid = int(input("What is your bid?: $"))
auction(name, bid)

while new:
  
  Bidder = input("Are there any more bidders? Type yes on no: ")
  if Bidder == "yes":
    os.system('cls')
    print("Welcome to the silent auction hosted by Mr. Abdullah Rafiq!")
    print(logo)
    name = input("What is your name? ")
    bid = int(input("What is your bid?: $"))
    auction(name, bid)
  if Bidder == "no":
    new = False

Highest_bid = 0
for key in auction_dict:
  if auction_dict[key] > Highest_bid:
    Highest_bid = auction_dict[key]

Highest_Bidder= list(auction_dict.keys())[list(auction_dict.values()).index(Highest_bid)]


print(f'{Highest_Bidder} won the auction at ${Highest_bid}')