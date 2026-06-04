from jacks import *
from sys import argv

if __name__ == '__main__':
    if len(argv) > 1:
        get_version_synced(argv[1])
    else:
        get_version_synced()