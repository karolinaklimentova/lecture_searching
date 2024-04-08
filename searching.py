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


def binary_search(numbers, target):
    """
    Performs binary search on an ordered sequence to find the position of the target number.
    :param numbers: (list) ordered sequence to search
    :param target: (int) target number to search for
    :return: (int) index where the target number is found, None if not found
    """
    left, right = 0, len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None


def main():
    ordered_numbers = read_data("sequential.json", "ordered_numbers")

    print("Ordered Numbers:", ordered_numbers)

    target_number = int(input("Enter the number to search for: "))
    result = binary_search(ordered_numbers, target_number)
    if result is not None:
        print(f"The target number {target_number} is found at index {result}.")
    else:
        print(f"The target number {target_number} is not found in the sequence.")


if __name__ == '__main__':
    main()

