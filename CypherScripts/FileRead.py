#  Simple script to read and store data from a txt file
import os


class FileRead:

    def __init__(self, file_name):
        self.file_name = file_name

    #  Loads txt file without loading whole file into memory
    def read_from_file(self):
        with open(self.file_name, "r") as readfile:
            array = []
            for lines in readfile:
                array.append(lines)
        return array
