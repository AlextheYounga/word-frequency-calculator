from os import listdir, scandir, path
import multiprocessing as mp
from definitions import *
from functions import scan_files


# Begin scanning imports folder
folders = scandir(IMPORTS)
for folder in folders:
    files = listdir(folder)
    if __name__ == '__main__':
        pool = mp.Pool(mp.cpu_count()) # Init multiprocessing.Pool()
        process = pool.apply_async(scan_files(files, folder, IMPORTS, action="graph")) # adding process to pool
        pool.close() #closing pool