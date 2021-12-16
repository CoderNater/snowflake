from turtle import *
import random as rand

def random_color():
    colors = str(hex(rand.randint(0,16777215)))
    colors = colors[2:]

    colors_len = len(colors)
    colors = colors[colors_len::-1]
    for i in range(6 - len(colors)):
        colors += "0"
    
    colors += "#"
    colors_len = len(colors)
    colors = colors[colors_len::-1]
    return colors

Screen().bgcolor(random_color())

amount = rand.randint(2,50)

pendown()
for i in range(amount):
    color(random_color())

    length = rand.randint(50, 200)
    degree = rand.randint(1,90)
    width(rand.randint(1,10))

    for i in range(2):
        forward(length)
        right(degree)
        forward(length)
        right(180-degree)
    right(360/amount)
done()