# Using turtle, write a program to draw a spiral.
from turtle import *

# 1:
# 2: draw a demi-circle
shape("turtle")
i = 50  # loop iterations
r = 20  # starting angle

for x in range(i):
    circle(r, 180)
    r = r * 1.2

exitonclick()
