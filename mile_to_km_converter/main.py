from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=200, height=100)
window.config(padx=15, pady=15)

FONT = ("Departure Mono", 10, "normal")

# Input Miles
input_miles = Entry(width=10, font=FONT)
input_miles.grid(column=1, row=0)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

# Conversion to KM
equal_to_label = Label(text="is equal to", font=FONT)
equal_to_label.grid(column=0, row=1)

converted_to_km = Label(text=0, font=FONT)
converted_to_km.grid(column=1, row=1)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

# Calculate Button
def button_clicked():
    miles = float(input_miles.get())
    miles_to_km = round(miles * 1.609)
    converted_to_km.config(text=f"{miles_to_km}")

calculate_button = Button(text="Calculate", command=button_clicked, font=FONT)
calculate_button.grid(column=1, row=2)

window.mainloop()