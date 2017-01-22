class Magazine():
    def __init__(self):
        self.name = ''
        self.works = []


class Work():
    def __init__(self, magazine, author_name, name):
        self.author_name = author_name
        self.name = name
        self.magazine = magazine

    @property
    def output(self):
        return '[%s]%s(%s)' % (self.author_name, self.name, self.magazine.name)
