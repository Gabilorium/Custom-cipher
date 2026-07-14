import json

with open("alphabet.json", "r") as f:
    alphabet = json.load(f)

while True:
    result=""
    msg = input("Enter the input you want to encode (press Enter with no input to exit): ")
    
    if (msg == ""):
        break

    for i in range ((len(msg))):
        if msg[i] in alphabet:
            result += alphabet[msg[i]]
        else: 
            result += msg[i]

    print(result)