import math

def drawCircle(t, centerX, centerY, radius):
    """Draws a circle with the given center coordinates and radius using a Turtle object."""

    t.up()
    t.goto(centerX, centerY - radius)  
    t.down()

    step_distance = 2.0 * math.pi * radius / 120.0

    for _ in range(120):
        t.forward(step_distance)
        t.left(3)
        
from turtle import Turtle, Screen
from circle import drawCircle

screen = Screen()
t = Turtle()

drawCircle(t, 100, 100, 50)

screen.mainloop()
