import csv
import os
from functions import *
from definitions import EXPORT_FILE


def refreshCSV():
    # If output file already exists, delete and recreate.
    if (os.path.exists(EXPORT_FILE)):
        os.remove(EXPORT_FILE)


def writeCSV(frequency, syllables, folder):
    with open(EXPORT_FILE, mode='w') as resultsfile:
        write_results = csv.writer(resultsfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        write_results.writerow([''])
        write_results.writerow(['{} Analysis', 'Average Syllables: {}'.format(folder, syllables)])
        write_results.writerow(['Word', 'Count'])

        for word, count in frequency.items():
            write_results.writerow(['{} Analysis | Average Syllables: {}'.format(folder, syllables)])
