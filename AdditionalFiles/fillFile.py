from random import randint, seed
from time import time

seed(time())

def populateFile(fileHandle, numOfElems = 100, numOfRows = 10):

    for _ in range(numOfRows):
        for _ in range(numOfElems):
            fileHandle.write(str(randint(1,100)))
            fileHandle.write(",")
        fileHandle.write("\n")
    pass


def main():
    FILE_TO_POPULATE = "largeNumberFile.txt"

    for _ in range(10):
        with open(FILE_TO_POPULATE, "w+") as f:
            populateFile(f, 100, 50)
    pass

if __name__ == '__main__':
    main()