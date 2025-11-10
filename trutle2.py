import turtle
import random

def turtlemaze():
    box= turtle.Turtle()
    box.speed(0)
    box.hideturtle()
    box.setpos(-200,0)
    box.penup()
    box.forward(-50)
    box.pendown()
    box.forward(-250)
    box.left (90)
    box.forward (500)
    box.right(90)
    box.forward (250)
    box.penup()
    box.forward(50)
    box.pendown()
    box.forward(200)
    box.right(90)
    box.forward(500)
    
    line = turtle.Turtle()
    line1 = turtle.Turtle()
    line2 = turtle.Turtle()
    line3 = turtle.Turtle()
    line4 = turtle.Turtle()
    line5 = turtle.Turtle()
    line6 = turtle.Turtle()
    line7 = turtle.Turtle()
    line8 = turtle.Turtle()
    line9 = turtle.Turtle()
    
    up = turtle.Turtle()
    up1 = turtle.Turtle()
    up2 = turtle.Turtle()
    up3 = turtle.Turtle()
    up4 = turtle.Turtle()
    up5 = turtle.Turtle()
    up6 = turtle.Turtle()
    up7 = turtle.Turtle()
    up8 = turtle.Turtle()
    up9 = turtle.Turtle()
    
    line.speed(0)
    line1.speed(0)
    line2.speed(0)
    line3.speed(0)
    line4.speed(0)
    line5.speed(0)
    line6.speed(0)
    line7.speed(0)
    line8.speed(0)
    line9.speed(0)
    
    up.speed(0)
    up1.speed(0)
    up2.speed(0)
    up3.speed(0)
    up4.speed(0)
    up5.speed(0)
    up6.speed(0)
    up7.speed(0)
    up8.speed(0)
    up9.speed(0)
    
    line.hideturtle()
    line1.hideturtle()
    line2.hideturtle()
    line3.hideturtle()
    line4.hideturtle()
    line5.hideturtle()
    line6.hideturtle()
    line7.hideturtle()
    line8.hideturtle()
    line9.hideturtle()
    
    up.hideturtle()
    up1.hideturtle()
    up2.hideturtle()
    up3.hideturtle()
    up4.hideturtle()
    up5.hideturtle()
    up6.hideturtle()
    up7.hideturtle()
    up8.hideturtle()
    up9.hideturtle()
    
    up.penup()
    up.setpos(-450,0)
    up.left(90)

    
    while up.ycor() < 500:
        rand=random.randint(1,2)
        if rand == 1:
            up.penup()
            up.forward(50)
        else:
            up.pendown()
            up.forward(50)
    
    up1.penup()
    up1.setpos(-400,0)
    up1.left(90)
    while up1.ycor() < 500:
        rand=random.randint(1,2)
        if rand == 1:
            up1.penup()
            up1.forward(50)
        else:
            up1.pendown()
            up1.forward(50)
    
    up2.penup()
    up2.setpos(-350,0)
    up2.left(90)
    while up2.ycor() < 500:
        rand=random.randint(1,2)
        if rand == 1:
            up2.penup()
            up2.forward(50)
        else:
            up2.pendown()
            up2.forward(50)
    
    up3.penup()
    up3.setpos(-300,0)
    up3.left(90)
    while up3.ycor() < 500:
        rand=random.randint(1,2)
        if rand == 1:
            up3.penup()
            up3.forward(50)
        else:
            up3.pendown()
            up3.forward(50)
    
    up4.penup()
    up4.setpos(-250,0)
    up4.left(90)
    while up4.ycor() < 500:
        rand=random.randint(1,2)
        if rand == 1:
            up4.penup()
            up4.forward(50)
        else:
            up4.pendown()
            up4.forward(50)
    
    up5.penup()
    up5.setpos(-200,0)
    up5.left(90)
    while up5.ycor() < 500:
        rand=random.randint(1,2)
        if rand == 1:
            up5.penup()
            up5.forward(50)
        else:
            up5.pendown()
            up5.forward(50)
    
    up6.penup()
    up6.setpos(-150,0)
    up6.left(90)
    while up6.ycor() < 500:
        rand=random.randint(1,2)
        if rand == 1:
            up6.penup()
            up6.forward(50)
        else:
            up6.pendown()
            up6.forward(50)
    
    up7.penup()
    up7.setpos(-100,0)
    up7.left(90)
    while up7.ycor() < 500:
        rand=random.randint(1,2)
        if rand == 1:
            up7.penup()
            up7.forward(50)
        else:
            up7.pendown()
            up7.forward(50)
    
    up8.penup()
    up8.setpos(-50,0)
    up8.left(90)
    while up8.ycor() < 500:
        rand=random.randint(1,2)
        if rand == 1:
            up8.penup()
            up8.forward(50)
        else:
            up8.pendown()
            up8.forward(50)
    
    line.penup()
    line.setpos(-500,50)
    while line.xcor() < 0:
        rand=random.randint(1,2)
        if rand == 1:
            line.penup()
            line.forward(50)
        else:
            line.pendown()
            line.forward(50)
    
    line1.penup()
    line1.setpos(-500,100)
    while line1.xcor() < 0:
        rand=random.randint(1,2)
        if rand == 1:
            line1.penup()
            line1.forward(50)
        else:
            line1.pendown()
            line1.forward(50)
    
    line2.penup()
    line2.setpos(-500,150)
    while line2.xcor() < 0:
        rand=random.randint(1,2)
        if rand == 1:
            line2.penup()
            line2.forward(50)
        else:
            line2.pendown()
            line2.forward(50)
    
    line3.penup()
    line3.setpos(-500,200)
    while line3.xcor() < 0:
        rand=random.randint(1,2)
        if rand == 1:
            line3.penup()
            line3.forward(50)
        else:
            line3.pendown()
            line3.forward(50)
    
    line4.penup()
    line4.setpos(-500,250)
    while line4.xcor() < 0:
        rand=random.randint(1,2)
        if rand == 1:
            line4.penup()
            line4.forward(50)
        else:
            line4.pendown()
            line4.forward(50)
    
    line5.penup()
    line5.setpos(-500,300)
    while line5.xcor() < 0:
        rand=random.randint(1,2)
        if rand == 1:
            line5.penup()
            line5.forward(50)
        else:
            line5.pendown()
            line5.forward(50)
    
    line6.penup()
    line6.setpos(-500,350)
    while line6.xcor() < 0:
        rand=random.randint(1,2)
        if rand == 1:
            line6.penup()
            line6.forward(50)
        else:
            line6.pendown()
            line6.forward(50)
    
    line7.penup()
    line7.setpos(-500,400)
    while line7.xcor() < 0:
        rand=random.randint(1,2)
        if rand == 1:
            line7.penup()
            line7.forward(50)
        else:
            line7.pendown()
            line7.forward(50)
    
    line8.penup()
    line8.setpos(-500,450)
    while line8.xcor() < 0:
        rand=random.randint(1,2)
        if rand == 1:
            line8.penup()
            line8.forward(50)
        else:
            line8.pendown()
            line8.forward(50)
    
    turtle.done()
turtlemaze()
