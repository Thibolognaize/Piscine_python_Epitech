""" "
Using turtle, write a function draw_polygon(sides) that takes an integer parameter sides.
The function draws a regular polygon with the given number of sides:
if sides = 3, then it draws an equilateral triangle ;
if sides = 4, then it draws a square ;
if sides = 5, then it draws a pentagon ;
if sides = 6, then it draws a hexagon ;
and so on...
"""

from turtle import *

# home()
# 360deg


def draw_polygon(sides: int, color: str = "black"):
    begin_fill()
    for i in range(sides):
        forward(200)
        left(360 / sides)
    end_fill()
    exitonclick()


# draw_polygon(3)
# draw_polygon(4)
# draw_polygon(5)
# draw_polygon(6)
draw_polygon(7)
