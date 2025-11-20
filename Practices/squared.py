#DP 2nd Squared Numbers

#create list of numbers
nums = [3, 7, 12, 25, 30, 45, 50, 65, 70, 85, 90, 105, 110, 125, 130, 145, 150, 165, 170, 185, 190, 205, 210, 225, 230, 245, 250, 265, 270, 285]

#function that i will call that basically sets what squared is
squared = list(map(lambda num: num*num, nums))

#for loop that goes over list
for i, num in enumerate(nums):
    print(f"original: {num} squared is {squared[i]}") #print the numbers before and after squared
