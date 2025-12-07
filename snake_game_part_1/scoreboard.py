from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

# Create a scoreboard
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt") as score_file:
            self.high_score = int(score_file.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # Save High Score
            with open("data.txt", mode="w") as score_file:
                score_file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()