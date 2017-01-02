import os
import json
import global_vars
import utilities
from dirForSerial import DirForSerial
from directory import Directory

def dump_path(path):
    if not os.path.isdir(path):
        raise 'Argument path is not a path.'
        return
    pathes = [path + global_vars.split + f for f in os.listdir(path) if os.path.isdir(path + global_vars.split + f)]
    d = [DirForSerial(folderpath = p) for p in pathes]
    dump(d, path + global_vars.split + global_vars.json_name)

def load_path(path):
    if not os.path.isdir(path):
        raise 'Argument path is not a path.'
        return
    if not os.path.isfile(path + global_vars.split + global_vars.json_name):
        return
    d = load(path + global_vars.split + global_vars.json_name)
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
    dump = json.dumps(arr, default = utilities.object2dict)
    filename += '.json' if filename[-5:] != '.json' else ''
    with open(filename, 'w') as f:
        f.write(dump)

def load(filename):
    filename += '.json' if filename[-5:] != '.json' else ''
    with open(filename, 'r') as f:
        load = json.loads(f.read(), object_hook = utilities.dict2object)
    return load