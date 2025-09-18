from turtle import *


def triangle(h):
    begin_fill()
    for i in range(3):
        forward(h)
        left(120)
    end_fill()


def sierpinski_triangle(n, h):
    if n == 1:
        triangle(h)
    else:
        sierpinski_triangle(n - 1, h / 2)
        left(60)
        forward(h / 2)
        right(60)
        sierpinski_triangle(n - 1, h / 2)
        right(60)
        forward(h / 2)
        left(60)
        sierpinski_triangle(n - 1, h / 2)
        backward(h / 2)


speed(0)
sierpinski_triangle(5, 1000)
exitonclick()
