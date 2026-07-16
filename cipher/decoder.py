import json
import sys
from pathlib import Path
from cipher.rules import get_separator_length , ELIGIBLE_SYMBOLS, MAX_FILE_SIZE


with open(Path(__file__).parent.parent / "alphabet.json", "r",  encoding="utf-8") as f:
    alphabet = json.load(f)

output_dir = Path(__file__).parent.parent / "decoded_texts"
output_dir.mkdir(parents=True, exist_ok=True)

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
            if i + 3 <= len(code):
                letter = get_letter(alphabet, code[i:i+3])
                if letter is None:
                    print("WARNING: Invalid or corrupted encoded message.")
                    sys.exit()
                result += letter
                separator_count = get_separator_length(code[i:i+3])
            else:
                print("WARNING: Trying to read off limits.")
                sys.exit()
            i = i + 3 + separator_count
        else:
            result += code[i]
            i += 1
    return result


## """MAIN"""
if __name__ == "__main__":
    decoded_msg=""

    if len(sys.argv) > 1:
        if Path(sys.argv[1]).stat().st_size > MAX_FILE_SIZE:
            print(f"WARNING: The file is over {MAX_FILE_SIZE//1024} KB, it won't be processed.")
            sys.exit()
        else:
            with open(sys.argv[1], "r", encoding="utf-8") as f:
                code = f.read()
            decoded_msg = get_msg(code)
            file_name= Path(sys.argv[1]).name
            with open(output_dir / f"decoded_file_{file_name}", "w", encoding="utf-8") as f:
                f.write(f"Text extracted from ===({sys.argv[1]})===:\n {decoded_msg}")
    else: 
        msg_number = 0
        file_count = 1
        while True:
            code = input("Enter the input you want to decode (press Enter with no input to exit): ")
            if (code == ""):
                break
            decoded_msg = get_msg(code)
            msg_number += 1

            current_file = output_dir / f"decoded_inputs{file_count}.txt"
            if current_file.exists() and current_file.stat().st_size >= 1024:
                file_count += 1
                current_file = output_dir / f"decoded_inputs{file_count}.txt"
                if file_count > 5:
                    file_to_remove = output_dir / f"decoded_inputs{file_count - 5}.txt"
                    if file_to_remove.exists():
                        file_to_remove.unlink()

            with open(current_file, "a", encoding="utf-8") as f:
                f.write(f"Decode code {msg_number}: {decoded_msg}\n")