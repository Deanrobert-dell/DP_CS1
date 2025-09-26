#DP 2nd Fix game


import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = (random.randint(1, 100))
    max_attempts = 10
    attempts = 0 #originally this stayed at 0 forever, that means you would never run out of guesses (logic)
    game_over = False
    while not game_over:
        guess = float(input("Enter your guess: ")) #wrong type of data, the > operator doesnt work with integers (runtime)
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        elif guess == number_to_guess: #There cannot be 2 if conditionals, this is wrong because both will be checked, (logic)
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
            attempts=attempts+1 #adds one to the attempts this is part of my first comment
        else: #pointless elif statement, this was simply not needed (logic)
            print("Too low! Try again.") 
            attempts=attempts+1 #adds one to the attempts this is part of my first comment
        continue
    print("Game Over. Thanks for playing!")
start_game()

