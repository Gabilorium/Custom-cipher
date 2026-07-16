import json
import sys
from pathlib import Path
import warnings
from cipher.rules import get_separator, MAX_FILE_SIZE



with open(Path(__file__).parent.parent / "alphabet.json", "r",  encoding="utf-8") as f:
    alphabet = json.load(f)

output_dir = Path(__file__).parent.parent / "encoded_texts"
output_dir.mkdir(parents=True, exist_ok=True)

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
        if Path(sys.argv[1]).stat().st_size > MAX_FILE_SIZE:
            print(f"WARNING: The file is over {MAX_FILE_SIZE//1024} KB, it won't be processed.")
            sys.exit()
        else:
            with open(sys.argv[1], "r", encoding="utf-8") as f:
                msg = f.read()
            encoded_msg = get_code(msg)
            file_name= Path(sys.argv[1]).name
            with open(output_dir / f"encoded_file_{file_name}", "w", encoding="utf-8") as f:
                f.write(f"Text extracted from ===({sys.argv[1]})===:\n {encoded_msg}")
    else:
        msg_number = 0
        file_count = 1
        while True:
            msg = input("Enter the input you want to encode (press Enter with no input to exit): ")
            if msg == "":
                break
            encoded_msg = get_code(msg)
            msg_number += 1

            current_file = output_dir / f"encoded_inputs{file_count}.txt"
            if current_file.exists() and current_file.stat().st_size >= 1024:
                file_count += 1
                current_file = output_dir / f"encoded_inputs{file_count}.txt"
                if file_count > 5:
                    file_to_remove = output_dir / f"encoded_inputs{file_count - 5}.txt"
                    if file_to_remove.exists():
                        file_to_remove.unlink()

            with open(current_file, "a", encoding="utf-8") as f:
                f.write(f"Encoded msg {msg_number}: {encoded_msg}\n")