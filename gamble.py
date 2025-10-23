

import random

print("its gamblin time")
money = 500.0 # Use a float for money to handle division correctly

while money > 0:
    print("you have", money, "money")
    choice = input("want to coin flip 50 percent chance (1) want to do lottery, 5 percent chance (2) or want to quit (3)")

    # The input() function returns a string. Compare the 'choice' variable to strings.
    if choice == '1':
        result = random.randint(1, 2)
        if result == 1:
            money *= 2
            print("You won the coin flip!")
        else:
            money /= 2
            print("You lost the coin flip.")

    elif choice == '2':
        result = random.randint(1, 20)
        if result == 1:
            money *= 20
            print("You won the lottery!")
        else:
            money /= 2
            print("You lost the lottery.")

    elif choice == '3':
        print("quiting")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

print("Game over. Final money:", money)
