from cipher_hc3245 import __version__
from cipher_hc3245 import cipher_hc3245

def test_version():
    assert __version__ == '0.1.1'
    
def cipher(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ'
    new_text = ''
    if isinstance(shift, str):
        raise Exception("shift parameter is a string")
    else:
        for c in text:
            index = alphabet.find(c)
            if index == -1:
                new_text += c
            else:
                new_index = index + shift if encrypt == True else index - shift
                new_index %= len(alphabet)
                new_text += alphabet[new_index:new_index+1]
        return new_text

def test_cipher():
    text_example = 'L'
    shift_example = 1
    expected = 'M'
    actual = cipher(text_example, shift_example, encrypt=True)
    assert actual == expected

def test_cipher_negshift():
    text_example = 'L'
    shift_example = -1
    expected = 'K'
    actual = cipher(text_example, shift_example, encrypt=True)
    assert actual == expected

def test_cipher_symbol():
    text_example = 'L*'
    shift_example = 1
    expected = 'M*'
    actual = cipher(text_example, shift_example, encrypt=True)
    assert actual == expected

import pytest
def test_cipher_strshift():
	with pytest.raises(Exception):
    		cipher('L', 'two', encrypt=True)
