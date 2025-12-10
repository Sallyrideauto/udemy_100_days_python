import turtle
import pandas as pd
from PIL import Image

class StateGame:
    def __init__(self, image_path: str, csv_path: str, final_output: str):
        self.screen = turtle.Screen()
        self.screen.title("Alberta Regions Game")

        image = "alberta_map_clean.gif"

        # Read image size
        img = Image.open(image_path)
        img_width, img_height = img.size

        # Adjust window size
        self.screen.setup(width=img_width, height=img_height)

        # Show Picture on Screen
        self.screen.addshape(image_path)
        turtle.shape(image)

        # Load CSV Data
        self.regions_data = pd.read_csv(csv_path)
        self.all_regions = self.regions_data["region"].to_list()   # All Alberta Regions
        self.guessed_regions: list[str] = []    # Guessed Regions

        # Text Output Turtle
        self.writer = turtle.Turtle()
        self.writer.hideturtle()
        self.writer.penup()

        # Export CSV File name
        self.final_output = final_output

    def ask_region(self, first: bool = False) -> str | None:
        # If 1st Question, 'Guess the Region', after showing score
        if first:
            title = "Guess the Region of Alberta"
        else:
            title = f"{len(self.guessed_regions)}/{len(self.all_regions)} Regions Correct"

        answer = self.screen.textinput(
            title = title,
            prompt = "What's another region's name? (Type 'Exit' to quit)"
        )

        return answer.title() if answer else None

    def write_region_on_map(self, region_name: str) -> None:
        # Print Region Name
        row = self.regions_data[self.regions_data["region"] == region_name]
        x, y = int(row.iloc[0]["x"]), int(row.iloc[0]["y"])

        self.writer.goto(x, y)
        self.writer.write(region_name, align="center", font=("Arial", 8, "normal"))

    def save_results(self) -> None:
        # Save CSV File
        guessed_regions_list = [region for region in self.all_regions if region in self.guessed_regions]
        missed_regions_list = [region for region in self.all_regions if region not in self.guessed_regions]

        guessed_df = pd.DataFrame(guessed_regions_list, columns=["region"])
        guessed_df["status"] = "guessed"
        missed_df = pd.DataFrame(missed_regions_list, columns=["region"])
        missed_df["status"] = "missed"

        result_df = pd.concat([guessed_df, missed_df])
        result_df.to_csv(self.final_output, index=False)

    def run(self):
        # Run Game
        region = self.ask_region(first=True) # 1st Input

        if region and region in self.all_regions and region not in self.guessed_regions:
            self.guessed_regions.append(region)
            self.write_region_on_map(region)

        # Repeat Input Loop
        while len(self.guessed_regions) < len(self.all_regions):
            region = self.ask_region(first=False)

            if not region or region == "Exit":
                break

            if region in self.all_regions and region not in self.guessed_regions:
                self.guessed_regions.append(region)
                self.write_region_on_map(region)

        self.save_results()
        self.screen.exitonclick()

