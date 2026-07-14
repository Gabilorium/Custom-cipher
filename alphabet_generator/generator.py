import random
import string
import json

## CONSTS:
ELIGIBLE_SYMBOLS = ['$', '<', '-', '>', '&']
SEED = 42
SYMBOLS_PER_LETTER = 3
##LOWERCASE_CHARS = len(string.ascii_lowercase)
##UPPERCASE_CHARS = len(string.ascii_uppercase)
LETTERS_COUNT = len(string.ascii_letters) ##LOWERCASE_CHARS + UPPERCASE_CHARS
DIGITS_COUNT = len(string.digits)
PUNCTUATION_COUNT = len(string.punctuation)
CHARACTERS_TO_CONVERT = LETTERS_COUNT + DIGITS_COUNT + PUNCTUATION_COUNT


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
for i in range (CHARACTERS_TO_CONVERT):
    if (i <= (LETTERS_COUNT -1)):
        letter_to_encode = string.ascii_letters[i]
    elif ((i > (LETTERS_COUNT -1)) and (i <= ((LETTERS_COUNT + DIGITS_COUNT) -1))):
        letter_to_encode = string.digits[i-LETTERS_COUNT ]
    elif ((i > ((CHARACTERS_TO_CONVERT - PUNCTUATION_COUNT) -1)) and (i <= (CHARACTERS_TO_CONVERT -1))):
        letter_to_encode = string.punctuation[i-(CHARACTERS_TO_CONVERT - PUNCTUATION_COUNT)]
    encoded_letter = encode_letter()
    dictionary [letter_to_encode] = encoded_letter
    code_set.add(encoded_letter)
    
with open("alphabet.json", "w") as f:
    json.dump(dictionary, f, indent=1)#, sort_keys=True)


with open("alphabet.json", "r") as f:
    alphabet = json.load(f)

print(alphabet)
##for code in code_set:
##   print (code)
