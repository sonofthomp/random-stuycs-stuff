import turtle
import random

raphael = turtle.Turtle()
raphael.shape('triangle')
raphael.speed(0)

raphael.color((1, 1, 0))

window = turtle.Screen()
window.bgcolor(0,0,0)

for i in range(2000):
    new_angle = random.choice([0, 90, 180, 270])
    raphael.rt(new_angle)
    
    raphael.fd(10)
