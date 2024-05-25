import os
from PIL import Image

class ImageSorter:
    """Image sorting class"""

    def init_sorting_folder(self, sortfolder):
        self.current_directory = os.path.dirname(os.path.abspath(__file__))
        self.parent_directory = os.path.dirname(self.current_directory)
        self.sort_folder_path = os.path.join(self.parent_directory, sortfolder)
        print(f"{self.sort_folder_path}")
        if os.path.isdir(self.sort_folder_path):
            return False
        else:
            os.mkdir(self.sort_folder_path)
            return True

    def sort_images(self, sortfolder):
        self.sortcount = 0
        print(f"{self.sort_folder_path}")
        for file in os.listdir(self.sort_folder_path):
            filename = os.fsdecode(file)
            if (filename != ".DS_Store") and ("." in filename):
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
                    self.sortcount += 1
                else:
                    pass
