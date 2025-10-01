import random

# Each player starts with 10 tower health
player1_health = 10
player2_health = 10
p1_elixir = 9
p2_elixir = 9

# Simple cards: each does 2, 3, or 4 damage
cards = [2, 3, 4]

print("clash")
print("win.")

while player1_health > 0 and player2_health > 0:
    # Player 1's turn
    print("\nPlayer 1's turn:")
    print(f"Your tower:{player1_health}, Opponent tower: {player2_health}")
    print("Choose a card: arrows, type 1 (2 dmg), pekka, type 2 (3 dmg), giant, type 3 (4 dmg)")
    choice = int(input("Enter card number: ")) - 1
    dmg = cards[choice]
    player2_health -= dmg
    print(f"You dealt {dmg} damage!")
    if player2_health <= 0:
        print("Player 1 wins!")
        break
    
    # Player 2's turn
    print("\nPlayer 2's turn:")
    print(f"Your tower: {player2_health}, Opponent tower: {player1_health}")
    print("Choose a card: arrows, type 1 (2 dmg), pekka, type 2 (3 dmg), giant, type 3 (4 dmg)")
    choice = int(input("Enter card number: ")) - 1
    dmg = cards[choice]
    player1_health -= dmg
    print(f"You dealt {dmg} damage!")
    if player1_health <= 0:
        print("Player 2 wins!")
        break
    