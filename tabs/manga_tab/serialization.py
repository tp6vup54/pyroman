import json
import os

from tabs import vars
from tabs.DirectoryJsonAdapter import DirectoryJsonAdapter
from tabs.manga_tab import util
from tabs.manga_tab.directory import Directory


def dump_path(path):
    if not os.path.isdir(path):
        raise 'Argument path is not a path.'
    pathes = [path + vars.split + f for f in os.listdir(path) if os.path.isdir(path + vars.split + f)]
    d = [DirectoryJsonAdapter(folderpath = p) for p in pathes]
    dump(d, path + vars.split + vars.json_name)

def load_path(path):
    if not os.path.isdir(path):
        raise 'Argument path is not a path.'
    if not os.path.isfile(path + vars.split + vars.json_name):
        return
    d = load(path + vars.split + vars.json_name)
    return [Directory(serial = dd) for dd in d]

# tags = { root key: keywords, ...}
def dump_tags(tags, filename):
    if not tags: return
    dump(tags, filename)

def load_tags(filename):
    if not os.path.isfile(filename):
        return
    d = load(filename)
    return d

def dump(arr, filename):
    dump = json.dumps(arr, default =util.object2dict)
    filename += '.json' if filename[-5:] != '.json' else ''
    with open(filename, 'w') as f:
        f.write(dump)

def load(filename):
    filename += '.json' if filename[-5:] != '.json' else ''
    with open(filename, 'r') as f:
        load = json.loads(f.read(), object_hook =util.dict2object)
    return load