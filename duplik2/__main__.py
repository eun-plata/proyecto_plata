from duplik2 import *

parser = argparse.ArgumentParser(description='Find duplicated files in your folder')
parser.add_argument('path', type=str, help='Absolute path')
root_dir = "/Users/eunyoungcho/Pictures/2019/example"
command_find_repeated(root_dir)
