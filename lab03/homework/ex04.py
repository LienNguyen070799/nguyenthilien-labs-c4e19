from turtle import *
def draw_square(length, square_color) :
    import turtle
    turtle.color(square_color)
    for i in range(4):
        turtle.forward(length)
        turtle.left(90)
# speed(-1)
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
# mainloop()