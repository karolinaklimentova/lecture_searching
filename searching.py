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


def pattern_search(sequence, pattern):
    """
    Performs pattern search on a DNA sequence to find positions of the target pattern.
    :param sequence: (str) DNA sequence to search
    :param pattern: (str) target pattern to search for
    :return: (set) set containing positions of the target pattern
    """
    positions = set()
    pattern_length = len(pattern)
    sequence_length = len(sequence)

    for i in range(sequence_length - pattern_length + 1):
        if sequence[i:i + pattern_length] == pattern:
            positions.add(i)

    return positions


def main():
    dna_sequence = read_data("sequential.json", "dna_sequence")

    print("DNA Sequence:", dna_sequence)

    target_pattern = input("Enter the pattern to search for: ")
    result = pattern_search(dna_sequence, target_pattern)
    print("Result:", result)


if __name__ == '__main__':
    main()
