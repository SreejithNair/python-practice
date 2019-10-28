
import turtle

wn = turtle.Screen()
wn.bgcolor("PeachPuff")        # set the window background color
anay = turtle.Turtle()
anay.pensize(3)
anay.color("blue")              # make tess blue
for i in range(1,5,1):
    anay.left(0.00)
    anay.forward(45)
    anay.left(90)
    anay.forward(45)
    anay.left(90)
    anay.forward(90)
    
wn.exitonclick()    