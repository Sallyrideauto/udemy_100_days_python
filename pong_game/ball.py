from turtle import Turtle
from scoreboard import Scoreboard

scoreboard = Scoreboard()

# Make moving ball
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

        # move speed vector
        self.x_move = 10
        self.y_move = 10

        # screen boundary
        self.top_limit = 290
        self.bottom_limit = -290
        self.right_limit = 390
        self.left_limit = -390

        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

        # Detect collision with wall and bounce
        if self.ycor() > self.top_limit or self.ycor() < self.bottom_limit:
            self.bounce_y()

        # Detect when paddle misses
        if self.xcor() > self.right_limit:
            self.score_left()
            scoreboard.l_point()
        elif self.xcor() < self.left_limit:
            self.score_right()
            scoreboard.r_point()

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9  # 공이 튕길 때마다 점차적으로 속도 증가

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

    def score_left(self):
        print("Left Win!")
        self.reset_position()

    def score_right(self):
        print("Right Win!")
        self.reset_position()