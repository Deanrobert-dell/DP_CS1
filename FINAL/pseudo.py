# VARIABLES

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
        hp += 2
    elif item == "khopesh":
        dp += 2
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
    choice = input("Go LEFT or FORWARD? ").upper()
# user input where to go
# leads to room2 or room3
    if choice == "LEFT":
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
    print("A dusty hall with a cracked wall.")
# do you wish to investigate suspicious wall, or move on forward or to the right
    choice = input("INVESTIGATE or MOVE? ").upper()
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
        changestats("khopesh")
# check mummy var so fight doesn't happen again
    room5_func()


# ROOM5
def room5_func():
# as player enters there is a well
    global hp
    print("There is a dark well.")
# sacrifice 1 health to gain random item
    hp -= 1
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
            changestats("scarab shield")
# check scarab var so it doesn't fight again
    room7_func()


# ROOM7
def room7_func():
# in the room there are 3 alters each one with an item for either health damage or defense
    choice = input("Choose altar: HEALTH, DAMAGE, or DEFENSE: ").upper()
# the player thinks they can get adll three
# but once they get one the room is destroyed
    if choice == "HEALTH":
        hp_gain = 5
    elif choice == "DAMAGE":
        dp_gain = 3
    else:
        defense_gain = 3
# they are forced into the boss room (finalRoom)
    roomfinal_func()


# FINAL ROOM
def roomfinal_func():
# contains final boss combat
    print("The final boss awakens.")
# if win print victory message 
    if combat(boss, bossD):
        print("YOU ESCAPED THE PYRAMID VICTORIOUS!")
# if lose ask if they wsant to restartGame() and call them loser
    else:
        print("You lost. Loser.")
        restartgame()


# MAIN GAME LOOP

# startGame()
startgame()
