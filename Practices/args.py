#DP 2nd flex calc

import math

def calculator(*numbers):
    numbers = input("type numbers seprataed by spaces, ex: 1 5 98: " )
    list = numbers.split()
    print(list)
    options = int(input("do you want to do average (1), sum(2), product(3), max(4), or minimum(5): "))
    if options == 1:
        average = sum(list) / len(list)
        print(f"The average is: {average}")
    elif options == 2:
        total = sum(list)
        print(f"the sum is : {total}")
    elif options == 3:
        mult = math.prod(list)
        print(f"product of numbers is: {mult}")
    elif options == 4:
        high = max(list)
        print(f"he highest number is: {high}")
    elif options == 5:
        low = min(list)
        print(f"he lowest number is: {low}")
    else:
        print("bad input")
    

calculator()