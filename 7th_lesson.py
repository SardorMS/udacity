# Circle of stars
import turtle

def star(color, sides, length, angle, distance):
    galileo = turtle.Turtle()
    galileo.color(color)  # colorful!
    galileo.width(3)  # visible!
    galileo.speed(0)  # fast!
    galileo.penup()
    galileo.left(angle)  # away from center
    galileo.forward(distance)
    galileo.pendown()  # start drawing
    for side in range(sides):
        galileo.forward(length)
        galileo.left(720 / sides)
    galileo.hideturtle()  # just the star


for angle in [180, 135, 90, 45, 0, -50, -95, -135]:
    star("aqua", 5, 50, angle, 100)
    star("orange", 5, 40, angle, 50)
    star("dark orange", 5, 20, angle, 20)

# ==================================================
# Increasing polygon
t = turtle.Turtle()


def polygon(sides, length):
    t.color("green")
    t.speed(0)
    angle = 360 / sides
    for side in range(sides):
        t.forward(length)
        t.right(angle)
    t.hideturtle()

t.penup()
t.right(90)
t.forward(150)
t.left(90)
t.pendown()
figure = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
for shape in figure:
    polygon(shape, 35)

turtle.done()
