# VARIABLES
import turtle
import random
# variables: health, damage, defense
hp = 200
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
    while True:
        
#   print statement welcoming player
        print("You enter the pyramid, and the opening behind you crumbles shut, you are stuck")
#   print backstory explaining where you are (in pyramid 
        print("You had been exploring near a pyramid when you found a small entrance and went inside.")
#   ask user if they wish to play the game now that they know what happens
        play = input("Do you wish to continue? (Y/N): ").upper()
#   if yes go to room1
        if play == "Y":
            room1_func()
            break
#   if no exit game (break)
        elif play == "N":
            print("BYE BYE")
            break


# combat()    health and damage
def combat(enemy_hp, enemy_damage):
#     player chooses attack 
    global hp
    while enemy_hp > 0 and hp > 0:
        choice = input("Fight or give up? (F/G): ").upper()
#   update player health and enemy health based on damage and defense
        if choice == "G":
            return False
        enemy_hp -= dp
        hp -= max(enemy_damage - defense, 0)
        print(f"Enemy HP: {enemy_hp} | Your HP: {hp}")
#   loop keeps going until one reaches 0
#   return win or lose 
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
        hp += 10
    elif item == "khopesh":
        dp += 3
    elif item == "scarab shield":
        defense += 2


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
    room1 = room2 = room3 = room4 = room5 = room6 = room7 = roomSecret = roomBoss = False
    startgame()


#room functions 

# ROOM1
def room1_func():
# just entered pyramid, entrance closed behind you
    print("You are in the entrance chamber.")
# there is a path to left and forward
    choice = input("Go to room 2(1) or room 3 (2)? ")
# user input where to go
# leads to room2 or room3
    if choice == "1":
        room2_func()
    else:
        room3_func()


# ROOM2
def room2_func():
# there is a chest in the corner it has a combination lock choose 1 or 2 to open (will make random so cant repeat on playthrough)
    global hp
    import random
    correct = random.choice(["1", "2"])
    guess = input("Chest lock: choose 1 or 2: ")
# if wrong input take damage
    if guess != correct:
        hp -= 5
        print("Trap! You take damage.")
# if right find cheesy mummy toe, eat to get +2 health
    else:
        if pickupitem("mummy toe"):
            changestats("mummy toe")
            print("You gained +2 health!")
# check if item already in inventory
    room1_func()


# ROOM3
def room3_func():
# description of the room
    print("A dusty hall with a suspiucious cracked wall.")
# do you wish to investigate suspicious wall, or move on forward or to the right
    choice = input("INVESTIGATE or MOVE to room 4 ").upper()
# suspicious wall leads to secret room
    if choice == "INVESTIGATE":
        roomsecret_func()
# nothing else in room
    else:
        room4_func()


# SECRET ROOM
def roomsecret_func():
# only allow entry if sroom var is False
    global roomSecret
    if roomSecret:
        room3_func()
# once entered set secret room variable  to True
    roomSecret = True
# special interaction or item here (tbd
    if pickupitem("scarab shield"):
        changestats("scarab shield")
        print("You gained +2 defense!")
        print("you exit to room 5")
# leads back to room3 or room5
    room5_func()


# ROOM4
def room4_func():
# as player enters, they are attackeed by a mummy for -1 health
    global hp
    hp -= 1
    print("A mummy attacks!")
# if player dies allow them to restart
    if not combat(mummy, mummyD):
        restartgame()
# if player wins recieve khopesh sword for +2 damage
    if pickupitem("khopesh"):
        print('you picked up the mummies khopesh for + 3 damage, (a khopesh is an ancient egyptian sword, it is curved forward to be better at chopping, but curves back straight to align with the tang of the blade, mkaing it useful for stabbing too)')
        changestats("khopesh")
# check mummy var so fight doesn't happen again
    room5_func()


# ROOM5
def room5_func():
    randstat = random.randint(1,3)
# as player enters there is a well
    global hp
    well = input("There is a dark well, sacrifice 1 health for random stat increase Y/N.").upper()
    if well == "Y":
