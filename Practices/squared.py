#DP 2nd Squared Numbers

#create list of numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

#function that i will call that basically sets what squared is
squared = list(map(lambda num: num*num, nums))

#for loop that goes over list
for i, num in enumerate(nums):
    print(f"original: {num} squared is {squared[i]}") #print the numbers before and after squared
