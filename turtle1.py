import turtle
import random

space = random.randint(1,4)




box= turtle.Turtle()
box.setpos(-230,0)
box.penup()
box.forward(-40)
box.pendown()
box.forward(-230)
box.left (90)
box.forward (500)
box.right(90)
box.forward (230)
box.penup()
box.forward(40)
box.pendown()
box.forward(230)
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

line.penup()
line.setpos(-500,50)
line.pendown()
line.forward(460)

line1.penup()
line1.setpos(-500,100)
line1.pendown()
line1.forward(460)

line2.penup()
line2.setpos(-500,150)
line2.pendown()
line2.forward(460)

line3.penup()
line3.setpos(-500,200)
line3.pendown()
line3.forward(460)

line4.penup()
line4.setpos(-500,250)
line4.pendown()
line4.forward(460)

line5.penup()
line5.setpos(-500,300)
line5.pendown()
line5.forward(460)

line6.penup()
line6.setpos(-500,350)
line6.pendown()
line6.forward(460)

line7.penup()
line7.setpos(-500,400)
line7.pendown()
line7.forward(460)

line8.penup()
line8.setpos(-500,450)
line8.pendown()
line8.forward(460)














turtle.done()