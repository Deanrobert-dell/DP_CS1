#DP 2nd Squared Numbers

nums = [3, 7, 12, 25, 30, 45, 50, 65, 70, 85, 90, 105, 110, 125, 130, 145, 150, 165, 170, 185, 190, 205, 210, 225, 230, 245, 250, 265, 270, 285]


divided = []
"""for num in numbers:
    divided.append(num/2)"""

"""def divide(number):
    return number/2"""

divided = list(map(lambda num: num/2, numbers))

for i, num in enumerate(numbers):
    print(f"{num} divided by 2 is {divided[i]}")