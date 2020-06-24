from os import walk
from multiprocessing import Pool
import json
from definitions import ROOT_DIR


imports_folder = "{}/imports/".format(ROOT_DIR)

for (directory, folders, filenames) in walk(imports_folder):
    print(json.dumps(folders, indent=1))
    for folder in folders:
        filename = walk(folder)
        print(filename)
        

    break


