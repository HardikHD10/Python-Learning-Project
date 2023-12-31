import turtle
import random
# import colorgram
#
# color_list = colorgram.extract("image.jpeg", 2 ** 32)
# color_palette = []
#
# for color in color_list:
#     r =color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     color_palette.append(new_color)
#
# print(color_palette)
turtle.colormode(255)
color_list = [(212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12), (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187), (151, 206, 220), (97, 127, 168), (34, 81, 49), (180, 188, 210),(84, 65, 30),(16, 77, 106)]
tim = turtle.Turtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
numbers_of_dots =100
tim.speed("fastest")
tim.hideturtle()

for dot_count in range(1, numbers_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle.Screen()
screen.exitonclick()

