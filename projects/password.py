#variable for password strength
strength = (0)
#variables for upper and lower
uppercase = False
lowercase = False
digit = False
char = False
# create different progress levels as variable
bar1 = (" ________ \n/")
bar2 = (" ________ \n//     ")
bar3 = (" ________ \n////   ")
bar4 = (" ________ \n/////  ")
bar5 = (" ________ \n/////////")

#variables for special charachter
char1 = "!@#$%^&*()_+=<>?[]{}"

#input asking for password
password = input("what is your password: ")

#turn password into list
password_list = list(password)

#variable for length
length = len(password)

#if statement for password length checking if it is longer than 8 charachters
if length >= 8:
    print ("long enough password ✓")
    strength += 1
else:
    print ("you need atleast 8 chrachters for strong password ")

# create for statement checking if an individual charachter is upper case
for item in password:
    if item.isupper():
        uppercase = True
        break 

# if statement for upper case letter
if uppercase:
    print("contains upper case ✓")
    strength += 1
else:
    print("you need an upper case letter")

# create for statement checking if an individual charachter is lower case
for item in password:
    if item.islower():
        lowercase = True
        break 

# if statement for upper case letter
if lowercase:
    print("contains lower case ✓")
    strength += 1
else:
    print("you need a lower case letter")

#Checks for number using for loop
for i in password:
    if i.isdigit():
        digit = True
        break 

#if statement for digit
if digit:
    print("contains number✓")
    strength += 1
else:
    print("you need a number")

#find if special charachters in list version of password
for x in password:
    if x in char1:
        char = True
        break 

if char:
    print("you have a special chrachter✓")
    strength += 1
else: 
    print ("need special charachter")
#print strenth
print ("your password strength is an",strength, "out of 5")

if strength == 1:
    print (bar1)
if strength == 2:
    print (bar2)
if strength == 3:
    print (bar3)
if strength == 4:
    print (bar4)
if strength == 5:
    print (bar5)
else:
    print ("bye bye")
    
 










