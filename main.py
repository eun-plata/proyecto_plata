import hashlib
import os
from collections import defaultdict


def hash_file(filepath):
    """This function returns the SHA-1 hash
    of the file passed into it"""
    # make a hash object
    hasher = hashlib.sha1()
    # open file for reading in binary mode
    with open(filepath, 'rb') as file:
        # loop till the end of the file
        chunk = 0
        while chunk != b'':
            # read only 1024 bytes at a time
            chunk = file.read(1024)
            hasher.update(chunk)
    # return the hex representation of digest
    return hasher.hexdigest()


def get_hash_by_file(root_dir):
    hash_by_file_dict = {}

    for dirpath, subdirs, file_list in os.walk(root_dir):
        file_list = ignore_hidden_files(file_list)
        for filename in file_list:
            filepath = os.path.join(dirpath, filename)
            file_hash = hash_file(filepath)
            hash_by_file_dict[filepath] = file_hash

    return hash_by_file_dict


def get_reverse_index(map):
    reverse_dict = defaultdict(set)

    for k, v in map.items():
        set_ = reverse_dict[v]
        set_.add(k)

    return reverse_dict


def format_file_by_hash_dict(files_by_hash):
    list_of_repeated_files = []
    for files in files_by_hash.values():
        if len(files) > 1:
            list_of_repeated_files.append(list(files))

    summary = []
    for repeated_files in list_of_repeated_files:
        reference = repeated_files[0]
        rest = repeated_files[1:]
        summary.append((reference, rest))

    return summary


def print_summary(summary):
    print('I think you have repeated files:')

    for reference, repeated in summary:
        print(f'\t{reference} is repeated in:')
        for repetition in repeated:
            print(f'\t\t{repetition}')
        print()


def ignore_hidden_files(file_list):
    result = []
    for file in file_list:
        is_hidden = file.startswith('.')
        if not is_hidden:
            result.append(file)

    return result


def command_find_repeated(root_dir):
    hash_by_file = get_hash_by_file(root_dir)
    files_by_hash = get_reverse_index(hash_by_file)
    summary = format_file_by_hash_dict(files_by_hash)
    print_summary(summary)


if __name__ == '__main__':
    root_dir = "/Users/eunyoungcho/Pictures/2019/example"
    command_find_repeated(root_dir)
