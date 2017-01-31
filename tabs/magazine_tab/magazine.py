class Magazine():
    def __init__(self):
        self.name = ''
        self.works = []


class Work():
    def __init__(self, magazine, author_name, name, image_url):
        self.author_name = author_name
        self.name = name
        self.magazine = magazine
        self.image_url = image_url

    @property
    def output(self):
        return '[%cd s]%s(%s)' % (self.author_name, self.name, self.magazine.name)
