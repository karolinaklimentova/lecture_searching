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


def linear_search(sequence, target):
    """
    Performs linear search on an unordered sequence to find positions and count of a target number.
    :param sequence: (list) unordered sequence to search
    :param target: (int) target number to search for
    :return: (dict) dictionary containing positions and count of the target number
    """
    positions = []
    count = 0
    for index, number in enumerate(sequence):
        if number == target:
            positions.append(index)
            count += 1
    return {"positions": positions, "count": count}


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")

    print("Sequential data:", sequential_data)

    target_number = int(input("Enter the number to search for: "))

    result = linear_search(sequential_data, target_number)
    print("Result:", result)


if __name__ == '__main__':
    main()
