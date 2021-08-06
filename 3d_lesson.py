# Square wheel
import turtle
jack = turtle.Turtle()
jack.color("green")
jack.speed(0)


def draw_square(distanse):
    for side in range(4):
        jack.forward(distanse)
        jack.right(90)


for square in range(72):
    draw_square(150)
    jack.forward(5)
    jack.left(5)

jack.hideturtle()
turtle.done()
