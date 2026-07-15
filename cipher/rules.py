import random

ELIGIBLE_SYMBOLS = ['$', '<', '-', '>', '&']
SYMBOLS_PER_LETTER = 3


def get_separator(encoded_char):

    used_symbols = set(encoded_char)
    characters_to_add = set(ELIGIBLE_SYMBOLS) - used_symbols
    separator = ""
    character_list = list(characters_to_add)
    random.shuffle(character_list)

    while character_list:
        separator += character_list.pop()

    return separator

def get_separator_length(code):
    separator = get_separator(code)
    #print(separator)
    return len(separator)