import sys, json, os


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filename, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


def pretty_print_json(json_file):
    return json.dumps(json_file, sort_keys=True, indent=4, ensure_ascii=False)


if __name__ == '__main__':
	try:
		filename = sys.argv[1]
	except IndexError:
		filename = None
	if filename is None:
		print('Please, enter filepath')
	else:	
		json_file = load_data(filename)
		print(pretty_print_json(json_file))
