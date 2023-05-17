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

#Now we gonna see some similar as int, it's gonna be the FLOAT (the one that i usually use on arcmap)
