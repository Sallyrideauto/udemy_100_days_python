import random
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def counter_clockwise():
    left_degree = random.randint(1, 360)
    tim.left(left_degree)

def clockwise():
    right_degree = random.randint(1, 360)
    tim.right(right_degree)

def clear_drawing():
    tim.reset()

screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()