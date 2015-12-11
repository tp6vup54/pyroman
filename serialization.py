import json
import utilities

def dump(arr, filename):
	dump = json.dumps(arr, default = utilities.object2dict)
	with open(filename + '.json', 'w') as f:
		f.write(dump)

def load(filename):
	with open(filename + '.json', 'r') as f:
		load = json.loads(f.read(), object_hook = utilities.dict2object)
	return load