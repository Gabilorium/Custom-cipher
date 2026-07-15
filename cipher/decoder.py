import json
import sys
from pathlib import Path
from cipher.rules import get_separator_length , ELIGIBLE_SYMBOLS



with open(Path(__file__).parent.parent / "alphabet.json", "r",  encoding="utf-8") as f:
    alphabet = json.load(f)

##FUNCTIONS
def get_letter(alphabet,value):
    for key, val in alphabet.items():
        if val == value:
            return key
    return None

def get_msg(code): 
    i=0
    result= ""
    while i < len(code):
        if code[i] in ELIGIBLE_SYMBOLS:
            separator_count = get_separator_length(code[i:i+3])
            #print(separator_count)
            result += get_letter(alphabet,code[i:i+3])
            i = i + 3 + separator_count
        else:
            result += code[i]
            i += 1
    return result


## """MAIN"""
if __name__ == "__main__":
    decoded_msg=""

    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            code = f.read()
        decoded_msg = get_msg(code)
        print(decoded_msg)
    else: 
        while True:
            code = input("Enter the input you want to decode (press Enter with no input to exit): ")
            if (code == ""):
                break
            decoded_msg = get_msg(code)
            print(decoded_msg)