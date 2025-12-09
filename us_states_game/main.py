import turtle
import pandas as pd
from PIL import Image

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"

# Read image size
img = Image.open(image)
img_width, img_height = img.size

# Adjust window size
screen.setup(width=img_width, height=img_height)

screen.addshape(image)
turtle.shape(image)

states_data = pd.read_csv("50_states.csv")
all_states = states_data.state.to_list()    # All US States
guessed_states = [] # Guessed States

# Text Output Turtle
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

def ask_state(first=False):
    # If 1st Question, 'Guess the State', after showing score
    if first:
        title = "Guess the State"
    else:
        title = f"{len(guessed_states)}/50 States Correct"

    answer = screen.textinput(
        title = title,
        prompt = "What's another state's name? (type 'Exit' to quit)"
    )

    return answer.title() if answer else None

def write_state_on_map(state_name):
    # Print State Name
    row = states_data[states_data.state == state_name]
    x, y = int(row.iloc[0].x), int(row.iloc[0].y)
    writer.goto(x, y)
    writer.write(state_name, align="center", font=("Arial", 8, "normal"))

# Run Game

state = ask_state(first=True) # 1st Input

if state and state in all_states and state not in guessed_states:
    guessed_states.append(state)
    write_state_on_map(state)

# Repeat Input Loop
while len(guessed_states) < 50:
    state = ask_state(first=False)

    if not state or state == "Exit":
        break

    if state in all_states and state not in guessed_states:
        guessed_states.append(state)
        write_state_on_map(state)

# Save CSV File
# guessed_df = states_data[states_data["state"].isin(guessed_states)].copy()
# missed_df = states_data[~states_data["state"].isin(guessed_states)].copy()

guessed_states_list = [state for state in all_states if state in guessed_states]
missed_states_list = [state for state in all_states if state not in guessed_states]

guessed_df = pd.DataFrame(guessed_states_list, columns=["state"])
missed_df = pd.DataFrame(missed_states_list, columns=["state"])

guessed_df["status"] = "guessed"
missed_df["status"]  = "missed"

result_df = pd.concat([guessed_df, missed_df])
result_df.to_csv("states_to_learn.csv", index=False)

screen.exitonclick()