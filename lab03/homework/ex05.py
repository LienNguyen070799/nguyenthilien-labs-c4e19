def draw_star(x,y,length) :
    import turtle
    turtle.penup()
    turtle.setposition(x,y)
    turtle.pendown()
    for i in range(5) :
        turtle.forward(length)
        turtle.left(144)
    turtle.mainloop()
draw_star(110,30,100)