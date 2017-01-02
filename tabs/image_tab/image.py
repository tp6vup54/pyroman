from tabs import vars
from tabs.image_tab.module import Pixiv

class Image():
    def __init__(self, full_path):
        self.full_path = full_path
        self.file_name = full_path.split(vars.split)[-1]
        self.tags = Pixiv().get_file_tag(self.file_name)

    is_pixiv = property(lambda self: self.tags != None)