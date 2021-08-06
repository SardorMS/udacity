# Draw Rose
import turtle

def spiral(size, turn, color, width, speed):
    t = turtle.Turtle()
    t.color(color)
    t.width(width)
    t.speed(speed)
    for n in range(size):
        t.forward(n)
        t.right(turn)

    turtle.done()

spiral(200, 70, "green", 1, 0)
turtle.done()