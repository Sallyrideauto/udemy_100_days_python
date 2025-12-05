from turtle import Turtle

STARTING_POSITIONS = [(350, 0), (-350, 0)]
MOVE_DISTANCE = 20

class Paddle(Turtle):

    def __init__(self, position):
        # Make paddle
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)