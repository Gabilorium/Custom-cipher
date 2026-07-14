import json

with open("alphabet.json", "r") as f:
    alphabet = json.load(f)

msg = input("Enter the imput you want to encode: ")

for i in range ((len(msg))):
    print(alphabet[msg[i]])