import string

def syllable_count(word):
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
    return count
# This particular function is not my code. 
# Source: Ryan & Jeremy McGibbon https://stackoverflow.com/questions/46759492/syllable-count-in-python

def count_frequency(lexicon):
    dictionary = {}
    for word in lexicon:
        word = word.translate(str.maketrans('', '', string.punctuation))
        # count = lexicon.count(word)
        count = sum(s.count(word) for s in lexicon)
        count = 1 if count == 0
        dictionary[word] = count
        
    return dictionary

