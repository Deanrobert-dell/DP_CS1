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
mummy= 30
mummyD = 6
scarab = 50
scarabD = 4
boss = 120
bossD = 15

#game functions

# startGame()
def startgame():
#   print statement welcoming player
    print("You enter the pyramid, and the opening behind you crumbles shut, you are stuck")
#   print backstory explaining where you are (in pyramid 
#   ask user if they wish to play the game now that they know what happens
#   if yes go to room1
#   if no exit game (break)

# combat()    health and damage
#     player chooses attack or defense
#   update player health and enemy health based on damage and defense
#   loop keeps going until one reaches 0
#   return win or lose 

# pickupitem()
#   if item not in inventory then add it
#   if item already in dictionary then dont add (prevents repeteable pickup)

# changestats() function to change statistics
#   increase health or damage or defense depending on itemm that are pick up

# restartghame()
#   reset stats
#   reset all booleans
#   reset enemy defeated variables
#   send player back to start game function
#basically start over

#room functions 

# function for each room, change boolean if entered to make sure interactions cant happen twice
# example function steps:
#   welcoming to room
#   print description of room
#   if monster present first thing is fight or run (i might not add run as an option
#   if no monster describe chest for loot or suspicious wallcfor secret room
#   suspicious wall leads to secret room
#   to stop picking up items twice check inventory first whichis dictionary
#   for monsters use a defeated variable so fight only happens once

# ROOM1
# just entered pyramid, entrance closed behind you
# there is a path to left and forward
# user input where to go
# leads to room2 or room3

# ROOM2
# there is a chest in the corner it has a combination lock choose 1 or 2 to open (will make random so cant repeat on playthrough)
# if wrong input take damage
# if right find cheesy mummy toe, eat to get +2 health
# check if item already in inventory

# ROOM3
# description of the room
# do you wish to investigate suspicious wall, or move on forward or to the right
# suspicious wall leads to secret room
# nothing else in room

# SECRET ROOM
# only allow entry if sroom var is False
# once entered set secret room variable  to True
# special interaction or item here (tbd
# leads back to room3 or room5

# ROOM4
# as player enters, they are attackeed by a mummy for -1 health
# if player dies allow them to restart
# if player wins recieve khopesh sword for +2 damage
# check mummy var so fight doesn't happen again

# ROOM5
# as player enters there is a well
# sacrifice 1 health to gain random item
# leads to rooms 3, 2, and 7

# ROOM6
# as they enter they fightt giant scarab beetle
# if player wins they can equip scarab shell shield for +2 defense
# check scarab var so it doesn't fight again

# ROOM7
# in the room there are 3 alters each one with an item for either health damage or defense
# the player thinks they can get adll three
# but once they get one the room is destroyed
# they are forced into the boss room (finalRoom)

# FINAL ROOM
# contains final boss combat
# if win print victory message 
# if lose ask if they wsant to restartGame() and call them loser

# MAIN GAME LOOP

# startGame()
# while playing:
# room1()
# player go to other rooms based on their chioices
# combat happens inside room functions when needed in specififc rooms
# finalRoom() ends the game plus boss
#     break once finished
#can loop when dead so replayaable 
