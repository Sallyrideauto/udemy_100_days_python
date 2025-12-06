from turtle import Turtle
import random

COLORS = ["#FCF7FF", "#C4CAD0", "#878C8F", "#A4969B", "#655560", "#73646E"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_MARGIN = 50

class CarManager():

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle("square")
        new_car.penup()

        # 40*20
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.color(random.choice(COLORS))

        # y scope
        y_min = -300 + Y_MARGIN
        y_max = 300 - Y_MARGIN
        random_y = random.randint(y_min, y_max)

        # x is start from right edge
        start_x = 300 - 20
        new_car.goto(start_x, random_y)

        # setting to move left
        new_car.setheading(180)

        self.all_cars.append(new_car)

    def move_cars(self):
        # moving all of cars with regular speed
        for car in self.all_cars:
            car.forward(self.car_speed)

        # remove car out of left side
        self.remove_offscreen_cars()

    def remove_offscreen_cars(self):
        cars_to_keep = []
        left_limit = -300 - 40

        for car in self.all_cars:
            if car.xcor() > left_limit:
                cars_to_keep.append(car)
            else:
                car.hideturtle()
        self.all_cars = cars_to_keep

    def level_up(self):
        # increasing speed by level up
        self.car_speed += MOVE_INCREMENT