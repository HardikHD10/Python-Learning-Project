import turtle
from turtle import Turtle,Screen
import random

flag = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput("PLACE A BET","Which color of turtle you would like to place a bet on :")
colors = ["red","violet","yellow","orange","blue","green","indigo"]
y_positions = [-90,-60,-30,00,30,60,90]
all_turtle = []

for turtle_index in range(0,7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230,y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    flag = True

while(flag):


    for t in all_turtle:
        if t.xcor()>230:
            winning_turtle = t.pencolor()
            if winning_turtle == user_bet:
                print("You have placed a successful bet. Your turtle won the race!")
            else:
                print("Bet was unsuccesful! You have lost the race !")
            flag = False
        random_distance = random.randint(0,10)
        t.forward(random_distance)


screen.exitonclick()