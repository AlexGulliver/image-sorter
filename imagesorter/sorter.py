import os
from PIL import Image

class ImageSorter:
    """Image sorting class"""
    def sort_images(self, sortfolder):
        self.filesortedcount = 0
        for file in os.listdir(sortfolder):
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

                    if os.path.isdir(os.path.join(sortfolder, year)):
                        pass
                    else:
                        os.mkdir(os.path.join(sortfolder, year))

                    if os.path.isdir(os.path.join(sortfolder, year, month)):
                        pass
                    else:
                        os.mkdir(os.path.join(sortfolder, year, month))

                    sorted_path = os.path.join(sortfolder, year, month) + "/" + filename

                    os.rename(filepath, sorted_path)
                    self.filesortedcount += 1
                else:
                    pass
