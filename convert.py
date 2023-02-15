import glob
import PIL
from PIL import Image

files = glob.glob("dataset/images/*")
len(files)
for file in files:
    if ".jpg" in file or ".jpeg" in file or ".webp" in file:
        image = PIL.Image.open(file)
        if image.format not in ["JPG", "JPEG"]:
            print (file,image.format)
            image.convert("RGB").save(file, "JPEG")