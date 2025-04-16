
from tkinter import Tk, Canvas

# Canvas & Grid Configurations
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(event):
    """Erase objects that are in contact with the eraser"""
    left_x = event.x
    top_y = event.y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE

    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)

    for obj in overlapping_objects:
        if obj != eraser:
            canvas.itemconfig(obj, fill="white")  # Set color to white

# Create Tkinter Window
root = Tk()
root.title("Eraser Tool")

# Create Canvas
canvas = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

# Draw Grid of Blue Squares
num_rows = CANVAS_HEIGHT // CELL_SIZE
num_cols = CANVAS_WIDTH // CELL_SIZE

for row in range(num_rows):
    for col in range(num_cols):
        left_x = col * CELL_SIZE
        top_y = row * CELL_SIZE
        right_x = left_x + CELL_SIZE
        bottom_y = top_y + CELL_SIZE
        canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill="blue", outline="black")

# Create Eraser
eraser = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="pink", outline="black")

# Move Eraser with Mouse
def move_eraser(event):
    """Move the eraser to follow the mouse"""
    canvas.coords(eraser, event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE)
    erase_objects(event)  # Call eraser function

canvas.bind("<Motion>", move_eraser)  # Track mouse movement

# Run the Tkinter Loop
root.mainloop()
