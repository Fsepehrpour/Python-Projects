# Password Generator - Functional Approach
This Python module provides a set of functions for generating different types of passwords and numeric pincodes. It includes utility functions for generating random passwords, memorable passphrases, and numeric PIN codes, along with corresponding unit tests for each function to ensure they behave as expected.

## Features
1. **PIN Code Generator**: Generates numeric PIN codes of a specified length.
2. **Random Password Generator**: Generates a random password with options to include numbers and symbols.
3. **Memorable Password Generator**: Generates a memorable password composed of a specified number of words, with options for capitalization and custom separators.

## Requirements
* Python 3.x
* nltk library (Natural Language Toolkit)
* unittest.mock for testing purposes

Ensure that the nltk words corpus is downloaded before using the memorable password generator:
`import nltk
nltk.download('words')`

## Installation
Clone the repository or download the script. Ensure that you have the necessary dependencies installed:
`pip install nltk`

### Usage

**PIN Code Generator**
Generates a numeric PIN code of a specified length (default is 6 digits).

```
from your_module import pin_code_generator

pin = pin_code_generator(4)
print(pin)  # Example output: '4938'
```

**Random Password Generator**
Generates a random password with the following options:
* **length**: Length of the password (default is 8 characters).
* **include_numbers**: Whether to include numbers (default is False).
* **include_symbols**: Whether to include symbols (default is False).

```
from your_module import generate_random_password

password = generate_random_password(10, include_numbers=True, include_symbols=True)
print(password)  # Example output: 'A1!b2@C3#'
```

**Memorable Password Generator**
Generates a password composed of randomly chosen words. Options include:

* **no_of_words**: Number of words in the password (default is 3).
* **separator**: Separator character between words (default is '-').
* **capitalization**: Whether to randomly capitalize some words (default is False).
* **vocabulary**: Custom vocabulary list (default is nltk.corpus.words.words()).
```
from your_module import memorable_pass_generator

memorable_password = memorable_pass_generator(4, '-', capitalization=True)
print(memorable_password)  # Example output: 'apple-Banana-cherry-Date'
```

**Testing**

The module includes built-in tests for each function, using the `unittest.mock` library to control randomness for predictable outputs.

**Run Tests**

To run the tests, execute the script directly:
`python your_script.py`

This will run tests for each generator and print the results.

### License
This project is licensed under the MIT License.

### Contact
For issues, questions, or suggestions, please open an issue or contact the author directly via the repository page.







