import json
from pathlib import Path
from cipher.encoder import get_code
from cipher.rules import get_separator_length, ELIGIBLE_SYMBOLS


principal_path = Path(__file__).parent

with open(principal_path.parent / "alphabet.json", "r", encoding="utf-8") as f:
    alphabet = json.load(f)


def extract_codes(encoded_msg):
    expected_codes = []
    i = 0
    while i < len(encoded_msg):
        if encoded_msg[i] in ELIGIBLE_SYMBOLS:
            character_code = encoded_msg[i:i+3]
            expected_codes.append(character_code)
            i += 3 + get_separator_length(character_code)
        else:
            i += 1
    return expected_codes

def test_basic():
    with open(principal_path / "encoder_tests" / "basic.txt", "r", encoding="utf-8") as f:
        msg = f.read()
    encode_msg= get_code(msg)
    expected_codes = [alphabet[character] for character in msg if character in alphabet]

    ## SON IGUALES
    #for character in msg:
     #   if character in alphabet:
      #      expected_codes.append(alphabet[character])
    assert extract_codes(encode_msg) == expected_codes

def test_digits_and_punctuation():
    with open(principal_path / "encoder_tests" / "digits_and_punctuation.txt", "r", encoding="utf-8") as f:
        msg = f.read()
    encode_msg= get_code(msg)
    expected_codes = [alphabet[character] for character in msg if character in alphabet]
    assert extract_codes(encode_msg) == expected_codes

def test_emoji_and_other_alphabets():
    with open(principal_path / "encoder_tests" / "emoji_and_other_alphabets.txt", "r", encoding="utf-8") as f:
        msg = f.read()
    encode_msg = get_code(msg)
    expected_codes = [alphabet[character] for character in msg if character in alphabet]
    assert extract_codes(encode_msg) == expected_codes

def test_empty():
    with open(principal_path / "encoder_tests" / "empty.txt", "r", encoding="utf-8") as f:
        msg = f.read()
    encode_msg= get_code(msg)
    expected_codes = [alphabet[character] for character in msg if character in alphabet]
    assert extract_codes(encode_msg) == expected_codes

def test_mixed_all_types():
    with open(principal_path / "encoder_tests" / "mixed_all_types.txt", "r", encoding="utf-8") as f:
        msg = f.read()
    encode_msg = get_code(msg)
    expected_codes = [alphabet[character] for character in msg if character in alphabet]
    assert extract_codes(encode_msg) == expected_codes

def test_mixed_case():
    with open(principal_path / "encoder_tests" / "mixed_case.txt", "r", encoding="utf-8") as f:
        msg = f.read()
    encode_msg= get_code(msg)
    expected_codes = [alphabet[character] for character in msg if character in alphabet]
    assert extract_codes(encode_msg) == expected_codes

def test_only_whitespace():
    with open(principal_path / "encoder_tests" / "only_whitespace.txt", "r", encoding="utf-8") as f:
        msg = f.read()
    encode_msg = get_code(msg)
    expected_codes = [alphabet[character] for character in msg if character in alphabet]
    assert extract_codes(encode_msg) == expected_codes

def test_repeated_character():
    with open(principal_path / "encoder_tests" / "repeated_character.txt", "r", encoding="utf-8") as f:
        msg = f.read()
    encode_msg = get_code(msg)
    expected_codes = [alphabet[character] for character in msg if character in alphabet]
    assert extract_codes(encode_msg) == expected_codes

def test_single_character():
    with open(principal_path / "encoder_tests" / "single_character.txt", "r", encoding="utf-8") as f:
        msg = f.read()
    encode_msg = get_code(msg)
    expected_codes = [alphabet[character] for character in msg if character in alphabet]
    assert extract_codes(encode_msg) == expected_codes

def test_spanish_specific():
    with open(principal_path / "encoder_tests" / "spanish_specific.txt", "r", encoding="utf-8") as f:
        msg = f.read()
    encode_msg= get_code(msg)
    expected_codes = [alphabet[character] for character in msg if character in alphabet]
    assert extract_codes(encode_msg) == expected_codes