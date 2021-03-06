import matplotlib.pyplot as plt
import numpy as np
from os import path
from pathlib import Path
from export import writeCSV
import string
from collections import Counter
import statistics
import json


def syllable_average(lexicon):
    # Will calculate the average syllable count of the entire lexicon
    syllable_lst = []
    for word in lexicon:
        word = word.lower()
        count = 0
        vowels = "aeiouy"
        if word[0] in vowels:
            count += 1
        for index in range(1, len(word)):
            if word[index] in vowels and word[index - 1] not in vowels:
                count += 1
        if word.endswith("e"):
            count -= 1
        if count == 0:
            count += 1
        syllable_lst.append(count)

    mean = statistics.mean(syllable_lst)

    return mean
# I reverse engineered this particular function from the source below.
# Source: Ryan & Jeremy McGibbon https://stackoverflow.com/questions/46759492/syllable-count-in-python


def count_frequency(lexicon):
    for word in lexicon:
        word = word.translate(str.maketrans('', '', string.punctuation))  # Removing unnecessary punctuations
        counts = Counter(lexicon).most_common(10)
        counts = dict((k[0], k[1:][0]) for k in counts)  # Converting Python's most_common results into dictionary

    return counts


def word_analyzer(lexicon, folder):
    # Will analyze average syllables and write results to a csv
    frequency = count_frequency(lexicon)
    syllables = syllable_average(lexicon)
    most_common_word = list(frequency.keys())[0]

    print("\n{} Average Syllables: {}".format(folder, syllables))
    print(json.dumps(frequency, indent=1))

    writeCSV(frequency, syllables, folder)  # sending to csv function in exports.py

    return


def graph_incidence(lexicon, full_text, folder):
    # Will graph the occurrance of the most common word throughout the text
    frequency = count_frequency(lexicon)
    most_common_word = list(frequency.keys())[0]

    sentences = full_text.split('.')  # dividing txt by sentence
    data = {}
    for i, sentence in enumerate(sentences):
        count = sentence.count(most_common_word)
        data[i] = count

    # graphing the data
    x = list(data.keys())
    plt.plot(x, list(data.values()), label='\"{}\" Occurance in {}'.format(most_common_word, folder))  # Plot some data on the (implicit) axes.
    plt.xlabel('x Time')
    plt.ylabel('y Occurance')
    plt.title("Word: \"{}\" Incidence".format(most_common_word))
    plt.legend()
    # plt.show()
    plt.draw()
    plt.pause(0.001)
    input("Press [enter] to continue.")
    return


def scan_files(files, folder, imports_folder, action):
    lexicon = []
    full_text = ""

    for f in files:
        if (Path(f).suffix == '.txt'):
            with open(path.join(imports_folder, folder, f), 'r') as file:
                txt = file.read().replace('\n', '')  # converting txt file into string
                full_text += txt  # appending to full_text string
                lexicon.extend(txt.split())  # converting string into list

        else:
            print("Error: Incorrect file type provided")
            break

    if action == "analyze":
        word_analyzer(lexicon, folder)
    if action == "graph":
        graph_incidence(lexicon, full_text, folder)
    return
