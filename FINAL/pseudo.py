# VARIABLES
import turtle as trutle
import turtle
import random
# variables: health, damage, defense
hp = 100
dp = 10
defense = 0

# dictionary for inventory
items = []
# boolean variables for each room so interactions can't happen twice
room1 = False
room2 = False
room3 = False
room4 = False
room5 = False
room6 = False
room7 = False
roomSecret = False
roomBoss = False

# enemy state variables like mummy, scarab, boss
mummy = 30
mummyD = 6
scarab = 50
scarabD = 4
boss = 120
bossD = 15
#python load
import turtle
import time

screen = turtle.Screen()

eye = turtle.Turtle()
eye.width(3)
eye.speed(0)
eye.hideturtle()
eye.setpos(0,0)
eye.pendown()
eye.forward(35)
eye.right(5)
eye.forward(20)
eye.left(60)
eye.forward(4)
eye.left(75)
eye.forward(10)
eye.right(10)
eye.forward(20)
eye.left(40)
eye.forward(15)
eye.left(10)
eye.width(4)
eye.forward(10)
eye.left(10)
eye.forward(10)
eye.left(30)
eye.forward(20)
eye.left(20)
eye.forward(10)
eye.right(40)
eye.width(5)
eye.forward(30)
eye.right(10)
eye.forward(20)
eye.left(80)
eye.forward(7)
eye.left(105)
eye.width(4)
eye.forward(30)
eye.right(15)
eye.forward(20)
eye.setpos(0,0)
eye.penup()
eye.setpos(18,18)
eye.pendown()
eye.width(35)
eye.forward(1)
eye.penup()
eye.setpos(20,-2)
eye.width(7)
eye.pendown()
eye.right(120)
eye.forward(20)
eye.width(6)
eye.right(10)
eye.forward(15)
eye.right(15)
eye.forward(10)
eye.right(20)
eye.forward(5)
eye.width(4)
eye.right(20)
eye.forward(5)
eye.right(30)
eye.forward(5)
eye.width(2)
eye.right(30)
eye.forward(3)
eye.penup()
eye.setpos(25,-2)
eye.pendown()
eye.right(196)
eye.width(10)
eye.forward(8)
eye.width(9)
eye.forward(7)
eye.width(8)
eye.forward(7)
eye.width(6)
eye.forward(7)
eye.width(5)
eye.forward(6)
eye.penup()
eye.setpos(55,45)
eye.left(240)
eye.pendown()
eye.width(6)
eye.forward(20)
eye.left(15)
eye.forward(25)
eye.left(15)
eye.width(7)
eye.forward(20)
eye.left(20)
eye.forward(15)
eye.left(10)
eye.width(8)
eye.forward(10)
eye.left(10)
eye.forward(10)
eye.right(10)
eye.width(7)
eye.forward(10)
eye.right(10)
eye.width(6)
eye.forward(10)
eye.right(20)
eye.width(5)
eye.forward(20)

eye.penup()
eye.setpos(-68,8)
eye.pendown()
eye.right(175)
eye.forward(30)
eye.left(10)
eye.width(7)
eye.forward(15)



t1= turtle.Turtle()
font_style = ("Times New Roman", 25, "normal")
t1.hideturtle()
t1.penup()
t1.goto(0,-150)
t1.pendown()
t1.write("LOADING...", font=font_style, align="center")




dot = turtle.Turtle()

dot.penup()
dot.speed(5)
dot.hideturtle()
dot.setpos(-10,110)
dot.width(10)
dot.pendown()
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.speed(1)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.speed(100)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.speed(1)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.speed(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.speed(1)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.speed(0)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)
dot.right(6)
dot.forward(10)

time.sleep(.2)
t1.clear()

time.sleep(.2)

t2= turtle.Turtle()
font_style = ("Times New Roman", 25, "normal")
t2.hideturtle()
t2.penup()
t2.goto(0,-150)
t2.pendown()
t2.write("click to continue", font=font_style, align="center")

screen.exitonclick()











#game functions

# startGame()
def startgame():
    global room1, room2, room3, room4, room5, room6, room7, roomSecret, roomBoss
    while True:
        print("You enter the pyramid, and the opening behind you crumbles shut, you are stuck")
        print("You had been exploring near a pyramid when you found a small entrance and went inside.")
        play = input("Do you wish to continue? (Y/N): ").upper()
        if play == "Y":
            room1_func()
            break
        elif play == "N":
            print("BYE BYE")
            break


# combat()    health and damage
def combat(enemy_hp, enemy_damage):
    global hp
    current_enemy_hp = enemy_hp
    while current_enemy_hp > 0 and hp > 0:
        choice = input("Fight or give up? (F/G): ").upper()
        if choice == "G":
            return False
        current_enemy_hp -= dp
        hp -= max(enemy_damage - defense, 0)
        print(f"Enemy HP: {current_enemy_hp} | Your HP: {hp}")
    return hp > 0


