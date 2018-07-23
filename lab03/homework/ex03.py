def draw_square(length, square_color) :
    import turtle
    turtle.color(square_color)
    for i in range(4):
        turtle.forward(length)
        turtle.left(90)
    turtle.mainloop()
    
draw_square(50, "red")

    