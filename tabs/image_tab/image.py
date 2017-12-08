import re
import json
import os

class Image():
    def __init__(self, full_path):
        self.full_path = full_path
        self.file_name =os.path.basename(full_path)
        self.illust_id = self.get_valid_id(self.file_name)
        self.title = ''
        self.author = ''
        self.tags = []

    @property
    def is_pixiv(self):
        return self.illust_id != None

    def get_valid_id(self, file_name):
        result = re.search(r'^\d{8,9}[._]', file_name)
        ret = None
        if result:
            ret = result.group(0)[:-1]
        return ret

    def parse_tags(self, response):
        if response.status_code == 200:
            # raise ImageException(response.status_code, self.illust_id)
            j = json.loads(response.text)
            self.title = j['illust']['title']
            self.author = j['illust']['user']['name']
            self.tags = j['illust']['tags']


class ImageException(Exception):
    def __init__(self, status_code, id):
        self.cause = 'ImageException'
        self.message = 'requests get %d, tags of the following id cannot be parsed: %s' % (status_code, id)
        super().__init__(self.cause, self.message)