# pickupitem()
#   if item not in inventory then add it
#   if item already in dictionary then dont add (prevents repeteable pickup)
def pickupitem(item):
    if item not in items:
        items.append(item)
        return True
    return False


# changestats() function to change statistics
#   increase health or damage or defense depending on itemm that are pick up
def changestats(item):
    global hp, dp, defense
    if item == "mummy toe":
        hp += 50
    elif item == "khopesh":
        dp += 5
    elif item == "scarab shield":
        defense += 4


# restartghame()
#   reset stats
#   reset all booleans
#   reset enemy defeated variables
#   send player back to start game function
#basically start over

def restartgame():
    global hp, dp, defense, items
    global room1, room2, room3, room4, room5, room6, room7, roomSecret, roomBoss
    hp = 100
    dp = 10
    defense = 0
    items = []
    room1 = False
    room2 = False
    room3 = False
    room4 = False
    room5 = False
    room6 = False
    room7 = False
    roomSecret = False
    roomBoss = False
    startgame()


#room functions 

# ROOM1
def room1_func():
    global room1
    room1 = True
    print("You are in the entracnce chamber.")
    choice = input("Go to room 2(1) or room 3 (2)? ")
    if choice == "1":
        room2_func()
    else:
        room3_func()


# ROOM2
# ROOM2
def room2_func():
    global room2, hp
    if room2:
        print("You already visited this room.")
        room1_func()
        return
    room2 = True
    correct = random.choice(["1", "2"])
    guess = input("Chest lock: choose 1 or 2: ")
    if guess != correct:
        hp -= 5
        print("Trap! You take damage.")
    else:
        if pickupitem("mummy toe"):
            changestats("mummy toe")
            print("You gained +50 heealth! from eating mummy toe")
    room1_func()


# ROOM3
# ROOM3
def room3_func():
    global room3
    room3 = True
    print("A dusty hall with a suspiucious cracked wall.")
    choice = input("INVESTIGATE or MoVE to room 4 ").upper()
    if choice == "INVESTIGATE":
        roomsecret_func()
    else:
        room4_func()


# SECRET ROOM
# SECRET ROOM
def roomsecret_func():
    global roomSecret
    if roomSecret:
        room3_func()
        return
    roomSecret = True
    if pickupitem("scarab shield"):
        changestats("scarab shield")
        print("You gained +4 defense! from a sheild you found in this secret room")
        print("you exit to room 5")
    room5_func()


# ROOM4
def room4_func():
    global hp, room4
    room4 = True
    hp -= 1
    print("A mummy attacks!")
    if not combat(mummy, mummyD):
        restartgame()
        return
    if pickupitem("khopesh"):
        print("you picked up the mummies khopesh for + 5 damage, (a khopesh is an ancient egygptian sword, it is curved forward to be better at chopping, but curves back straight to align with the tang of the blade, mkaing it useful for stabbing too)")
        changestats("khopesh")
    room5_func()


# ROOM5
def room5_func():
    global hp, dp, defense, room5
    room5 = True
    randstat = random.randint(1,3)
    well = input("There is a dark well, sacrifice 1 health for random stat increase Y/N.").upper()
    if well == "Y":
        hp -= 1
        if randstat == 1:
            hp += 10
            print("plus 10 health")
        elif randstat == 2:
            dp += 4
            print("plus 4 damage")
        elif randstat == 3:
            defense += 2
            print("plus 2 defense")
    else:
        print("it was only 1 health, anyway time to move")
    choice = input("Go to ROOM3, ROOM2, or ROOM7? ").upper()
    if choice == "ROOM7":
        room7_func()
    elif choice == "ROOM2":
        room2_func()
    else:
        room3_func()


# ROOM6
def room6_func():
    global room6
    room6 = True
    print("A giant scarab attacks!")
    if combat(scarab, scarabD):
        if pickupitem("scarab shield"):
            print("you picked up the scarabs shell, you can use it as a sheild for +2 defense")
            changestats("scarab shield")
            
    choice2 = input("Go to ROOM7, or ROOM5? ").upper()
    if choice2 == "ROOM7":
        room7_func()
    elif choice2 == "ROOM5":
        room5_func()


# ROOM7
def room7_func():
    global hp, dp, defense, room7
    room7 = True
    choice = input("you enter and see 3 alters, each can increase a statChoose altar: HEALTH, DAMAGE, or DEFENSE: ").upper()
    print("your stat increases, but a door opens, the room your in crumbles and you run into the finl room.")
    if choice == "HEALTH":
        hp += 20
    elif choice == "DAMAGE":
        dp += 3
    else:
        defense += 3
    roomfinal_func()


# FINAL ROOM
def roomfinal_func():
    global boss
    print("The final boss awakens, anubis, the god of the afterlife arises")
    if combat(boss, bossD):
        print("YOU ESCAPED THE PYRAMID VICTOrRIOUS!, escaping with the skull of the jackal headed god")

    else:
        print("You lost. Anubis rips out your heart and sends you to Duat. ")
        restartgame()


# MAIN GAME looP

# startGame()
startgame()
