import os
import sys

dir_path = os.path.abspath(os.path.dirname(__file__))
print("Path to directory: ", dir_path)

path = os.path.join(dir_path, "data/data.csv")
print("Path to file: ", path)

import csv

with open(path) as csv_file:
    pass
