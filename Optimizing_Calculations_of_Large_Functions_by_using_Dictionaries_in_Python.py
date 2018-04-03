# File: Optimizing_Calculations_of_Large_Functions_by_using_Dictionaries_in_Python.py
# Description: Optimizing Calculations of Large Functions by using Dictionaries in Python
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Optimizing Calculations of Large Functions by using Dictionaries in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Optimizing_Calculations_of_Large_Functions_by_using_Dictionaries_in_Python (date of access: XX.XX.XXXX)

# Program are being used for the large functions f() not to repeat the calculations but store them in the dictionary
# It is called Optimizing of Calculations

# Example of the function - it is needed to implememnt the task but in real can be with large calculations
def f(x):
    return x + 1

# Creating an empty dictionary
d = {}

# Function to return already calculated value or update dictionary and return new one 
def update(d, key):
    if key in d:
        print(d[key])  # Showing the result without calculating large function f(x)
    else:
        d[key] = f(key)  # Updating value for the Key = key in dictionary
        print(d[key])

# Implementing results
n = int(input())  # Howmany times we're going to input values
for i in range(n):
    x = int(input())  # Imputing values
    update(d, x)  # Showing results
 
    
