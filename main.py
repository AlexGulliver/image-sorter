"""Image date/month sorting script"""

import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image
from imagesorter.sorter import ImageSorter
from functools import partial

# Image sorting
def sort(sort_folder_created):
    if sort_folder_created:
        print(f"Specified sort folder does not exist. Place image files inside /{sortfolder} and re-run script.")
    else:
        print(f"{sortfolder} folder found. Sorting files...")
        image_sorter.sort_images(sortfolder)
        print(f"Sorting completed. Moved {image_sorter.sortcount} files")

# GUI
def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)

root = Tk()
folder_path = StringVar()
browse_label = Label(root, text="Select path of folder containing images")
browse_label.grid(row=0,column=1)
Label1 = Label(master=root,textvariable=folder_path)
Label1.grid(row=1, column=2)
browser_folder_button = Button(root, text="Browse", command=browse_button)
browser_folder_button.grid(row=0, column=3)

image_sorter = ImageSorter()
sortfolder = "tosort"
sort_folder_created = image_sorter.init_sorting_folder(str(folder_path))

sort_button = Button(root, text="Sort", command=partial(sort, sort_folder_created))
sort_button.grid(row=0, column=2)

# GUI Config
root.title("Image Sorter")
root.minsize(400, 100)
root.mainloop()
