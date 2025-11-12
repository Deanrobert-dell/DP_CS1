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
meal1 = Food["drinks"][drink]

print("meals options are: ")
print(Food["meals"])
meal = input("choose a meal from the list: ")
print(f"cost of main meal is {Food["meals"][meal]}")

meal2 = Food["meals"][meal]


print("sandwiches options are: ")
print(Food["sandwiches"])
sandwich = input("choose a sandwich from list: ")
print(f"cost of sandwich is {Food["sandwiches"][sandwich]}")

meal3 = Food["sandwiches"][sandwich]

print ("price of meal is", meal2 + meal1 + meal3, "dollars")
price = (meal2 + meal1 + meal3)
percent1 = (price*.10)
percent2 = (price * .25)


tip = input("would you like to add a tip Y or N: ")
        
if tip == "Y":
    amount = input(f"10 percent (type 1) for extra {percent1} or 25 percent(type 2) for {percent2} dollars: ")
    if amount == 1:
        print("new order costs: ", price + percent1, "dollars")
    elif amount ==2:
        print("new order costs: ", price + percent2, "dollars")
else:
    print ("BYE BYE")

