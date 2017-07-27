import json


def read_json(my_json_path):
    try:
        with open(my_json_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("file not found!")
        return None


def pretty_print_json(json_data):
    print(json.dumps(json_data, indent=4))


if __name__ == '__main__':
    json_path = input('input data path: ')
    json_text = read_json(json_path)
    if json_text:
        pretty_print_json(json_text)
