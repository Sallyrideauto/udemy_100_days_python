import random
import turtle
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -70, -40, -10, 20, 50]
all_turtles = []

# mamechi = Turtle(shape="turtle")
# mamechi.penup()
# mamechi.color("red")
# mamechi.goto(x=-230, y=-100)
#
# bira = Turtle(shape="turtle")
# bira.penup()
# bira.color("orange")
# bira.goto(x=-230, y=-70)
#
# moco = Turtle(shape="turtle")
# moco.penup()
# moco.color("yellow")
# moco.goto(x=-230, y=-40)
#
# yanukami = Turtle(shape="turtle")
# yanukami.penup()
# yanukami.color("green")
# yanukami.goto(x=-230, y=-10)
#
# rain = Turtle(shape="turtle")
# rain.penup()
# rain.color("blue")
# rain.goto(x=-230, y=20)
#
# chimata = Turtle(shape="turtle")
# chimata.penup()
# chimata.color("purple")
# chimata.goto(x=-230, y=50)

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()