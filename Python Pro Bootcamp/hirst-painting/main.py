import random
import colorgram
import turtle as t

timmy = t.Turtle()
t.colormode(255)

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

color_list = [(248, 241, 245), (239, 247, 241), (239, 242, 247), (197, 165, 119), (144, 81, 56), (220, 201, 138), (61, 95, 121), (165, 150, 54), (136, 162, 180), (131, 34, 23), (52, 119, 87), (73, 37, 29), (190, 96, 82), (145, 177, 150), (100, 76, 80), (165, 147, 157), (21, 92, 68), (28, 59, 75), (225, 177, 167), (59, 44, 46), (133, 29, 33), (180, 202, 179), (26, 84, 89), (88, 147, 129), (13, 70, 58), (42, 65, 89), (180, 99, 102), (216, 181, 186), (182, 191, 204)]

timmy.shape("circle")
timmy.pensize(20)
timmy.speed("fastest")

y_cor = 0
for i in range(9):
    for j in range(9):
        timmy.color(random.choice(color_list))
        timmy.stamp()
        timmy.penup()
        timmy.forward(50)

    timmy.goto(0, y_cor)
    y_cor = y_cor - 50


screen = t.Screen()
screen.exitonclick()
