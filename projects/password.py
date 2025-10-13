#variable for password strength
strength = (0)
#variables for upper and lower
uppercase = False
lowercase = False
# create different progress levels as variable
bar1 = (" ________ \n/")
bar2 = (" ________ \n//     ")
bar3 = (" ________ \n////   ")
bar4 = (" ________ \n/////  ")
bar5 = (" ________ \n/////////")

#variables for numbers
num1 = ("1")
num2 = ("2")
num3 = ("3")
num4 = ("4")
num5 = ("5")
num6 = ("6")
num7 = ("7")
num8 = ("8")
num9 = ("9")
num0 = ("0")


#input asking for password
password = input("what is your password: ")

#make list from password
pass_list = list(password)

print (pass_list)

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


#Checks for number after converting to list

if num1 or num2 or num3 or num4 or num5 or num6 or num7 or num8 or num9 or num0 in pass_list:
    print("you have a number ✓")
    strength += 1
else:
    print ("password needs number")

























