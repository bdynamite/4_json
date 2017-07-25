import json


def get_data(my_json_path):
    try:
        with open(my_json_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("file not found!")
        exit()


def pretty_print_json(json_data):
    print(json.dumps(json_data, indent=4))


if __name__ == '__main__':
    json_path = input('input data path: ')
    json_data_text = get_data(json_path)
    pretty_print_json(json_data_text)
