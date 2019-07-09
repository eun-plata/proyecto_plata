import hashlib
import os
from collections import defaultdict


root_dir = "/Users/eunyoungcho/Pictures/2019/example"


def hash_file(filepath):
   """"This function returns the SHA-1 hash
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

def get_file_list(root_dir):
    hash_by_file_dict = {}

    for dirpath, subdirs, file_list in os.walk(root_dir):
        file_list = ignore_hidden_files(file_list)
        for filename in file_list:
            filepath = os.path.join(dirpath, filename)
            file_hash = hash_file(filepath)
            hash_by_file_dict[filepath] = file_hash

    print("lista de archivos", hash_by_file_dict)

    return hash_by_file_dict


def reverse_index_file_list(root_dir):
    hash_by_file_dict = get_file_list(root_dir)

    file_by_hash_dict = defaultdict(set)

    for file, size in hash_by_file_dict.items():
        set_ = file_by_hash_dict[size]
        set_.add(file)

    print('reverse_index', file_by_hash_dict)

    return file_by_hash_dict


def ignore_hidden_files(file_list):
    result = []
    for file in file_list:
        is_hidden = file.startswith('.')
        if not is_hidden:
            result.append(file)

    return result



if __name__ == '__main__':
    get_file_list(root_dir)
    reverse_index_file_list(root_dir)

