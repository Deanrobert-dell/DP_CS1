#DP 2nd combat code
import random 

def monster():
    m_damage = random.randint(2,14)
    m_health = random.randint (45,70)
monster()


def attack1(x,y):
    return x-y
health = attack1(1,2)

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
    atrackinp = input("press one to axe chop enemy, press two to heal 5 - 15 health" )
elif type == "2":
    print (name,"your stats as a Mage are HP: ", hp + randmove3,", attack: ", attack - randmove, "Defense: ", defense + randmove2)
    atrackinp = input("press one to fire ball enemy" )
elif type == "3":
    print (name,"your stats as a Human are HP: ", hp - randmove3,", attack: ", attack - randmove3, "Defense: ", defense)
    atrackinp = input("press one to slap enemy" )








