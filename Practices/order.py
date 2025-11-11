#DP 2nd prder up

cost = 0

Food = {"sandwiches": {"hamburger": 4.99, "BLT": 3.99, "grilled-cheese": 2.99, "lobster-rolls": 9.99 },
        "drinks": {"sprite": 1.99, "water": 0.00, "coffee": 3.99, "Apple-juice": .99 },
        "meals": {"steak": 7.99, "pizza": 4.99, "lasagna": 6.99, "crocodile-liver": 19.99 }
        }
print("drink options are: ")
print(Food["drinks"])
drink = input("choose a drink from that list: ")
print(f"cost of drink is {Food["drinks"][drink]}")

print("meals options are: ")
print(Food["meals"])
meal = input("choose a meal from the list: ")
print(f"cost of main meal is {Food["meals"][meal]}")

print("sandwiches options are: ")
print(Food["sandwiches"])
sandwich = input("choose a sandwich from list: ")
print(f"cost of sandwich 1  is {Food["sandwiches"][sandwich]}")


