# Multicolored beads
import turtle

# Color for beads
def bead_color(num):
    if num % 3 == 0:
        return "red"
    elif num % 3 == 1:
        return "green"
    else:
        return "blue"

# Bead 
def bead(tur):
    tur.right(75)
    for _ in range(12):
        tur.forward(10)
        tur.left(30)
    tur.left(75)


t = turtle.Turtle()
t.speed(0)
t.width(2)

# Move to the left before starting.
t.penup()
t.back(200)
t.pendown()

# Draw ten beads.
for n in range(10):
    t.color(bead_color(n))
    bead(t)
    t.forward(40)
