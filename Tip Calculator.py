# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 00:13:07 2024

@author: Abdullah
"""

bill = input('What is your bill?')
People = input('How many people?')
tip = input('What percentage of tip would you like to give?')

Cont = ((float(bill))*(1+float(tip)/100))/int(People)

print(f'Each person shuould pay {Cont}')
