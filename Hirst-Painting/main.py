# import colorgram
import turtle
from turtle import Turtle, Screen
import random
# colors = colorgram.extract('image.jpg', 30)
# extracted_colors = []
# for color in colors:
#     color_values = (color.rgb.r, color.rgb.b, color.rgb.b)
#     extracted_colors.append(color_values)
#
# print(extracted_colors)
color_list = [(198, 32, 32), (248, 25, 25), (40, 188, 188), (39, 69, 69), (238, 5, 5), (227, 49, 49),
              (29, 154, 154), (212, 15, 15), (17, 17, 17), (241, 161, 161), (195, 12, 12), (223, 120, 120),
              (68, 31, 31), (61, 8, 8), (223, 206, 206), (11, 62, 62), (219, 11, 11), (54, 229, 229), (19, 49, 49),
              (238, 216, 216), (79, 212, 212), (10, 238, 238), (73, 168, 168), (93, 198, 198), (65, 239, 239),
              (217, 51, 51)]


def draw_square_paint(width, height):
    actual_lines = 0
    while actual_lines != height:
        for _ in range(width):
            timmy.dot(20, random.choice(color_list))
            timmy.penup()
            timmy.forward(50)

        timmy.teleport(0, timmy.ycor() + 50.00)
        actual_lines += 1


turtle.colormode(255)
timmy = Turtle()
timmy.hideturtle()

draw_square_paint(6, 6)

screen = Screen()
screen.exitonclick()
