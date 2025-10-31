# DP 2nd combat code
import random 

#funstionwith monster stats
def monster():
    m_damage = random.randint(2,14)
    m_health = random.randint(45,70)
    return m_damage, m_health

m_damage, m_health = monster()

def attack1(x,y):
    return x-y

hp = 50
attack = 10
defense = 2
#random funstions
randmove = random.randint(1,2)
randmove1 = random.randint(1,3)
randmove2 = random.randint(1,5)
randmove3 = random.randint(1,10)

#get class and name
name = input('What is your name: ')
type = input('what is your class: Warrior (1), Mage (2), normal human (3): ')

if type == "1":
    hp = hp - randmove2
    attack = attack + randmove
    print(name, "your stats as a Warrior are HP:", hp, ", attack:", attack, "Defense:", defense)
elif type == "2":
    hp = hp + randmove3
    attack = attack - randmove
    defense = defense + randmove2
    print(name, "your stats as a Mage are HP:", hp, ", attack:", attack, "Defense:", defense)
    #The human class is kinda bad
elif type == "3":
    hp = hp - randmove3
    attack = attack - randmove3
    print(name, "your stats as a Human are HP:", hp, ", attack:", attack, "Defense:", defense)

print(" monster attacks you!")
print("Monster HP:", m_health)
#players moves in function
def player_turn():
    global hp, attack, m_health
    print("\nYour turn:")
    print("1 attack enemy")
    print("2 wild attack (double damage but take damage)")
    print("3 heal (5–15 HP)")
    print("4 run (50% chance)")
    move = input(": ")
#different actions
    if move == "1":
        dmg = random.randint(2, attack)
        m_health -= dmg
        print("You hit for", dmg)

    elif move == "2":
        dmg = random.randint(4, attack * 2)
        wild = random.randint(1,6)
        m_health -= dmg
        hp -= wild
        print("Wild hit for", dmg, "You take", wild)

    elif move == "3":
        heal = random.randint(5,15)
        hp += heal
        print("You heal", heal)

    elif move == "4":
        if random.randint(1,2) == 1:
            print("You fled!")
            return "fled"
        else:
            print("Failed to runn away.")

def monster_turn():
    global hp, m_damage
    dmg = random.randint(1, m_damage)
    hp -= dmg
    print("Monster hits you for", dmg)
#random turns
turn = random.randint(1,2)
print("\nYou go first" if turn == 1 else "\nMonster goes first!")
#while loop to keep game running
while hp > 0 and m_health > 0:
    if turn == 1: 
        turn232 = player_turn()#random variable name
        if turn232== "fled":
            break
        turn = 2
    else:
        monster_turn()
        turn = 1
    print("Your HP:", hp, "Monster HP:", m_health)
#deatah condition
if hp <= 0:
    print("\nYou died.")
elif m_health <= 0:
    print("\nYou beat the monster yippee")
