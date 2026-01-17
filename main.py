import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Drawing Shapes with Turtle")

my_pen = turtle.Turtle()
my_pen.pensize(3)

my_pen.color("hotpink")
for _ in range(3):
    my_pen.forward(100)
    my_pen.left(120)

my_pen.penup()
my_pen.forward(150)
my_pen.pendown()

my_pen.color("blue")
length = 200
width = 100
for _ in range(2):
    my_pen.forward(length)
    my_pen.left(90)
    my_pen.forward(width)
    my_pen.left(90)


my_pen.penup()
my_pen.forward(250)
my_pen.pendown()

my_pen.color("red")
for _ in range(6):
    my_pen.forward(100)
    my_pen.left(60)

wn.exitonclick()