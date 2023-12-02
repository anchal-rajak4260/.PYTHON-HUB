#Python program to draw star 
#using Turtle Programming
import turtle

star = turtle.Turtle()

star.right(75)
star.forward(100)

for i in range (4):
    star.right(144)
    star.forward(100)

    # code for inner lines of the star
star.penup()
star.setpos(-90,30)
star.pendown()

star.penup()
star.setpos(80,-140)
star.pendown()

turtle.done()
