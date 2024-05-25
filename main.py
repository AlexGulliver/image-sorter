import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from imagesorter.sorter import ImageSorter
from functools import partial

# Image sorting
def sort(folder_path):
    print("Sorting files...")
    print(f"FOLDERPATH: {folder_path}")
    image_sorter.sort_images(folder_path)
    print(f"Sorting completed. Moved {image_sorter.sortcount} files")

# GUI
def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_path_var.set(folder_path)
        print(folder_path)
        return folder_path

root = Tk()
folder_path_var = StringVar()
browse_label = Label(root, text="Select path of folder containing images")
browse_label.grid(row=0, column=1)
Label1 = Label(master=root, textvariable=folder_path_var)
Label1.grid(row=1, column=2)
browser_folder_button = Button(root, text="Browse", command=browse_button)
browser_folder_button.grid(row=0, column=3)

image_sorter = ImageSorter()

def sort_with_filename():
    filename = folder_path_var.get()
    if filename:
        sort(filename)

sort_button = Button(root, text="Sort", command=sort_with_filename)
sort_button.grid(row=0, column=2)

# GUI Config
root.title("Image Sorter")
root.minsize(400, 100)
root.mainloop()
