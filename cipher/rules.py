import random

ELIGIBLE_SYMBOLS = ['$', '<', '-', '>', '&']
SEED = 42
SYMBOLS_PER_LETTER = 3


used_symbols = set()

def add_separator(ELIGIBLE_SYMBOLS, encoded_char):

    used_symbols = set(encoded_char)
    characters_to_add = set(ELIGIBLE_SYMBOLS) - used_symbols
    separator = ""
    character_list = list(characters_to_add)
    random.shuffle(character_list)

    while character_list:
        separator += character_list.pop()

    return encoded_char + separator

char = input("encodedchar: ")
char = add_separator(ELIGIBLE_SYMBOLS, char)
print (char)