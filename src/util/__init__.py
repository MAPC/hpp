"""
HPP Util

A bunch of small functions that don't particularly belong
anywhere logically, even if only used in one spot of the 
whole program.
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


def parse_bool(val):
    return bool(str(val).lower() in ('true', 'yes', 't', '1'))


def strip_list(val):
    if isinstance(val, list) and len(val) > 0:
        val = val[0]

    if val:
        return [x.strip() for x in str(val).split(',')]
    else:
        return val


def convert_binary(data):
    if isinstance(data, dict):
        items = list(data.items())

        for key, value in items:
            data[key.decode()] = convert_binary(value)
            del data[key]

        return data

    elif isinstance(data, list):
        return list(map(convert_binary, data))

    else:
        return data.decode()
