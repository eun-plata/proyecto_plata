import os
from collections import defaultdict


root_dir = "/Users/eunyoungcho/Pictures/2019/example"


def get_file_list(root_dir):
    size_by_file_dict = {}

    for dirpath, subdirs, file_list in os.walk(root_dir):
        file_list = ignore_hidden_files(file_list)
        for file in file_list:
            file_size = os.path.getsize(root_dir + "/{}".format(file))
            size_by_file_dict[root_dir+'/'+file] = file_size

    print("lista de archivos", size_by_file_dict)

    return size_by_file_dict


def reverse_index_file_list(root_dir):
    size_by_file_dict = get_file_list(root_dir)

    file_by_size_dict = defaultdict(set)

    for file, size in size_by_file_dict.items():
        set_ = file_by_size_dict[size]
        set_.add(file)

    print('reverse_index', file_by_size_dict)

    return file_by_size_dict


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

#
# import hashlib
# def hash_file(filename):
#    """"This function returns the SHA-1 hash
#    of the file passed into it"""
#    # make a hash object
#    h = hashlib.sha1()
#    # open file for reading in binary mode
#    with open(filename,'rb') as file:
#        # loop till the end of the file
#        chunk = 0
#        while chunk != b'':
#            # read only 1024 bytes at a time
#            chunk = file.read(1024)
#            h.update(chunk)
#    # return the hex representation of digest
#    return h.hexdigest()
# message = hash_file("track1.mp3")
# print(message)
