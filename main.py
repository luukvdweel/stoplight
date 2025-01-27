import tkinter as tk
from tkinter import Canvas
import time
import random

def switch_light():
    """Switch the stoplight between red and green."""
    global is_red

    if is_red:
        canvas.itemconfig(red_light, fill="gray")
        canvas.itemconfig(green_light, fill="green")
        delay = random.randint(2, 10) * 1000  # Random delay for green light (2-10 seconds)
    else:
        canvas.itemconfig(green_light, fill="gray")
        canvas.itemconfig(red_light, fill="red")
        delay = random.randint(2, 60) * 1000  # Random delay for red light (2-60 seconds)

    is_red = not is_red
    root.after(delay, switch_light)

# Initialize the main application window
root = tk.Tk()
root.overrideredirect(1)  # Remove the window decorations (title bar, borders, etc.)
root.attributes("-topmost", True)  # Keep the window on top
root.attributes("-transparentcolor", "black")  # Make black color transparent
root.geometry("200x400+100+100")  # Set the window size and position
root.config(bg="black")  # Set background color to transparent color

# Create a canvas for drawing the stoplight
canvas = Canvas(root, width=200, height=400, bg="black", highlightthickness=0)
canvas.pack(expand=True)

# Draw the stoplight housing
canvas.create_rectangle(50, 50, 150, 350, fill="black", outline="black")

# Draw the red light
red_light = canvas.create_oval(75, 75, 125, 125, fill="red")

# Draw the green light
green_light = canvas.create_oval(75, 275, 125, 325, fill="gray")

# Allow dragging the window
def start_move(event):
    root.x = event.x
    root.y = event.y

def move_window(event):
    x = root.winfo_pointerx() - root.x
    y = root.winfo_pointery() - root.y
    root.geometry(f"200x400+{x}+{y}")

canvas.bind("<Button-1>", start_move)
canvas.bind("<B1-Motion>", move_window)

# Initial light state
is_red = True

# Start the light-switching loop
root.after(0, switch_light)

# Run the application
root.mainloop()
