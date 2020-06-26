from os import listdir, scandir, path
import multiprocessing as mp
from definitions import *
from functions import scan_files
from export import refreshCSV


# Begin scanning imports folder
folders = scandir(IMPORTS)
refreshCSV()

for folder in folders:
    files = listdir(folder)
    if __name__ == '__main__':
        pool = mp.Pool(mp.cpu_count())  # Init multiprocessing.Pool()
        process = pool.apply_async(scan_files(files, folder.name, IMPORTS, action="analyze"))  # adding process to pool
        pool.close()  # closing pool
