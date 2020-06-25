from os import listdir, scandir, path
from pathlib import Path
from multiprocessing import Pool
import json
from definitions import ROOT_DIR
from functions import *


imports_folder = "{}/imports/".format(ROOT_DIR)

folders = scandir(imports_folder)
for folder in folders:
    files = listdir(folder)
    lexicon = []

    for f in files:
        if (Path(f).suffix == '.txt'):            
            with open(path.join(imports_folder, folder, f), 'r') as file:
                txt = file.read().replace('\n', '')
                lexicon.extend(txt.split())

        else:
            print("Error: Incorrect file type provided")
            break
    frequency = count_frequency(lexicon)
    print(json.dumps(frequency, indent=1))
