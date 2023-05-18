'''
15/05/2023 (30 minutes)
Start: Introduction
End: Multiple Function Arguments
'''
#ask user for their name

x = input("what's your name? ")

#say hello to user
print (fr'hello, {x}')
print ('hello, ' + x)
print ('hello,', x)


'''
16/05/2023 (1 hour)
Start: Named Parameters
End: Type Conversion
'''
print(f'hello \n {x}') #\n steps one line
print(f'hello, ',x, end="???")
print ('how are you')
print(f'hello, ', x, sep ='???')    
print ("hello, 'friend'") 
print (f"hello {x}")

## now we gonna see how to format str##

y = input ("Whats your name? ")
y = y.strip() #remove whitespace from string
y = y.capitalize() #capitalize the string
y = y.title() #capitalize first letter of each word
y = y.strip().title() #merge string methods
print (f'hello, {y}')

#the input can have all those config just by coding like that:

z = input ("What's your name? ").strip().title()

first, last= z.split() #split user's name into first name and last name

print (f'hello, {first} the spider, {last}')

#Now its the integer class, we gonna see how to use .int, (it's numbers without decimal points)

#This one concatenate because you didn't informed the code that u want to convert the input x as a integer
x = input ("What's x? ")
y = input ("What's y? ")
z = x + y
print (z)

#Here in the line 11 we convert the variables to integer by using int() function
x = input ("What's x? ")
y = input ("What's y? ")
z = int(x) + int(y)
print (z)

#or you can inform that the input is going to be an int
x = int(input ("What's x? "))
y = int(input ("What's y? "))
print (x+y)

#or... 

print(int(input("What's your x? "))+int(input("What's your y? ")))


'''
17/05/2023 (1h 15min)
Start: Float
End: Defining Functions
'''

#Now we gonna see some similar as int, it's gonna be the FLOAT (the one that i usually use on arcmap)

x = float(input ("What's x? "))
y = float(input ("What's y? "))
z = round(x+y) #this function allows me to round numbers round(number[, ndigits])

print (z)

# if i want the float number formatted with thousand separators, i have to script like this

x = float(input ("What's x? "))
y = float(input ("What's y? "))
z = round(x+y) 

print (f'{z:,}')

#if you want to determine how much decimal digits in your float, u should do this


x = float(input ("What's x? "))
y = float(input ("What's y? "))
z = round(x/y, 4) #here we code to receive 4 decimal digits

print (z)

#or you can do like this

x = float(input ("What's x? "))
y = float(input ("What's y? "))
z = (x/y) 

print (f'{z:.2f}')#here we code to receive 2 decimal digits

#Now we gonna work with def (FUNCTIONS)

#here is an exemple of function without parameter
name = input("What's your name? ")

def hello():
    if name == 'Eduarda':
        return print('hello eduarda')
    if name == 'maria':
        return print('hello maria')
    else:
        return 'who r u?'
x = hello()
print (x)
    
#here is an exemplo using a parameter

def hello(to):
    print('Hello,', to)

name = input("What's your name? ")
hello(name) #here i transformed my incognite (to) into my variable (name), so that's why in Expression on field calculator we used the function name with the relative field name in ()

#this next step is to determine a default parameter to our funcion

def hello(to='world'):
    print ('hello', to)

hello()
name = input("What's your name? ")
hello(name)

'''
18/05/2023 (xx )
Start: Scope
End: (...)
'''
