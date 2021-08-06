import turtle

links = ["red", "orange", "yellow", "green", "blue", "purple"]
sides = 6

weaver = turtle.Turtle()
weaver.width(5)
weaver.speed(0)
weaver.color('orange')

# Move back so the chain is centered.
weaver.penup()
weaver.back(80)
weaver.pendown()

for link in links:
    weaver.color(link)
    # Draw a hexagon.
    for side in range(sides):
        weaver.forward(50)
        weaver.right(360 / sides)

    # Scoot over to the next link.
    weaver.penup()
    weaver.forward(20)
    weaver.left(60)
    weaver.pendown()

# ----------------------------------
# Draw a Triangle 
weaver.color("cyan")
weaver.penup()
weaver.forward(230)
weaver.pendown()

for side in range(22):
    weaver.forward(side * 10)
    weaver.right(120)

weaver.penup()
weaver.right(60)
weaver.forward(105)
weaver.right(90)
weaver.forward(70)
weaver.right(90)
weaver.pendown()

for side in range(22):
    weaver.forward(side * 10)
    weaver.left(120)


weaver.hideturtle()
turtle.done()
