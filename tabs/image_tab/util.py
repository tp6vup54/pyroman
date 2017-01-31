import os

from tabs import vars
from tabs.image_tab.image import Image
from tabs.image_tab.module import Pixiv

def parse_image(path):
    pathes = [path + vars.split + f for f in os.listdir(path)
              if os.path.isfile(path + vars.split + f) and
              os.path.splitext(f)[1].lower() in vars.image_valid_extension]
    images = [Image(p) for p in pathes]
    Pixiv().get_images_detail(images)
    return images