import random

playerhp = 30
monsterhp = (random.randint(20,50))
roll = (random.randint(1,20))
monsteratk = (random.randint(2,15))
print ("monster health is", monsterhp)
print ("you rolled a", roll)

if roll > 18:
    print ("critical hit of", roll, "damage")
elif roll >8:
    print ("you landed a hit of", roll, "damage")
elif roll <8:
    print ("you did minimal damage monster attacks you for",monsteratk, "damage")
    playerhp = playerhp - monsteratk

print ("your health is now",playerhp)
print ("")