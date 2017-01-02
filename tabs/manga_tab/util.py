import os
import time

from tabs import vars
from tabs.manga_tab import serialization, directory


def object2dict(obj):
    d = {}
    d['__class__'] = obj.__class__.__name__
    d['__module__'] = obj.__module__
    d.update(obj.__dict__)
    return d


def dict2object(d):
    if'__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        module = __import__(module_name)
        class_ = getattr(module, class_name)
        args = dict((key.encode('ascii'), value) for key, value in d.items())
        inst = class_.DirectoryJsonAdapter()
        inst.folderpath = args[b'folderpath']
        inst.timestamp = args[b'tim' \
                              b'estamp']
    else:
        inst = d
    return inst


def parse_directory_with_json(path, force=False):
    json_path = path + vars.split + vars.json_name
    need_dump = False
    if not os.path.isfile(json_path):
        print(path + ' not found.')
        need_dump = True
    elif force:
        print('Force parse.')
        need_dump = True
    elif get_newer_file(get_latest_folder(path), json_path) != 2:
        print('A file newer than json is found.')
        need_dump = True
    if need_dump:
        print('Serialize json.')
        serialization.dump_path(path)
    else:
        print('json exist.')
    directories = serialization.load_path(path)
    return directories


def get_newer_file(file1, file2):
    time1 = time.strftime('%Y/%m/%d %H:%M:%S', time.gmtime(os.path.getmtime(file1)))
    time2 = time.strftime('%Y/%m/%d %H:%M:%S', time.gmtime(os.path.getmtime(file2)))
    return get_newer_time(get_splitted_time(time1), get_splitted_time(time2))


# 0 is same, 1 is time1, 2 is time2
def get_newer_time(time1, time2):
    result = 0
    for i in range(6):
        if time1[i] > time2[i]:
            result = 1
            break
        elif time1[i] < time2[i]:
            result = 2
            break
        else:
            result = 0
    return result


def get_splitted_time(time_string):
    temp = time_string.split(' ')
    return temp[0].split('/') + temp[1].split(':')


def get_latest_folder(path):
    all_subdirs = [path + vars.split + d for d in os.listdir(path) if os.path.isdir(path + vars.split + d)]
    return max(all_subdirs, key=os.path.getmtime)


def check_folder_is_duplicate(source, dest):
    if not dest:
        return False
    try:
        dest_dir = [f for f in os.listdir(dest.folderpath)]
    except FileNotFoundError:
        return False
    for d in dest_dir:
        if source.name == directory.get_title_name(d):
            return True
    return False