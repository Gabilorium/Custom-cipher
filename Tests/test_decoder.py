from pathlib import Path
import pytest
from cipher.decoder import get_msg

principal_path = Path(__file__).parent


def test_basic():
    with open(principal_path / "decoder_tests" / "basic.txt", "r", encoding="utf-8") as f:
        msg_coded = f.read()
    assert get_msg(msg_coded) == "helloworld"

def test_corrupted_raises_system_exit():
    with open(principal_path / "decoder_tests" / "corrupted.txt", "r", encoding="utf-8") as f:
        msg_coded = f.read()
    with pytest.raises(SystemExit):
        get_msg(msg_coded)

def test_digits_and_punctuation():
    with open(principal_path / "decoder_tests" / "digits_and_punctuation.txt", "r", encoding="utf-8") as f:
        msg_coded = f.read()
    assert get_msg(msg_coded) == "Price: $150.700,62?"

def test_emoji_and_other_alphabets():
    with open(principal_path / "decoder_tests" / "emoji_and_other_alphabets.txt", "r", encoding="utf-8") as f:
        msg_coded = f.read()
    assert get_msg(msg_coded) == "Hola 😀 mundo 日本語 test"

def test_empty():
    with open(principal_path / "decoder_tests" / "empty.txt", "r", encoding="utf-8") as f:
        msg_coded = f.read()
    assert get_msg(msg_coded) == ""

def test_mixed_all_types():
    with open(principal_path / "decoder_tests" / "mixed_all_types.txt", "r", encoding="utf-8") as f:
        msg_coded = f.read()
    assert get_msg(msg_coded) == "Test123! áé"

def test_mixed_case():
    with open(principal_path / "decoder_tests" / "mixed_case.txt", "r", encoding="utf-8") as f:
        msg_coded = f.read()
    assert get_msg(msg_coded) == "My friends are CARLOS, Mariela and PENELoPE"

def test_off_limits_raises_system_exit():
    with open(principal_path / "decoder_tests" / "off_limits.txt", "r", encoding="utf-8") as f:
        msg_coded = f.read()
    with pytest.raises(SystemExit):
        get_msg(msg_coded)

def test_only_whitespace():
    with open(principal_path / "decoder_tests" / "only_whitespace.txt", "r", encoding="utf-8") as f:
        msg_coded = f.read()
    assert get_msg(msg_coded) == "       "

def test_repeated_character():
    with open(principal_path / "decoder_tests" / "repeated_character.txt", "r", encoding="utf-8") as f:
        msg_coded = f.read()
    assert get_msg(msg_coded) == "bbbbbbbbb"

def test_single_character():
    with open(principal_path / "decoder_tests" / "single_character.txt", "r", encoding="utf-8") as f:
        msg_coded = f.read()
    assert get_msg(msg_coded) == "a"

def test_spanish_specific():
    with open(principal_path / "decoder_tests" / "spanish_specific.txt", "r", encoding="utf-8") as f:
        msg_coded = f.read()
    assert get_msg(msg_coded) == "café con leche y ñoquis"