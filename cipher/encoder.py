import json
import sys
from pathlib import Path
from cipher.rules import get_separator

with open(Path(__file__).parent.parent / "alphabet.json", "r",  encoding="utf-8") as f:
    alphabet = json.load(f)

##FUNCTIONS
def get_code(msg):
        result=""
        for i in range ((len(msg))):
            if msg[i] in alphabet:
                result += alphabet[msg[i]]
                result += get_separator(alphabet[msg[i]])
                #print(result)
            else: 
                result += msg[i]
        return result

## """MAIN"""
if __name__ == "__main__":
    encoded_msg= ""

    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            msg = f.read()
        encoded_msg = get_code(msg)
        print(encoded_msg)
    else: 
        while True:
            msg = input("Enter the input you want to encode (press Enter with no input to exit): ")
            if (msg == ""):
                break
            encoded_msg = get_code(msg)
            print(encoded_msg)