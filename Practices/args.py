#DP cs flex calc 2nd
import math
#import math to use math stuff
def calculator(*numbers):
    # create funstion with asterisk for arg
    if not numbers:
        input_numbers = input("type numbers separated by spaces, ex: 1 5 98: ")
        numbers = tuple(map(float, input_numbers.split()))  # change numbers to a float wit decimal
    else:
        # make sure numberts are real numbers
        numbers = tuple(float(num) for num in numbers)

    print(numbers)  # Debug print

# create if statemsnts for each operation using f strings
    options = int(input("do you want to do average (1), sum(2), product(3), max(4), or minimum(5): "))
    if options == 1:
        average = sum(numbers) / len(numbers)
        print(f"The average is: {average}")
    elif options == 2:
        total = sum(numbers)
        print(f"the sum is : {total}")
    elif options == 3:
        mult = math.prod(numbers)
        print(f"product of numbers is: {mult}")
    elif options == 4:
        high = max(numbers)
        print(f"the highest number is: {high}")
    elif options == 5:
        low = min(numbers)
        print(f"the lowest number is: {low}")
    else:
        print("bad input")
    
calculator()
