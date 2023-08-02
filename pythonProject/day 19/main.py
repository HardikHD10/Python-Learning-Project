from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()


# screen.listen()
# screen.onkey(key="space",fun=moveforward)
# screen.exitonclick()

def moveforward():
    tim.forward(10)

def movebackward():
    tim.backward(10)

def clearscreen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def counterclockwise():
    new_heading = tim.heading() + 90
    tim.setheading(new_heading)

def clockwise():
    new_heading = tim.heading() + 180
    tim.setheading(new_heading)

screen.listen()
screen.onkey(key="w",fun=moveforward)
screen.onkey(key="s",fun=movebackward)
screen.onkey(key="a",fun=counterclockwise)
screen.onkey(key="d",fun=clockwise)
screen.onkey(key="c",fun=clearscreen)
screen.exitonclick()



