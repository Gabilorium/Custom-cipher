import random
import string

## CONSTANTES:
ELIGIBLE_SYMBOLS = ['$', '<', '-', '>', '&']
SEED = 42
SYMBOLS_PER_LETTER = 3
CHARACTERS_TO_CONVERT = len(string.ascii_lowercase)

random.seed(SEED)
dicionary = {}


for i in range (CHARACTERS_TO_CONVERT):
    letter_to_encode = string.ascii_lowercase[i]
    encoded_letter = ""
    print("Letter = %a" %(letter_to_encode))
    for j in range(SYMBOLS_PER_LETTER):
        encoded_letter = encoded_letter + random.choice(ELIGIBLE_SYMBOLS)
        dicionary[letter_to_encode] = encoded_letter
        


for key, value in dicionary.items():
    print(key, value)