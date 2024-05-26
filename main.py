import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from imagesorter.sorter import ImageSorter
from functools import partial

def sort(folder_path):
    """Calls image sort when sort button pressed."""
    print("Sorting files...")
    print(f"FOLDERPATH: {folder_path}")
    image_sorter.sort_images(folder_path)
    print(f"Sorting completed. Moved {image_sorter.sortcount} files")

def browse_button():
    """Stores user-selected sort path to folder path."""
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_path_var.set(folder_path)
        print(folder_path)
        return folder_path

def sort_with_filename():
    """File sorter command for sort button."""
    filename = folder_path_var.get()
    if filename:
        sort(filename)

# Initialise TKinter and ImageSorter
root = Tk()
image_sorter = ImageSorter()

folder_path_var = StringVar()

# Labels
browse_label = Label(root, text="Select path of folder containing images")
folder_path_label = Label(master=root, textvariable=folder_path_var)

# Buttons
browser_folder_button = Button(root, text="Browse", command=browse_button)
sort_button = Button(root, bg="green", text="Sort", command=sort_with_filename)

# Griddy
sort_button.grid(row=1, column=2)
browse_label.grid(row=0, column=1)
browser_folder_button.grid(row=0, column=2)
folder_path_label.grid(row=1, column=1)

# GUI Config
root.title("Image Sorter")
root.minsize(100, 20)
root.config()
root.mainloop()
