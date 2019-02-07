from turtle import *
from random import *
def randomcolor():
    red = int(randint(0,255))
    green = int(randint(0,255))
    blue = int(randint(0,255))
    color(red,green,blue)
    
def randomPlace():
    penup()
    x = randint(-100,100)
    y = randint(-100,100)
    goto(x,y)
    pendown()
    
def randomHeading():
    a = randint(0,120)
    right(a)

shape('turtle')
for x in range(30):
    randomcolor()
    randomPlace()
    randomHeading()
    stamp()
