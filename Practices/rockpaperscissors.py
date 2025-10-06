import random

random_move= random.randint(1,3)

user_score = 0

comp_score = 0

rock = "    _____   \n   /     \\ \n  |       | \n   \\_____/ \n      "

scissor = "Ʌ     Ʌ\n\\\   //\n \\\_//\n  (_)\n/\   /\ \n\/   \/ "

paper = " ______\n/     /\n|     |\n\\_____\\"


while user_score <= 5 and comp_score <=5:
    if random_move == 1:
        comp_move = (rock)
    elif random_move == 2:
        comp_move = (paper)
    elif random_move == 3:
        comp_move = (scissor)
    else:
        print("error")
    print (comp_move)
    print ("computer chose, your turn \n")

    user_input = input("choose rock (1) paper (2) scissors (3) or quit (4): ")
    user_input = int(user_input)
    if user_input == 1:
        user_move = (rock)
    elif user_input == 2:
        user_move = (paper)
    elif user_input == 3:
        user_move = (scissor)
    elif user_input == 4:
        print ("quiting")
        break
    else:
        print("error")
    print (user_move)
    


print (user_move)



    

