'''
Start of the LOOP class

28/05/2023 (xx minutes)
Start: Introduction
End: 
'''

#a manual loop for 3 meows
print("Meow")
print("Meow")
print("Meow")

#we can use WHILE

i = 3
while i != 0:
    print("Meow")
    i = i - 1

#or you can do like this
i = 0 
while i < 3:
    print("Meow")
    i = i + 1

#this is how to use a FOR loop and a list
for i in [0, 1 , 2]:      #"i" gonna be zero, then one, then two, then three /// [] <- this represents a list
    print("Meow")

#you can use a function in the place of the list
for i in range(100):      #we dont need to have a def, you just put a function
    print("Meow")

#is pythonic to remove the i and replace for _ when you dont gonna use this variable again
for _ in range(100):    
    print("Meow")

#or you can do like this 
print("Meow\n" * 3, end="")

#another feature that u can use with while is:
while True:
    n = int(input("What's n? "))
    if n < 0:
        continue
    else:
        break

#or you can make it smaller
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("Meow")

#to exemplify FOR and WHILE in a function:

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("Meow")

main()

#this is how lists works, 

students = ["Hermione", "Harry", "Ron"]

print(students[0])
print(students[1])
print(students[2])

#but you can use loop for that
students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)

#this is how you print the list of students

students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i+1, students[i]) #the i is bc i want to make a ranking starting by 1 
