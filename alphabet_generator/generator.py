import random
import string
import json
from cipher.rules import ELIGIBLE_SYMBOLS, SEED, SYMBOLS_PER_LETTER

## CONSTS:
SEED = 42
SPANISH_CHARS = "áéíóúñüÁÉÍÓÚÑÜ"
LETTERS_COUNT = len(string.ascii_letters)
DIGITS_COUNT = len(string.digits)
PUNCTUATION_COUNT = len(string.punctuation)
SPANISH_CHARS_COUNT = len(SPANISH_CHARS)
CHARACTERS_TO_CONVERT_COUNT = LETTERS_COUNT + DIGITS_COUNT + PUNCTUATION_COUNT + SPANISH_CHARS_COUNT
CHARACTERS_TO_CONVERT = string.ascii_letters + string.digits + string.punctuation + SPANISH_CHARS


random.seed(SEED)
dictionary = {}
code_set = set()

##FUNCTIONS
def encode_letter ():
    while True:
        encoded_letter = ""  # reset en cada intento
        for j in range(SYMBOLS_PER_LETTER):
            encoded_letter = encoded_letter + random.choice(ELIGIBLE_SYMBOLS)
        if encoded_letter not in code_set:
            break
    return encoded_letter

## """MAIN"""
for i in range (CHARACTERS_TO_CONVERT_COUNT):
    letter_to_encode = CHARACTERS_TO_CONVERT[i]
    encoded_letter = encode_letter()
    dictionary [letter_to_encode] = encoded_letter
    code_set.add(encoded_letter)
    
with open("alphabet.json", "w", encoding="utf-8") as f:
    json.dump(dictionary, f, indent=1, ensure_ascii=False)
