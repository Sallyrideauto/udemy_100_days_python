from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        # Make Turtle
        super().__init__()
        self.shape("turtle")
        self.left(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def reset_position(self):
        self.goto(STARTING_POSITION)