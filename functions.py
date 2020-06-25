import string
from collections import Counter
import statistics


def syllable_average(lexicon):
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
        word = word.translate(str.maketrans('', '', string.punctuation)) # Removing unnecessary punctuations
        counts = Counter(lexicon).most_common(10)        
        counts = dict((k[0], k[1:][0]) for k in counts) # Converting Python's most_common results into dictionary

    return counts
