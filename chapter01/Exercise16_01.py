
# import turtle module
import turtle

# Use turtle module to draw the four circles
turtle.showturtle()

turtle.penup()
turtle.goto(50, 50)
turtle.pendown()
turtle.circle(50)

turtle.penup()
turtle.goto(-50, 50)
turtle.pendown()
turtle.circle(50)

turtle.penup()
turtle.goto(-50, -50)
turtle.pendown()
turtle.circle(50)

turtle.penup()
turtle.goto(50, -50)
turtle.pendown()
turtle.circle(50)

turtle.done()
