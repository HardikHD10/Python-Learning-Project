import turtle
import random
from turtle import *

# timmy_the_turtle = turtle.Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")

#challenge 1
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)

#challenge 2
# distance = 0
# while (distance!=100):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()
#     distance += 10

#challenge 3
colors = ["Red","ForestGreen","Blue","GreenYellow","MidnightBlue","Purple","Lime","AliceBlue","Azure","Crimson"]
#
# def draw_shape(n):
#     angle = 360 / n
#     for i in range(n):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)
#
# for shape_side_n in range(3,11):
#     draw_shape(shape_side_n)
#     timmy_the_turtle.color(colors[shape_side_n - 2])

#challenge 4
# def North():
#     timmy_the_turtle.left(90)
#     timmy_the_turtle.forward(20)
#     timmy_the_turtle.color(colors_selector)
#
# def South():
#     timmy_the_turtle.right(90)
#     timmy_the_turtle.forward(20)
#     timmy_the_turtle.color(colors_selector)
#
# def West():
#     timmy_the_turtle.right(90)
#     timmy_the_turtle.right(90)
#     timmy_the_turtle.forward(20)
#     timmy_the_turtle.color(colors_selector)
#
# def East():
#     timmy_the_turtle.left(90)
#     timmy_the_turtle.left(90)
#     timmy_the_turtle.forward(20)
#     timmy_the_turtle.color(colors_selector)
#
#
# #directions = ["North", "South", "East", "West"]
#
# screen = Screen()
# flag = True
# while(flag):
#     directions_selector = random.randint(0, 3)
#     colors_selector = colors[random.randint(0, 9)]
#     if directions_selector == 0:
#         North()
#     elif directions_selector == 1:
#         South()
#     elif directions_selector == 2:
#         West()
#     elif directions_selector == 3:
#         East()
#     elif screen.exitonclick():
#         flag == False

timmy_the_turtle = turtle.Turtle()

# directions = [0,90,180,270]
turtle.colormode(255)
#
def random_color():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  my_tuple = (r, g, b)
  return my_tuple
#
# for _ in range(100):
#     timmy_the_turtle.color(random_color())
#     timmy_the_turtle.pensize(15)
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice(directions))
#     timmy_the_turtle.speed(50)
timmy_the_turtle.pensize(2)
timmy_the_turtle.speed(100)
angle = 5

def draw_spirograph(size_of_gap):
    for _ in range(int(360/(size_of_gap))):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        current_heading =timmy_the_turtle.heading()
        timmy_the_turtle.setheading(current_heading + size_of_gap)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()