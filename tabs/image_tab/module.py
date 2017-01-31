from pixivpy3 import *
import grequests

from tabs import vars

class Pixiv():
    def __init__(self):
        self.api = AppPixivAPI()
        self.api.requests_call = self.get_requests_call

    def get_requests_call(self, method, url, headers={}, params=None, data=None, stream=False):
        if (method == 'GET'):
            return grequests.get(url, params=params, headers=headers, stream=stream)
        elif (method == 'POST'):
            return grequests.post(url, params=params, data=data, headers=headers, stream=stream)
        elif (method == 'DELETE'):
            return grequests.delete(url, params=params, data=data, headers=headers, stream=stream)

    def illust_detail(self, illust_id, req_auth=False):
        url = 'https://app-api.pixiv.net/v1/illust/detail'
        params = {'illust_id': illust_id}
        return self.api.no_auth_requests_call('GET', url, params=params, req_auth=req_auth)

    def get_images_detail(self, image_list):
        rs = []
        for image in image_list:
            if image.is_pixiv:
                rs.append(self.illust_detail(image.illust_id))
        grequests.map(rs)
        i = 0
        for image in image_list:
            if image.is_pixiv:
                image.parse_tags(rs[i].response)
                i = i + 1
        return image_list