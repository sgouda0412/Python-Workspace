import turtle

turt = turtle.Turtle()
turt.speed(10)

for i in range(180):
    turt.color("red")
    turt.forward(100)
    turt.right(30)
    turt.color("blue")
    turt.forward(20)
    turt.right(60)
    turt.color("green")
    turt.forward(50)
    turt.right(30)
    turt.penup()
    turt.setposition(0, 0)
    turt.pendown()
    turt.right(2)
turtle.done()
