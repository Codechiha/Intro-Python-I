"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime
import time

# Still need to include some of the rules at the top regarding if 1 argument assume it is month and print
# Calendar of that month

valid_months = [
  'january', 'february', 'march', 
  'april', 'may', 'june', 'july', 
  'august', 'september', 'october', 
  'november', 'december', 
  'jan', 'feb', 'mar', 'apr', 'jun', 
  'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

try:
  month, year = input("Enter a month and a year(1900 - 2020): ").split()
except: 
  print("Pleae enter a valid Month and Year(1900 - 2020) \ne.g.: February 2020")
  print("The current Month and Year:", datetime.today().strftime("%B"), datetime.today().strftime("%Y"))
else: 
  if (len(month) > 0) and (1900 <= int(year) <= 2020):
      if month.lower() in valid_months:
        print('You entered', month.capitalize(), year)
      else: 
        print('You entered an invalid month')
  else:
    print("Pleae enter a valid Month and Year(1900 - 2020) \ne.g.: February 2020")
    print("The current Month and Year:", datetime.today().strftime("%B"), datetime.today().strftime("%Y"))
