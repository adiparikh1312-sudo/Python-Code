import turtle

screen = turtle.Screen()
screen.bgcolor("green")   #

cursor = turtle.Turtle()

cursor.shape("triangle")
cursor.shapesize(2, 1, 1)

cursor.fillcolor("blue")
cursor.pencolor("black")

cursor.penup()
cursor.goto(-50, -50)
cursor.pendown()

cursor.begin_fill()

cursor.goto(0, 100)
cursor.goto(25, 60)
cursor.goto(55, 120)
cursor.goto(75, 110)
cursor.goto(45, 50)
cursor.goto(100, 50)
cursor.goto(-50, -50)

cursor.end_fill()

cursor.hideturtle()

turtle.done()