"""
HPP - abbreviate

Used for abbreviating/truncating phrases to the desired length.
"""


abbreviations = {
    'average': 'avg',
    'household': 'HH',
}

def abbreviate(phrase, length):
    words = phrase.split()

    while len(phrase) > length:
        if len(words) > 0:
            word = words.pop(0)

            if word.lower() in abbreviations:
                phrase.replace(word, abbreviations[word.lower()])
        else:
            phrase = phrase[:length]

    return phrase
