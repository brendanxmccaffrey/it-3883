# Program Name:         Assignment3.py
# Course:               IT3883/Section W01
# Student Name:         Brendan McCaffrey
# Assignment Number:    Lab3
# Due Date:             10/10/2026
# Purpose:              This program creates a graphical user interface that converts
#                       Miles per Gallon (MPG) to Kilometers per Liter (km/L).
# Resources:            Module 3-1 GUI Design, Module 3-2 GUI,
#                       Calculator 1.py, Calculator 2_hole.py,
#                       calendar_gui.py, todo_app.py

from tkinter import *

# Conversion factor provided in the assignment
CONVERSION_FACTOR = 0.425143707

# Convert miles per gallon to kilometers per liter as the user types
def convert_mpg(event=None):
    user_input = mpg_entry.get().strip()

    # Clear the result if the input box is empty
    if user_input == "":
        result_label.config(text="")
        return

    # Attempt the conversion and prevent invalid input from crashing the program
    try:
        mpg = float(user_input)
        km_per_liter = mpg * CONVERSION_FACTOR
        result_label.config(text=f"{km_per_liter:.3f}")

    except ValueError:
        result_label.config(text="Invalid input")


# Create  GUI window
root = Tk()
root.title("MPG to km/L Converter")
root.geometry("320x120")

# Create labels and entry box
mpg_label = Label(root, text="Miles per Gallon:")
mpg_label.grid(row=0, column=0)

mpg_entry = Entry(root)
mpg_entry.grid(row=0, column=1)

km_label = Label(root, text="Kilometers per Liter:")
km_label.grid(row=1, column=0)

result_label = Label(root, text="")
result_label.grid(row=1, column=1)

# Run the conversion after every key stroke
mpg_entry.bind("<KeyRelease>", convert_mpg)

# Start the GUI event loop
root.mainloop()