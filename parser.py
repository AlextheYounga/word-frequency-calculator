from os import listdir, scandir, path
from pathlib import Path
import multiprocessing as mp
import json
from definitions import ROOT_DIR
from functions import *


imports_folder = "{}/imports/".format(ROOT_DIR)

def scan_files(files):
    lexicon = []
    results = {}
    for f in files:
        if (Path(f).suffix == '.txt'):
            with open(path.join(imports_folder, folder, f), 'r') as file:
                txt = file.read().replace('\n', '')  # converting txt file into string
                lexicon.extend(txt.split())  # converting string into list

        else:
            print("Error: Incorrect file type provided")
            break
    
    frequency = count_frequency(lexicon)
    syllables = syllable_average(lexicon)

    print(json.dumps(frequency, indent=1))
    print("\nAverage Syllables: {}".format(syllables))

    return

# Begin scanning imports folder
folders = scandir(imports_folder)
for folder in folders:
    files = listdir(folder)
    if __name__ == '__main__':
        pool = mp.Pool(mp.cpu_count()) # Init multiprocessing.Pool()
        process = pool.apply_async(scan_files(files)) # adding process to pool
        pool.close() #closing pool
