from turtle import *
def drawSquare(x, y):
    penup()
    setposition(x, y)
    pendown()

    length = 100
    angle = 90

    forward(length)
    right(angle)
    forward(length)
    right(angle)
    forward(length)
    right(angle)
    forward(length)
    right(angle)

drawSquare(90,100)
drawSquare(40,160)
drawSquare(10,90)
drawSquare(60,65)
drawSquare(10,90)
done()