# sacrifice 1 health to gain random item
                hp -= 1
                if randstat == 1:
                    hp+=10
                    print("plus 10 health")
                elif randstat == 2:
                    dp += 4
                    print("plus 4 damage")
                elif randstat == 3:
                    defense+=2
                    print("plus 2 defense")

    else:
        print("it was only 1 health, anyway time to move")
# leads to rooms 3, 2, and 7
    choice = input("Go to ROOM3, ROOM2, or ROOM7? ").upper()
    if choice == "ROOM7":
        room7_func()
    elif choice == "ROOM2":
        room2_func()
    else:
        room3_func()


# ROOM6
def room6_func():
# as they enter they fightt giant scarab beetle
    print("A giant scarab attacks!")
# if player wins they can equip scarab shell shield for +2 defense
    if combat(scarab, scarabD):
        if pickupitem("scarab shield"):
            print("you picked up the scarabs shell, you can use it as a sheild for +2 defense")
            changestats("scarab shield")
# check scarab var so it doesn't fight again
    room7_func()


# ROOM7
def room7_func():
# in the room there are 3 alters each one with an item for either health damage or deffense
    choice = input("you enter and see 3 alters, each can increase a statChoose altar: HEALTH, DAMAGE, or DEFENSE: ").upper()
    print("your stat increases, but a door opens, the room your in crumbles and you run into the finl room.")
# the player thinks they can get adll three
# but once they get one the room is destroyed
    if choice == "HEALTH":
        hp += 10
    elif choice == "DAMAGE":
        dp += 3
    else:
        defense += 3
# they are forced into the boss room (finalRoom)
    roomfinal_func()


# FINAL ROOM
def roomfinal_func():
# contains final boss combat
    print("The final boss awakens, anubis, the god of the afterlife arises")
