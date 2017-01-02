from pixivpy3 import *

from tabs import vars


class Pixiv():
    __single = None
    def __init__(self):
        self.api = PixivAPI()
        self.api.login(vars.pixiv_username, vars.pixiv_password)

    def __new__(clz):
        if not Pixiv.__single:
            Pixiv.__single = object.__new__(clz)
        return Pixiv.__single

    def __get_id(self, filename):
        id = filename.split('.')[0].split('_')[0]
        if len(id) > 8: return None
        try: id = int(id)
        except: return None
        return id

    def get_file_tag(self, filename):
        id = self.__get_id(filename)
        tags = None
        if not id: return None
        json = self.api.works(id)
        if not hasattr(json, 'has_error'):
            tags = json.response[0].tags
        return tags
