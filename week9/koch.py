from turtle import Turtle, Screen

def drawFractalLine(t, distance, angle, level):
    """Recursively draws a fractal line (Koch curve) with the given distance, angle, and level."""
    if level == 0:
        t.setheading(angle)
        t.forward(distance)
    else:
        drawFractalLine(t, distance / 3, angle, level - 1)
        drawFractalLine(t, distance / 3, angle + 60, level - 1)
        drawFractalLine(t, distance / 3, angle - 60, level - 1)
        drawFractalLine(t, distance / 3, angle, level - 1)

def main():
    
    screen = Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("white")  
    t = Turtle()
    t.speed(0)  
    t.hideturtle()  
    t.penup()
    t.goto(-150, 100)  
    t.pendown()

    initial_distance = 300 
    levels = 3  

    for initial_angle in [0, -120, 120]:
        drawFractalLine(t, initial_distance, initial_angle, levels)

    t.setheading(0)
    drawFractalLine(t, initial_distance, 0, levels)

    screen.mainloop()

if __name__ == "__main__":
    main()
