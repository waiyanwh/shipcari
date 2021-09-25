import os
from pdf2image import convert_from_path
from PIL import Image

def convert_to_jpg(image_file_name):
    images = convert_from_path(f'{image_file_name}.pdf')
    for image in range(len(images)):
        images[image].save(f'{image_file_name}.jpg', 'JPEG')

    return f"{image_file_name}.jpg"

def crop_image(image):
    image_file_name = f"{image}.jpg"
    im = Image.open(image_file_name)

    width, height = im.size

    # Setting the points for cropped image
    left = 140
    top = 65
    right = 1560
    bottom = 1030

    # Crop photo
    im.crop((left, top, right, bottom)).rotate(90, expand=True).save(fp=image_file_name)

    return image_file_name
