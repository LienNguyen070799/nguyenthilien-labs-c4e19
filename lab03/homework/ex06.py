from turtle import *
def draw_star(x,y,length) :
    import turtle
    turtle.penup()
    turtle.setposition(x,y)
    turtle.pendown()
    for i in range(5) :
        turtle.forward(length)
        turtle.left(144)
    

speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)
