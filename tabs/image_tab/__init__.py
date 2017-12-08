import os

from tabs import vars
from tabs.tab import Tab
from tabs.image_tab.util import *

class ImageTab(Tab):
    def __init__(self, view):
        super().__init__(view)

    def parse(self, source_path, dest_path, force_parse_source=False, force_parse_dest=False):
        super().parse(source_path, dest_path, force_parse_source, force_parse_dest)
        images = parse_image(source_path)
        self.datasource = self.get_datasource(images, dest_path)
        self.invalidate_tableWidget()

    def invalidate_tableWidget(self):
        self.table_data = self.get_table_data(self.datasource)
        self.view.set_tableWidget_items(self.table_data)

    def get_datasource(self, images, dest_path):
        datasource = [images]
        datasource.append(self.get_datasource_dest(images, dest_path))
        return datasource

    def get_table_data(self, datasource):
        result = []
        result.append([image.file_name for image in datasource[0]])
        result.append([list(_.keys())[0] if _ else '' for _ in datasource[1]])
        result.append(self.get_duplicated_list(datasource))
        return list(map(list, zip(*result)))

    def get_duplicated_list(self, datasource):
        result = []
        found = False
        for idx, image in enumerate(datasource[0]):
            if datasource[1][idx] == '':
                result.append('')
                continue
            for root, dirs, files in os.walk(list(datasource[1][idx].values())[0]):
                if image.file_name in files:
                    result.append('Yes')
                    found = True
                    break
            if not found: result.append('')
            found = False
        return result

    def get_datasource_dest(self, images, dest_path):
        result = []
        dest_dict = {}
        for root, dirs, files in os.walk(dest_path):
            for d in dirs:
                fullpath = os.path.join(root, d)
                dest_dict.update({os.path.basename(d).lower(): fullpath})
        for i in images:
            found = False
            if not i.tags:
                result.append('')
                continue
            for t in i.tags:
                name = t['name']
                if name.lower() in dest_dict:
                    result.append({name: dest_dict[name.lower()]})
                    found = True
                    break
            if not found:
                result.append('')
        return result

    def move_image(self, idx):
        source = self.datasource[0][idx]
        dest = self.datasource[1][idx]
        os.rename(source.full_path, )

    def remove_moved_index(self, idx):
        for _ in self.datasource:
            _.remove(idx)
        self.invalidate_tableWidget()