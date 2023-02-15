import turtle
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def turn_clockwise():
    timmy.left(90)

def turn_counter_clockwise():
    timmy.right(90)

def clear_drawing():
    screen.clearscreen()
    turtle.goto(0, 0)

screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_clockwise)
screen.onkey(key="d", fun=turn_counter_clockwise)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()