
# import turtle module
import turtle

# Use turtle module to draw the rectanguloid
turtle.showturtle()

turtle.goto(120, 0)
turtle.goto(150, 30)
turtle.goto(30, 30)
turtle.goto(0, 0)

turtle.goto(0, 60)
turtle.goto(120, 60)
turtle.goto(150, 90)
turtle.goto(30, 90)
turtle.goto(0, 60)

turtle.penup()
turtle.goto(30, 90)

turtle.pendown()
turtle.goto(30, 30)

turtle.penup()
turtle.goto(150, 90)

turtle.pendown()
turtle.goto(150, 30)

turtle.penup()
turtle.goto(120, 60)

turtle.pendown()
turtle.goto(120, 0)

turtle.done()
