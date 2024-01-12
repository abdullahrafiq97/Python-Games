# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 00:09:43 2024

@author: Abdullah
"""

def leap_year(year):
  """Tells you if the year is a leap year or not"""
  if year%4==0:
    if year%100==0:
      if year%400==0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year,month):
  """Tells you the number of days in a month"""
  days=[31,28,31,30,31,30,31,31,30,31,30,31]
  if (leap_year(year)):
    days[1]=29
  return days[month-1]

print(days_in_month(year=int(input("Enter a year: ")),month=int(input("Enter a month: "))))
