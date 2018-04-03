# Program are bein used for the large functions f() not to repeat the calculations but store them in the dictionary
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
 
    
