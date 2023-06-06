'''
Start of the EXCEPTION class

05/06/2023 (1/2 hour)
Start: Introduction
End: else
'''

#SyntaxError is an error in the writing of your code. Now we gonna learn to use Try

try:
    x = int(input("What's the x? "))
    print(f"x is {x}")
except ValueError:
    print("X is not an integer")

#if you want to call an variable defined inside a try, you have to do this:
try:
    x = int(input("What's the x? "))
except ValueError:
    print("X is not an integer")
else:
print(f"x is {x}")

