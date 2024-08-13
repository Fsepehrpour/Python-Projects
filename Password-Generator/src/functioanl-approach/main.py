import random
import string
from typing import List, Optional
from unittest.mock import patch


import nltk

nltk.download('words')


def pin_code_generator(number_of_digits: int = 6) -> str:
  """
  Generate a numeric pincode.
  """
    digits = string.digits
    pincode = ''.join([random.choice(digits) for i in range(number_of_digits)])
    return pincode

def test_pin_generator():
    pin = pin_code_generator(4)
    print(pin)
    assert len(pin) == 4
    assert all(char in string.digits for char in pin)


def generate_random_password(length: int = 8,
                             include_numbers: bool = False,
                             include_symbols: bool = False
                             ) -> str:
    """
    Generate a random password.
    """
    if include_numbers and include_symbols:
        characters = string.ascii_letters + string.digits + string.punctuation
    elif include_numbers:
        characters = string.ascii_letters + string.digits
    elif include_symbols:
        characters = string.ascii_letters + string.punctuation
    else:
        characters = string.ascii_letters

    return ''.join(random.choice(characters) for _ in range(length))


def test_random_password_generator():
    with patch('random.choice') as mock_choice:  # Use a string path for patching
        # Setting up mock returns
        mock_choice.side_effect = ['A', 'a', '1', '!', 'B', 'b', '2', '@', 'C', 'c']

        # Generate a password
        password = generate_random_password(10, True, True)

        # Assert length
        assert len(password) == 10

        # Assert contains upper case
        assert any(char in string.ascii_uppercase for char in password)

        # Assert contains digits
        assert any(char in string.digits for char in password)

        # Assert contains symbols
        assert any(char in string.punctuation for char in password)

        print("Password:", password)
        print("Test passed!")



