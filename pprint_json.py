import json
import os

def load_data(filename):
	with open(filename, 'r') as json_file:
		json_file = json.loads(json_file.read())
		return json_file

def pretty_print_json(json_file):
    return json.dumps(json_file, sort_keys=True, indent=4)


if __name__ == '__main__':
	filename = input('Enter filename: ')
	if not os.path.exists(filename):
		print('No %s file in current directory' % filename)
	else:
		json_file = load_data(filename)
		print(pretty_print_json(json_file))
		