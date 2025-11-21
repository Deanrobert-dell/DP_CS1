"""defin function calld find factorial then multiply number by number -1, call it num-1
"num-1"
"num-2"
"num-3"
"num-4"
over and over once it hits 0 show most recent number return number also original number


make variable called number, ask user for number
check if its an integer if not ask again so basically make a while loop until you can call the function"""








def find_factorial():
    while True:   #while loop
        num = num-1
        num2 = num-2
        num3 = num-3
        num4 = num-4
        num5 = num-5
        num6 = num-6
        num7 = num-7
        num8 = num-8
        num9 = num-9
        num10 = num-10
        num11 = num-11
        num12 = num-12
        num13 = num-13
        num14 = num-14
        num15 = num-15
        num16 = num-16
        num17 = num-17
        num18 = num-18
        num19 = num-19
        num20 = num-20
        if num <= 0:
            print (num)
            print (num*num2*num3*num4*num5*num6*num7*num8*num9*num10*num11*num12*num13*num14*num15*num16*num17*num18*num19*num20)
            break


while True: #while loop to be able to ask use rto input new input
    num = input("enter a number to be factored:") #specify that it will be factored
    if num.isdigit():
        print("please enter valid integer")
        continue
    elif num.is_integer():
        find_factorial()
        

