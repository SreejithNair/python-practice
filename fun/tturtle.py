
import turtle

wn = turtle.Screen()
wn.bgcolor("PeachPuff")        # set the window background color
anay = turtle.Turtle()
anay.pensize(3)
anay.color("blue")              # make tess blue
for i in range(1,5,1):
    anay.forward(50.00)
    anay.right(90)
    anay.forward(50.00)
    anay.right(90)
    anay.forward(50.00)
    anay.right(90)
    anay.forward(50.00)
    anay.left(45.00)
    anay.forward(50.00)
wn.exitonclick()    