import csv
import os
from .functions import *
from definitions import ROOT_DIR


def writeCSV(words, syllables):
    output_file = "{}/exports/wordfrequency.csv".format(ROOT_DIR)

    # If output file already exists, delete and recreate.
    if (os.path.exists(output_file)):
        os.remove(output_file)

    with open(output_file, mode='w') as resultsfile:
        write_results = csv.writer(resultsfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        write_results.writerow(['Word Frequency Analysis'])
