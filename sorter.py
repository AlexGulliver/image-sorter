"""Image date/month sorting script"""

import os
from PIL import Image

sortfolder = "tosort"


class ImageSorter:
    """Image sorting class"""

    def init_sorting_folder(self, sortfolder):
        sort_folder_path = os.path.join(os.path.dirname(__file__), sortfolder)
        if os.path.isdir(sort_folder_path):
            return False
        else:
            os.mkdir(sort_folder_path)
            return True

    def sort_images(self, sortfolder):
        sort_folder_path = os.path.join(os.path.dirname(__file__), sortfolder)
        for file in os.listdir(sort_folder_path):
            filename = os.fsdecode(file)
            filepath = sortfolder + "/" + filename
            image = Image.open(filepath)
            exifdata = image.getexif()
            if exifdata and 306 in exifdata:
                year = exifdata[306][0:4]
                month = exifdata[306][5:7]
                print(f"File: {filename}")
                print(f"Year: {year}")
                print(f"Month: {month}")
                print(f"Datetime: {exifdata[306]}\n")

                if os.path.isdir(year):
                    pass
                else:
                    os.mkdir(year)

                if os.path.isdir(os.path.join(year, month)):
                    pass
                else:
                    os.mkdir(os.path.join(year, month))

                sorted_path = os.path.join(year, month) + "/" + filename

                os.rename(filepath, sorted_path)

                # Create folder with that year/month structure


image_sorter = ImageSorter()

sort_folder_created = image_sorter.init_sorting_folder(sortfolder)

if sort_folder_created:
    print(f"{sortfolder} folder created.")
else:
    print(f"{sortfolder} folder already exists.")
    image_sorter.sort_images(sortfolder)
