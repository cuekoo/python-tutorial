# This script demonstrates basic usage of functions

def printMsg(name, age, height):
    print "%s is  a girl of age %d and height of %f" % (name, age, height)

def main():
    a_name = "Fiona"
    a_age = 21
    a_height = 1.65

    b_name = "Edward"
    b_age = 26
    b_height = 1.74

    printMsg( a_name, a_age, a_height)
    printMsg( b_name, b_age, b_height)

main()
