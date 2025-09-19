import random

playerhp = 30

roll = (random.randint(1,20))

print ("you rolled a", roll)

if roll > 18:
    print ("critical hit")
elif roll >8:
    print ("you landed a hit of", roll, "damage")