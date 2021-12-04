from PIL import Image
import pathlib
import os
import random

layers = []
directory = pathlib.Path(__file__).parent.absolute()
main_image = Image.open(f"{directory}\\img2\\1.jpg")


for root, dirs, files in os.walk(f"{directory}\\img"):  
    for filename in files:
        layers.append(Image.open(f"{directory}\\img\\{filename}"))

def generate(image):
    image.thumbnail(main_image.size)
    main_image.paste(image, (0, 0),  image)

def save(image):
    main_image.save(f"{directory}\\img3\\{os.path.basename(image.filename)}")

# layers[random.randint(0, len(layers))]