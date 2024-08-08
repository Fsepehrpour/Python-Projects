import random
import string
from abc import ABC, abstractmethod

import nltk

nltk.download('words')


class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass


class PinGenerator(PasswordGenerator):
    def __init__(self, lenght: int = 8):
        self.lenght = lenght

    def generate(self) -> str:
        return ''.join([random.choice(string.digits) for i in range(self.lenght)])


class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, lenght: int = 8, include_numbers: bool = False, include_symbols: bool = False):
        self.lenght = lenght
        self.characters = string.ascii_letters
        if include_numbers:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation

    def generate(self):
        return ''.join([random.choice(self.characters) for i in range(self.lenght)])


class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(
            self,
            number_of_words: int = 4,
            separator: str = '-',
            capitalize: bool = False,
            vocabulary: list = None
            ):
        if vocabulary is None:
            vocabulary = nltk.corpus.words.words()

        self.vocabulary = vocabulary
        self.number_of_words = number_of_words
        self.separator = separator
        self.capitalize = capitalize

    def generate(self):
        password_words = [random.choice(self.vocabulary) for i in range(self.number_of_words)]
        if self.capitalize:
            password_words = [word.upper() if random.choice([True, False]) else word.lower() for word in password_words]
        return self.separator.join(password_words)

if __name__ == "__main__":
    pin_obj = PinGenerator()
    print(pin_obj.generate())
    memorable_pass = MemorablePasswordGenerator(4)
    print(memorable_pass.generate())
    random_pass = RandomPasswordGenerator(lenght=10, include_numbers=True, include_symbols=True)
    print(random_pass.generate())
