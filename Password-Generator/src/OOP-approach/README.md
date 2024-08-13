# Password Generator - OOP Approach
This Python script provides classes for generating different types of passwords: PINs, random passwords, and memorable passwords. Each password generator class implements the PasswordGenerator abstract base class, which defines a generate method that subclasses must implement.

## Features:
* **PIN Generator**: Creates random PINs (Personal Identification Numbers) of a specified length (default: 8 digits).
* **Random Password Generator**: Generates random passwords with configurable length (default: 8 characters) and optional inclusion of numbers and symbols.
* **Memorable Password Generator**: Creates passwords using random words separated by a chosen separator (default: '-'), with optional capitalization (randomly applied to each word). You can also customize the vocabulary used for word selection.


### How It Works
The password generator uses the Python `random` module to generate passwords based on user preferences. The generator is split into three classes, each representing a different type of password generation:

1. `RandomPasswordGenerator` generates a completely random password of a specified length, optional with numbers, and symbols.
2. `MemorablePasswordGenerator` creates a password made up of a set number of randomly chosen words from the NLTK English language corpus. It can optionally separate the words with a separator and use capitalized words.
3. `PinCodeGenerator` creates a numeric password of a specified length.

Each generator class inherits from a base PasswordGenerator class. They each override the base class's generate() method in order to provide their own unique password generation functionality.


### Requirements
* Python 3.7+
* NLTK (Natural Language Toolkit)

To install NLTK, use pip:
`pip install nltk`

After installing NLTK, you need to download the 'words' corpus. Run Python and type these commands:
`import nltk
nltk.download('words')`


### Running the Project
Make sure you've installed all the required dependencies. You can then set your PYTHONPATH, navigate to the 'src' directory and run the project using Python:

export PYTHONPATH="${PYTHONPATH}:/your/path/to/main/directory"
cd src
python main.py`

Be sure to replace /your/path/to/main/directory with the actual path to the directory containing your project.


### Testing
The `main.py` script also includes test cases for each password generator. The script will print out a test password for each generator and run checks to make sure the password matches the expected format.


### Additional Notes:
* The script uses the NLTK library for word generation.
* The `abc` module is used for defining abstract classes.


### Security Considerations:
* This script is for educational purposes only. In a production environment, consider using more robust password generation libraries.
* Store passwords securely (e.g., password managers).
* Avoid using predictable patterns or dictionary words in passwords.

### License
This script is provided "as-is" without any warranty. Feel free to modify and use it for your own purposes.
