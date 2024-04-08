import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    if not os.path.exists(file_path):
        print(f"File {file_name} not found.")
        return None

    with open(file_path, "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file {file_name}.")
            return None

    if field not in data:
        print(f"Field '{field}' not found in {file_name}")
        return None

    return data[field]


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")

    print("Sequential data:", sequential_data)


if __name__ == '__main__':
    main()
