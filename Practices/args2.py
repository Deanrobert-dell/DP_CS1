numbers = [2,12,21,321,3,2,13,21,32,1]
divided = []
"""for num in numbers:
    divided.append(num/2)"""

"""def divide(number):
    return number/2"""

divided = list(map(lambda num: num/2, numbers))

for i, num in enumerate(numbers):
    print(f"{num} divided by 2 is {divided[i]}")




