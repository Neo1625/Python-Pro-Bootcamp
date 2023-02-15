import random
import turtle as t


timmy = t.Turtle()


direction = [0, 90, 180, 270]
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

#timmy.pensize(10)
#timmy.forward(10)

#timmy.speed(8)

#for _ in range(100):
#    timmy.color(random_color())
 #   timmy.right(random.choice(direction))
 #   timmy.forward(40)

timmy.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()