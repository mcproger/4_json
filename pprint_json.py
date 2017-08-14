import json
import os
import argparse


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


def get_arguments_from_console():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', type=str, help='file containing json for pretty print')
    args = parser.parse_args()
    return args


def pretty_print_json(json_file):
    return json.dumps(json_file, sort_keys=True, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    args = get_arguments_from_console()
    json_file = load_data(args.filepath)
    print(pretty_print_json(json_file))
