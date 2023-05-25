
'''
24/05/2023 (xx minutes)
Start: Introduction
End: 
'''

#Signs used to determine condition
# > (Greater then)
# >= (Greater or equal to)
# < (Smaller then)
# <= (Smaller or equal to)
# == (Equality)
# != (Not equal to)

x = int(input("What's x? "))
y = int(input("What's y? "))

#This is an if
if x < y:
    print ("x is less than y")
if x > y:
    print ("x is greater than y")
if x == y:
    print ("x is equal to y")

 #in this way you make the algorithm faster, bc it stops when TRUE
if x < y:
    print ("x is less than y")
elif x > y:
    print ("x is greater than y")
elif x == y:
    print ("x is equal to y")

#you can use else too
if x < y:
    print ("x is less than y")
elif x > y:
    print ("x is greater than y")
else:
    print ("x is equal to y")

#now we gonna see how to use the condition "OR"

if x < y or x > y:
    print('X is not equal to y')
else:
    print('X is equal to y')

#Or you can use the != (not equal)
if x != y:
    print('X is not equal to y')
else:
    print('X is equal to y')

#now we gonna see how to use the condition "AND"
score = int(input('Score: '))

if score >= 90 and score <= 100:
    print('Grade A')
elif score >= 80 and score < 90:
    print('Grade B')
elif score >= 70 and score < 80:
    print('Grade C')
elif score >= 60 and score < 0:
    print('Grade D')
else:
    print('Grade F')

#or you can do like this
if  90 >= score <= 100:
    print('Grade A')
elif 80 >= score < 90:
    print('Grade B')
elif 70 >= score < 80:
    print('Grade C')
elif 60 >= score < 70:
    print('Grade D')
else:
    print('Grade F')
    
#or even more simplified 
if score >= 90:
    print('Grade A')
elif score >= 80:
    print('Grade B')
elif score >= 70:
    print('Grade C')
elif score >= 60:
    print('Grade D')
else:
    print('Grade F')
     
#i dont really know what this was about, but he told that we can make those if statements
x = int(input("What's x? "))

if x % 2 == 0: #this means "Is this number divided by 2?"
    print("Even")
else:
    print("Odd")

#Now we gonna see about Boolean values (True or False)

def main():
    x= int(input("What's the x? "))
    if is_even(x):
        print ("Even")
    else:
        print ("Odd")

def is_even(n): #it has an "n" because i want this function to have an argument
    if n % 2 == 0:
        return True #This is a boolean value, in python we have str; int; float; bool
    else:
        return False

main()

#or you can do like this
def main():
    x= int(input("What's the x? "))
    if is_even(x):
        print ("Even")
    else:
        print ("Odd")

def is_even(n):
    return True if n % 2 == 0 else False #this way is more simplified

main()

#to make a even better code, you can do it like this one
def main():
    x= int(input("What's the x? "))
    if is_even(x):
        print ("Even")
    else:
        print ("Odd")


#Now we going to lean "Match
#this is the code we going to optimize
name = input ("What's your name? ")

if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

#so you can do it like this>
match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who")

#so using "case" you can do it like this
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who")
