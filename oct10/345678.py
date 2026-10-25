import turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("NEON MANDALA")

ground = turtle.Turtle()
ground.speed("fastest")
ground.hideturtle()


colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
for i in range(80):
    ground.color(colors[i % len(colors)])
    ground.width(2)
    ground.forward(i * 4)
    ground.right(80)

ground.penup()
ground.goto(0,-60)
ground.setheading(80)
ground.pendown()
ground.color("gold" , "yellow")
ground.begin_fill()
for i in range(5):
    ground.forward(120)
    ground.right(144)
ground.end_fill()

ground.penup()
ground.goto(0, -30)
ground.pendown()
petal_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet" , "pink", "cyan", "magenta"]
for i in range(30):
    ground.color(petal_colors[i % len(petal_colors)],
                 petal_colors[(i+2)% len(petal_colors)])
    ground.begin_fill()

    for j in range(4):
        ground.forward(60)
        ground.right(90)
    ground.end_fill()
    ground.right(72)

turtle.done()
    