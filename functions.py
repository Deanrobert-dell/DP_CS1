def add():
    print (f"5 + 5 = {5+5}")
add()

def add(x,y):
    print (f"{x} + {y} = {x+y}")



add(5,5)

add(3.1,88)

playerhp = 100

def add(x,y):
    return x+y


num = 0
while num < add (2,2):
    print ("duck")
    num += 1
print("goose")
print(f"result is: {add (1,2)}")

add(5,5)
add(3.1,88)







def initials(name):
    names = name.split(" ")
    initial = " "
    for name in names:
        initial += name [0]
    return initial

print (f"deans initials are: {initials("dean peterson")}")




def attack (dmg):
    return playerhp - dmg
