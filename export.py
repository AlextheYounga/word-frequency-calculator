import csv
import os
from definitions import EXPORTS


def writeCSV(frequency, syllables, folder):
    if (os.path.exists(EXPORTS + folder + ".csv")):
        os.remove(EXPORTS + folder + ".csv")

    with open(EXPORTS + folder + ".csv", mode='w') as resultsfile:
        write_results = csv.writer(resultsfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        write_results.writerow(['{} Analysis, Average Syllables: {}'.format(folder, syllables)])
        write_results.writerow(['Word', 'Count'])

        for word, count in frequency.items():
            write_results.writerow([word, count])
