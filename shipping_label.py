import urllib
import tempfile
from pdf2image import convert_from_path
from PIL import ImageOps

def crop_pdf(url):
    response = urllib.request.urlopen(url)
    filename = "temp.pdf"
    file = open(filename, 'wb')
    file.write(response.read())
    border = (170,120,170,1215)
    images = convert_from_path(filename)
    cropped_img = ImageOps.crop(images[0], border).rotate(270, expand=True)
    file.close()
    return cropped_img