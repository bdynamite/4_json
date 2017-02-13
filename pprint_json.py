import json
import os
import chardet
import pprint


def load_data(my_json_path):
    if not os.path.exists(my_json_path):
        raise Exception("file not found!")
    encoding = get_encoding(my_json_path)
    with open(my_json_path, 'r', encoding=encoding) as file:
        return json.load(file)


def get_encoding(path_to_file_text):
    with open(path_to_file_text, 'rb') as source:
        lines = source.read()
        result = chardet.detect(lines)
        if result['encoding'] is None:
            raise Exception("Unknown encoding!")
        else:
            return result['encoding']


def pretty_print_json(json_data):
    pprint.pprint(json_data)


if __name__ == '__main__':
    json_path = input('input data path: ')
    json_data_text = load_data(json_path)
    pretty_print_json(json_data_text)
