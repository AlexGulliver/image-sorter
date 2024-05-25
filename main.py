"""Image date/month sorting script"""

import os
from PIL import Image
from imagesorter.sorter import ImageSorter

sortfolder = "tosort"
            
image_sorter = ImageSorter()

sort_folder_created = image_sorter.init_sorting_folder(sortfolder)

if sort_folder_created:
    print(f"Specified sort folder does not exist. Place image files inside /{sortfolder} and re-run script.")
else:
    print(f"{sortfolder} folder found. Sorting files...")
    image_sorter.sort_images(sortfolder)
    print(f"Sorting completed. Moved {image_sorter.sortcount} files")
