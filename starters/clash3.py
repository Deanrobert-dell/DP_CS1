import random

# Each player starts with 10 tower health
player1_health = 10
player2_health = 10
p1_elixir = 9
p2_elixir = 9

# Card data: name, damage, elixir cost
cards = [
    {"name": "arrows", "dmg": 2, "cost": 2},
    {"name": "pekka", "dmg": 3, "cost": 4},
    {"name": "giant", "dmg": 4, "cost": 6},
    {"name": "skip", "dmg": 0, "cost": 0}
]

def print_cards():
    for idx, card in enumerate(cards):
        print(f"{idx + 1}: {card['name']} ({card['dmg']} dmg, {card['cost']} elixir)")

def get_choice(player, elixir):
    while True:
        print_cards()
        choice = input(f"Player {player}, choose a card by number: ")
        if not choice.isdigit():
            print("Invalid input. Enter a number.")
            continue
        choice = int(choice) - 1
        if choice < 0 or choice >= len(cards):
            print("Invalid choice. Try again.")
            continue
        if elixir < cards[choice]['cost']:
            print(f"Not enough elixir! You have {elixir}, need {cards[choice]['cost']}.")
            continue
        return choice

print("Clash!")
print("Win.")

while player1_health > 0 and player2_health > 0:
    # Player 1's turn
    print("\nPlayer 1's turn:")
    print(f"Your tower: {player1_health}, Opponent tower: {player2_health}")
    print(f"Your elixir: {p1_elixir}")
    choice = get_choice(1, p1_elixir)
    p1_elixir -= cards[choice]['cost']
    player2_health -= cards[choice]['dmg']
    print(f"You played {cards[choice]['name']}, dealt {cards[choice]['dmg']} damage!")
    print(f"Your elixir left: {p1_elixir}")
    if player2_health <= 0:
        print("Player 1 wins!")
        break

    # Elixir regen (optional, you can remove or adjust this mechanic)
    p1_elixir = min(p1_elixir + 2, 9)
    p2_elixir = min(p2_elixir + 2, 9)

    # Player 2's turn
    print("\nPlayer 2's turn:")
    print(f"Your tower: {player2_health}, Opponent tower: {player1_health}")
    print(f"Your elixir: {p2_elixir}")
    choice = get_choice(2, p2_elixir)
    p2_elixir -= cards[choice]['cost']
    player1_health -= cards[choice]['dmg']
    print(f"You played {cards[choice]['name']}, dealt {cards[choice]['dmg']} damage!")
    print(f"Your elixir left: {p2_elixir}")
    if player1_health <= 0:
        print("Player 2 wins!")
        break


