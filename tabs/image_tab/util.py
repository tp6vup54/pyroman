import os
from tabs import vars
from tabs.image_tab.image import Image


def parse_image(path):
    pathes = [path + vars.split + f for f in os.listdir(path) \
              if os.path.isfile(path + vars.split + f) and os.path.splitext(f)[1] in vars.image_valid_extension]
    images = [Image(p) for p in pathes]
    return images