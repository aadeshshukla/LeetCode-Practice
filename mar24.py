# python code to print the calendar of a given month and year
# using the calendar module 
import calendar
# take month and year input from the user
yy = int(input("Enter year: ")) 
mm = int(input("Enter month: "))
# display the calendar
print(calendar.month(yy, mm))
