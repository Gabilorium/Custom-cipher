import random
import string

## CONSTS:
ELIGIBLE_SYMBOLS = ['$', '<', '-', '>', '&']
SEED = 42
SYMBOLS_PER_LETTER = 3
CHARACTERS_TO_CONVERT = len(string.ascii_lowercase)


random.seed(SEED)
dicionary = {}
code_set = set()

##FUNCTIONS
def encode_letter ():
    while True:
        encoded_letter = ""   # reset en cada intento
        for j in range(SYMBOLS_PER_LETTER):
            encoded_letter = encoded_letter + random.choice(ELIGIBLE_SYMBOLS)
        if encoded_letter not in code_set:   # ¿qué condición te dice "este código sirve, salí del loop"?
            break
    return encoded_letter

## """MAIN"""
for i in range (CHARACTERS_TO_CONVERT):
    letter_to_encode = string.ascii_lowercase[i]
    encoded_letter = encode_letter()
    dicionary[letter_to_encode] = encoded_letter
    code_set.add(encoded_letter)
        
for code in code_set:
    print (code)

for key, value in dicionary.items():
    print(key, value)