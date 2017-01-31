import requests
from bs4 import BeautifulSoup
from tabs.magazine_tab.magazine import *

class Parser():
    def __init__(self):
        self.url = ''
        self.domain = ''
        self.soup = None

    def parse(self, url):
        self.url = url
        response = requests.get(self.url)
        if response.status_code != 200:
            raise WebsiteUnreachableException(response.status_code, self.url)
        self.soup = BeautifulSoup(response.content, 'html5lib')

    def _get_new_magazine(self):
        new_magazine = Magazine()
        if self.soup != None:
            new_magazine.name = self._get_magazine_name()
        return new_magazine

    def _get_magazine_name(self):
        pass


class LivedoorParser(Parser):
    def __init__(self):
        super().__init__()
        self.domain = 'livedoor'
        self.work_selectors = [{
            'caption': {'selector': 'div.deka-caption', 'func': self._standardize_big_caption},
            'image': {'selector': 'img.deka-gazou'}
        }, {
            'caption': {'selector': 'div.sanretu-caption-2gyou', 'func': self._standardize_small_caption},
            'image':{'selector': '.img-body img.sanretu-gazou'}
        }]

    def parse(self, url):
        super().parse(url)
        new_magazine = self._get_new_magazine()
        first = True
        for selector in self.work_selectors:
            captions = self.soup.select(selector['caption']['selector'])
            images = self.soup.select(selector['image']['selector'])
            for idx, caption in enumerate(captions):
                if not first:
                    new_magazine.works.append(Work(
                        new_magazine,
                        *selector['caption']['func'](caption),
                        images[len(images) - len(captions) + idx]['src']
                    ))
                else:
                    first = False
        return new_magazine

    def _standardize_big_caption(self, caption):
        return (str(caption.contents[0])[:-1], caption.contents[1].text)

    def _standardize_small_caption(self, caption):
        def remove_useless_char(s):
            s = s.replace('「', '')
            s = s.replace('」', '')
            s = s.replace('\n', '')
            s = s.strip()
            return s

        text = caption.text
        ret = text.rsplit('「', 1)
        ret[0] = remove_useless_char(ret[0])
        ret[1] = remove_useless_char(ret[1])
        return ret

    def _get_magazine_name(self):
        main = self.soup.find('div', {'class': 'main'})
        img = main.find('img')
        ret = img['alt'].replace('「', '')
        ret = ret.replace('」', '')
        return ret

class AcgnichieParser(Parser):
    def __init__(self):
        super().__init__()
        self.domain = 'acgnichie'
        self.work_selectors = [{
            'caption': {'selector': 'td.tr-caption', 'func': self._standardize_caption},
            'image': {'selector': '.tr-caption-container img'}}]

    def parse(self, url):
        super().parse(url)
        new_magazine = self._get_new_magazine()
        for selector in self.work_selectors:
            captions = self.soup.select(selector['caption']['selector'])
            images = self.soup.select(selector['image']['selector'])
            for idx, caption in enumerate(captions):
                if self._check_if_caption_valid(caption.text):
                    new_magazine.works.append(Work(
                        new_magazine,
                        *selector['caption']['func'](caption.text),
                        images[idx]['src']
                    ))
        return new_magazine

    def _check_if_caption_valid(self, text):
        return text != '' and text[-1][0] == '」'

    def _standardize_caption(self, text):
        text = text[:-1]
        return text.split('「')

    def _get_magazine_name(self):
        title = self.soup.find('title').text
        ret = title[title.index('「') + 1:title.index('」')]
        ret = ret.upper()
        return ret

class WebsiteUnreachableException(Exception):
    def __init__(self, status_code, url):
        self.cause = 'WebsiteUnreachableException'
        self.message = 'requests get %d, the following website cannot be queried: %s' % (status_code, url)
        super().__init__(self.cause, self.message)