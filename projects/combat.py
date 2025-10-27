#DP 2nd combat code
import random 

hp = (50)
attack = (10)
defense = (2)


randmove = random.randint(1,2)
randmove1 = random.randint(1,3)
randmove2 = random.randint(1,5)
randmove3= random.randint(1,10)
print (randmove)

name = input('What is your name: ')
type = input('what is your class: Warrior (1), Mage (2), normal human (3)')


if type == "1":
    print (name,"your stats as a Warrior are HP: ", hp - randmove2,", attack: ", attack + randmove, "Defense: ", defense)
    attacktype = "axe chop"
elif type == "2":
    print (name,"your stats as a Mage are HP: ", hp + randmove3,", attack: ", attack - randmove, "Defense: ", defense + randmove2)
    attacktype = "fire ball"
elif type == "3":
    print (name,"your stats as a Human are HP: ", hp - randmove3,", attack: ", attack - randmove3, "Defense: ", defense)
    attacktype = "slap"
def monster():
    m_damage = random.randint(2,14)
    m_health = random.randint (45,70)
monster()


atrackinp = input("press one to",attacktype,"enemy" )

