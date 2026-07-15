import json
import sys
from cipher.rules import get_separator

with open("alphabet.json", "r",  encoding="utf-8") as f:
    alphabet = json.load(f)

##FUNCTIONS
def get_msg(msg):
        result=""
        for i in range ((len(msg))):
            if msg[i] in alphabet:
                result += alphabet[msg[i]]
                result += get_separator(alphabet[msg[i]])
                #print(result)
            else: 
                result += msg[i]
        print(result)

## """MAIN"""
if len(sys.argv) > 1:
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        msg = f.read()
    get_msg(msg)
else: 
    while True:
        msg = input("Enter the input you want to encode (press Enter with no input to exit): ")
        if (msg == ""):
            break
        get_msg(msg)