# if win print victory message 
    if combat(boss, bossD):
        import turtle
        import time

        screen1 = turtle.Screen()


        e = turtle.Turtle()
        e.width(3)
        e.speed(0)
        e.hideturtle()
        e.setpos(0,0)
        e.right(30)
        e.forward(30)
        e.left(25)
        e.forward(80)
        e.right(10)
        e.forward(120)
        e.left(30)
        e.forward(20)
        e.left(45)
        e.forward(20)
        e.left(30)
        e.forward(5)
        e.left(100)
        e.forward(30)
        e.right(35)
        e.forward(130)
        e.left(40)
        e.forward(20)
        e.right(60)
        e.forward(40)
        e.right(25)
        e.forward(45)

        e.left(90)
        e.forward(30)
        e.left(70)
        e.forward(25)
        e.right(60)
        e.forward(25)

        e.right(50)
        e.forward(20)
        e.left(60)
        e.forward(5)
        e.left(90)
        e.forward(35)

        e.setpos(0,0)
        e.home()
        e.penup()
        e.setpos(250,-25)
        e.pendown()
        e.left(65)
        e.forward(20)
        e.left(30)
        e.forward(15)
        e.left(145)
        e.forward(20)
        e.right(30)
        e.forward(20)

        e.penup()
        e.home()
        e.setpos(225,-28)
        e.left(70)
        e.pendown()
        e.forward(20)

        e.left(30)
        e.forward(15)
        e.left(140)
        e.forward(15)
        e.right(25)
        e.forward(10)
        e.setpos(120,30)
        e.setpos(113,22)

        t = turtle.Turtle()
        t.hideturtle()
        t.width(3)
        t.speed(0)
        t.hideturtle()
        t.left(60)
        t.penup()
        t.setpos(208, -22)
        t.pendown()
        t.forward(13)
        t.penup()

        t.penup()
        t.setpos(190, -15)
        t.pendown()
        t.forward(13)
        t.penup()

        t.penup()
        t.setpos(170, -6)
        t.pendown()
        t.forward(13)
        t.penup()

        t.penup()
        t.setpos(150, 1)
        t.pendown()
        t.forward(13)
        t.penup()

        t.penup()
        t.setpos(130, 12)
        t.pendown()
        t.forward(13)
        t.penup()

        t.setpos(218, -10)
        t.pendown()
        t.left(90)
        t.forward(70)
        t.left(90)
        t.forward(10)


        t.penup()
        t.home()
        t.setpos(30,100)
        t.pendown()
        t.right(15)
        t.forward(60)
        t.right(45)
        t.forward(30)
        t.left(70)
        t.forward(70)
        t.left(25)
        t.forward(45)
        t.right(50)
        t.forward(50)
        #hook end of top teeth
        t.left(115)
        t.forward(20)
        t.right(25)
        t.forward(30)
        t.left(75)
        t.forward(15)
        t.left(10)
        t.forward(30)
        t.left(15)
        t.forward(35)
        t.right(20)
        t.forward(35)
        t.right(180)
        t.forward(35)
        t.left(145)
        t.forward(35)
        t.left(60)
        t.forward(25)
        #above eye
        t.right(20)
        t.forward(55)
        t.left(25)
        t.forward(65)
        t.left(32)
        t.forward(110)
        t.left(40)
        t.forward(45)

        t.left(20)
        t.forward(50)

        t.left(90)
        t.forward(20)

        t.left(75)
        t.forward(25)
        t.setpos(30, 100)

        t.penup()
        t.home()
        t.setpos(40, 175)
        t.pendown()

        t.left(25)
        t.forward(30)

        t.right(70)
        t.forward(40)
        t.right(70)
        t.forward(20)

        t.right(40)
        t.forward(30)

        t.right(40)
        t.forward(20)

        t.right(35)
        t.forward(25)
        t.setpos(40, 175)

        t.penup()
        t.home()

        t.setpos(255, 85)
        t.pendown()


        t.right(80)
        t.forward(25)

        t.right(35)
        t.forward(22)
        t.right(150)
        t.forward(20)
        t.left(20)
        t.forward(10)
        t.setpos(255, 85)

        t.penup()
        t.home()
        t.setpos(245, 70)
        t.left(170)
        t.pendown()
        t.forward(20)

        t.penup()
        t.home()
        t.setpos(210, 95)
        t.pendown()

        t.right(60)
        t.forward(25)
        t.right(40)
        t.forward(32)

        t.right(155)
        t.forward(25)
        t.left(35)
        t.forward(12)

        t.left(80)
        t.forward(30)
        t.right(28)
        t.forward(70)
        t.right(95)
        t.forward(18)


        t.penup()
        t.home()
        t.left(100)
        t.setpos(130, 43)
        t.pendown()
        t.forward(18)

        t.penup()
        t.setpos(145, 48)
        t.pendown()
        t.forward(17)

        t.penup()
        t.setpos(160, 52)
        t.pendown()
        t.forward(17)

        t.penup()
        t.setpos(175, 56)
        t.pendown()
        t.forward(17)

        t.penup()
        t.setpos(190, 64)
        t.pendown()
        t.forward(15)

        t.penup()
        t.setpos(198, 72)
        t.pendown()
        t.left(30)
        t.forward(15)

        t.penup()
        t.setpos(225, 75)
        t.pendown()
        t.right(35)
        t.forward(18)

        t.penup()
        t.setpos(238, 73)
        t.pendown()
        t.right(20)
        t.forward(17)

        time.sleep(1)


        t2= turtle.Turtle()
        font_style = ("Times New Roman", 25, "normal")
        t2.hideturtle()
        t2.penup()
        t2.goto(100,-150)
        t2.pendown()
        t2.write("You defeated Anubis, protector of the after life", font=font_style, align="center")

        time.sleep(.5)

        time.sleep(.5)

        t2= turtle.Turtle()
        font_style = ("Times New Roman", 25, "normal")
        t2.hideturtle()
        t2.penup()
        t2.goto(100,-200)
        t2.pendown()
        t2.write("click to continue", font=font_style, align="center")

        screen1.exitonclick()
        print("YOU ESCAPED THE PYRAMID VICTOrRIOUS!, escaping with the skull of the jackal headed god")
        turtle.done
# if lose ask if they wsant to restartGame() and call them loser
    else:
        print("You lost. Anubis rips out your heart and sends you to Duat. ")
        restartgame()


# MAIN GAME looP

# startGame()
startgame()
