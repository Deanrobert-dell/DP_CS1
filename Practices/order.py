#DP 2nd prder up

#make dictionary of food
Food = {"sandwiches": {"hamburger": 4.99, "BLT": 3.99, "grilled-cheese": 2.99, "lobster-rolls": 9.99, "none": 0.00 },
        "drinks": {"sprite": 1.99, "water": 0.00, "coffee": 3.99, "Apple-juice": .99 },
        "meals": {"steak": 7.99, "pizza": 4.99, "lasagna": 6.99, "crocodile-liver": 19.99 }
        }

#options for drinks
print("drink options are: ")
print(Food["drinks"])
drink = input("choose a drink from that list: ")
print(f"cost of drink is {Food['drinks'][drink]}") #take value of drink that i inputted
meal1 = Food["drinks"][drink]

#options for meals
print("meals options are: ")
print(Food["meals"])
meal = input("choose a meal from the list: ")
print(f"cost of main meal is {Food['meals'][meal]}")#take value of meal that i inputted
meal2 = Food["meals"][meal]

#2 options for side dishes
print("sandwiches options are: ")
print(Food["sandwiches"])
sandwich = input("choose a sandwich from list: ")
print(f"cost of sandwich is {Food['sandwiches'][sandwich]}")#take value of sandwich that i inputted
sandwich2 = input("choose a second sandwich: ")
print(f"cost of sandwich 2 is {Food['sandwiches'][sandwich2]}")#take value of sandwich 2 that i inputted
meal3 = Food["sandwiches"][sandwich]
meal4 = Food["sandwiches"][sandwich2]

#calculate price and tip percentages
print ("price of meal is", meal2 + meal1 + meal3 + meal4, "dollars")
price = (meal2 + meal1 + meal3+ meal4)
percent1 = (price*.10)
percent2 = (price * .25) #find percentage by multipling price in a seperate variable by a decimal

#ask for tip
tip = input("would you like to add a tip Y or N: ")
        


#if statement for tips
if tip == "Y":
    amount = int(input("10 percent (type 1), or 25 percent(type 2) "))
    if amount == 1:
        print("new order costs: ", price + percent1, "dollars")
    elif amount == 2:
        print("new order costs: ", price + percent2, "dollars")
    else:
        print("invalid input")
else:
    print ("BYE BYE")#no tip option

