#  Simple script to read and store data from a txt file
import os


class FileRead:

    def __init__(self, file_name):
        self.file_name = file_name

    def read_from_file(self):
        with open(self.file_name, "r") as readfile:
            data = readfile.read()
        return data
