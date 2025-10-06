
        comp_move = (rock)
    elif random_move == 2:
        comp_move = (paper)
    elif random_move == 3:
        comp_move = (scissor)
    else:
        print("error")
    print (comp_move)

    user_input = input("choose rock (1) paper (2) scissors (3) or quit (4): ")
    user_input = int(user_input)
    if user_input == 1: