# DP 2nd Inputs & Outputs
import time
import random
import datetime as date

print (random.random())
print (random.randint(1,20))

number = 1
while number == 2:
    print(int("4") + 1)

print ("new seat 9/17")
currenttime = time.time()
readable_time = time.ctime(currenttime)
now= date.datetime.now()
hour=now.strftime("%H ""%M")
#month %m or %B, minute %M, second %S, day %D, year %Y or %y 

print (f"Time in seconds since 1970: {currenttime}")
print (f"current time: {readable_time}")
print (f"current time: {now}")
print (F"mil time is {hour}")


nums= [1, 2, 4]

for num in nums:
    div = num/2
    if div> 100:
        print (f"{div}is half of {num}. and it is still large ")
    else:
        print (num)



for x in range(1,10):
    print (x)

print ("hello")


for x in range(2,11,2):
    print (x)

print ("countdown")


for x in range(999999,0,-1):
    print (x)
