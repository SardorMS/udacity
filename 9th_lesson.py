# Wandering  multicolorful turtle
import turtle
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

t = turtle.Turtle()
t.width(20)

for step in range(100):
    
    t.color(random.choice(colors))
    t.right(random.randint(1, 6))
    t.forward(10)
