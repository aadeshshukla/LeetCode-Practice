# python code to print the calendar of a given month and year
# using the calendar module 
import calendar
# take month and year input from the user
yy = int(input("Enter year: ")) 
mm = int(input("Enter month: "))
# display the calendar
print(calendar.month(yy, mm))

# lets learn more about different modules in python
# we can use the datetime module to work with dates and times
import datetime
# get the current date and time
now = datetime.datetime.now()
print("Current date and time: ")
print(now)
# we can also create a date object
date = datetime.date(2024, 3, 24)
print("The date is: ")
print(date)
# we can also create a time object
time = datetime.time(12, 30, 45)
print("The time is: ")
print(time)
# we can also create a datetime object
datetime_obj = datetime.datetime(2024, 3, 24, 12, 30, 45)
print("The datetime is: ")
print(datetime_obj)
# we can also format the date and time
formatted_date = now.strftime("%Y-%m-%d")
formatted_time = now.strftime("%H:%M:%S")
print("Formatted date: ")
print(formatted_date)
print("Formatted time: ")
print(formatted_time)

# others modules we can learn about are os, sys, math, random, etc.
# the os module provides a way of using operating system dependent functionality
import os
# get the current working directory
cwd = os.getcwd()
print("Current working directory: ")
print(cwd)
# change the current working directory
os.chdir('/home/user/Documents')
print("Current working directory after change: ")
print(os.getcwd())
# the sys module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter
import sys
# get the version of python
print("Python version: ")
print(sys.version)
# the math module provides access to the mathematical functions defined by the C standard
import math
# get the value of pi
print("Value of pi: ")
print(math.pi)
# get the value of e
print("Value of e: ")
print(math.e)
# the random module implements pseudo-random number generators for various distributions
import random
# get a random number between 0 and 1
print("Random number between 0 and 1: ")
print(random.random())
# get a random integer between 1 and 10
print("Random integer between 1 and 10: ")
print(random.randint(1, 10))
