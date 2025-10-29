import turtle
import random
screen=turtle.Screen()
screen.setup(1500,900)
t1= turtle.Turtle()
t2= turtle.Turtle()
t3= turtle.Turtle()
t4= turtle.Turtle()
t5= turtle.Turtle()
winner = False

t1.setpos(-500,0)
t2.setpos(-500,100)
t3.setpos(-500,200)
t4.setpos(-500,300)
t5.setpos(-500,400)

while winner == False:
    speed1 = random.randint(1,5)
    speed2 = random.randint(1,5)
    speed3 = random.randint(1,5)
    speed4 = random.randint(1,5)
    speed5 = random.randint(1,5)
    move1 = random.randint(1,100)
    move2 = random.randint(1,100)
    move3 = random.randint(1,100)
    move4 = random.randint(1,100)
    move5 = random.randint(1,100)
    
    t1.speed(speed1)
    t1.shape("turtle")
    t1.color ("red")
    t1.forward(move1)
    if t1.xcor() > 700:
        print ("turtle one won")
        winner==True
    
    t2.speed(speed2)
    t2.shape("turtle")
    t2.color ("orange")
    t2.forward(move2)
    if t2.xcor() > 700:
        print ("turtle two won")
        winner==True
    
    t3.speed(speed3)
    t3.shape("turtle")
    t3.color ("yellow")
    t3.forward(move3)
    if t3.xcor() > 700:
        print ("turtle three won")
        winner==True
    
    t4.speed(speed4)
    t4.shape("turtle")
    t4.color ("green")
    t4.forward(move4)
    if t4.xcor() > 700:
        print ("turtle four won")
        winner==True
    t5.speed(speed4)
    t5.shape("turtle")
    t5.color ("blue")
    t5.forward(move5)
    if t5.xcor() > 700:
        print ("turtle five won")
        winner==True




turtle.done()