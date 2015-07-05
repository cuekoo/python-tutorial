# This script demonstrates how to create directories

import os

#  This function creates [number] directories under root
def mkdir( root, number ):

    for i in range(0, number):
        dirname = root + "/" + str(i)
        os.mkdir( dirname )


def main():
    root = "/Users/liuyuan/temp/foo/"
    os.mkdir( root )
    mkdir( root, 5 )

main()
