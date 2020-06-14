"""
Program: TDD First Program.py
Author: Justin Protzman
Last date modified: 06/03/2020


Program specifications: The program will have will prompt for the age of one infant (age 1-5 years) who is attending camp and convert the age in months to years via a function call then print the result.

Write a program camper_age_input.py with a main function. (Name is important! If you are programming tasked with writing a script called x, and you call it y, other part of the program expecting x cannot run your code.)

Your computer is performing all four functions 1. store and input, 2. process and store, 3. output. More specifically


Store a numeric value in a variable age_in_years from input
Perform calculation, store answer in a variable age_in_months use symbolic constant years to  months conversion (in a function call convert_to_months()) that returns the value
Output the answer variable received from the function with meaning string to inform the user what the output means
"""
def convert_to_months(years):
    months = years*12
    return months

def age_in_years(years):
    age_in_years = years

if __name__ == '__main__':
    print (age_in_years, "years is", convert_to_months, "months")
# works for any number of years but for this it's only for 3-72
#calling this function can be hard
