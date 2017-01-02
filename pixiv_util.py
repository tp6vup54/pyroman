from pixivpy3 import *
import global_vars

class pixiv_util():
    __single = None
    def __init__(self):
        self.api = PixivAPI()
        self.api.login(global_vars.pixiv_username, global_vars.pixiv_password)

    def __new__(clz):
        if not pixiv_util.__single:
            pixiv_util.__single = object.__new__(clz)
        return pixiv_util.__single

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
