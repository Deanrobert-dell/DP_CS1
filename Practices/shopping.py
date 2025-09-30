# DP 2nd Shopping List Manager

shopping_list=[]

while True:
    print("shopping list contains", shopping_list)
    action=input("do you want to add to list (1) remove item from list (2) view list (3) or exit (4): ")
    if action == "1":
        add = input("what do you want to add: ")
        shopping_list.append(add)
        print ("shopping list is now: ",shopping_list)
        #adds item to list from input
    elif action == "2":
        print("removeable items are,", shopping_list)
        remove = input("what do you want to remove: ")
        if remove not in shopping_list:
            print ("invalid item")
        else:
            break
        shopping_list.remove(remove)
        print ("shopping list is now: ",shopping_list)
        #removes item from list by input
    elif action == "3":
        print("shopping list is", shopping_list)
    #option to print list
    elif action == "4":
        print ("bye bye")
        break
    #closes loop
    else:
        print("invalid")
    #ensures no iunvalid code is inputed


