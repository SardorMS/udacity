# Stairs
import turtle

t = turtle.Turtle()
t.color("limegreen")
t.width(5)
t.speed(0)

t.penup()
t.back(150)
t.right(90)
t.forward(150)
t.left(90)
t.pendown()


for side in range(50):
    t.forward(10)
    if side % 2 == 0:
        t.left(90)
    else:
        t.right(90)

t.hideturtle()
turtle.done()
