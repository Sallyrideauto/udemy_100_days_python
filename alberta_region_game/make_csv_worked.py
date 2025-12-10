import turtle
from PIL import Image
import pandas as pd

# Configure
IMAGE_PATH = "alberta_map.gif"
OUTPUT_CSV_FILE = "alberta_regions.csv"

# Load Screen and Image
screen = turtle.Screen()
screen.title("Make Alberta Map Coordinate")

# Fit Window Size by Image
img = Image.open(IMAGE_PATH)
img_width, img_height = img.size
screen.setup(width=img_width, height=img_height)

# Show Map Image on Background
screen.bgpic(IMAGE_PATH)

# List for saving Coordinate and Region Name
points = [] # Ex. [{"name": "Edmonton", "x": 10, "y": 120}, ...]

# Function when clicked
def get_mouse_click_coor(x, y):

    # Window for input region name
    region_name = screen.textinput(
        "Input Region Name",
        f"Input this coordinate's name.\n(x={int(x)}, y={int(y)})"
    )

    # If User canceled or inputted empty string, ignore it
    if not region_name:
        return

    region_name = region_name.strip()

    point = {
        "name": region_name,
        "x": int(x),
        "y": int(y)
    }
    points.append(point)

    # Print for Confirmation
    print(f"{point} added")

# Function for save CSV and exit
def save_and_exit():
    # When press 's', exit program
    if not points:
        print("Nothing data for saved.")
    else:
        df = pd.DataFrame(points)
        df.to_csv(OUTPUT_CSV_FILE, index=False)
        print(f"Saved to {OUTPUT_CSV_FILE}! Total {len(points)}")

    turtle.bye()    # Close Turtle Window

# Input Coordinate when click
turtle.onscreenclick(get_mouse_click_coor)

# When press 's' key, save CSV and exit
screen.listen()
screen.onkeypress(save_and_exit, "s")

# main loop
turtle.mainloop()