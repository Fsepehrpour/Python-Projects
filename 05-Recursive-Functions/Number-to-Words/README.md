# Number to Words Converter
This project aims to create a Python function that converts a given integer into its numeral version. For example, the number `100` should be converted to "one hundred".

The solution involves breaking down the problem into manageable parts and using a recursive approach to construct the numeral version of numbers.

## Problem Breakdown
Due to the irregularities in the English language, the conversion of numbers is not straight forward. The problem can be decomposed into several base cases, regarding the size of the number:
1. **Numbers less than 20**: Unique names that don’t follow a regular pattern (e.g., "eleven", "seventeen"). We handle these by direct mapping using a predefined dictionary named UNDER_20.
2. **Numbers from 20 to 99**: Composed of a ten's name and sometimes an additional unit's name (e.g., "twenty-one", "eighty-five"). We handle these by defining a dictionary named TENS for the multiples of ten and combining them with the necessary unit's name if needed.
3. **Numbers 100 and above**: These require a recursive approach because they are composed of smaller parts that repeat the same pattern (e.g., "two hundred", "one thousand"). We handle these by defining a dictionary named ABOVE_100 to map significant number pivots like 100, 1000, and so on to their respective names ("hundred", "thousand", etc.). We then use recursion to break down and convert each part of the number.

## `num_to_word` Function
this function is the core of this project which takes an integer and returns its numeral version as a string. The function is implemented as follows:
```python
def num_to_word(num: int) -> str:
    if num < 20:
        # Direct mapping for numbers less than 20
        return UNDER_20[num]
    if num < 100:
        # Concatenation of tens and possibly a unit less than 10
        return TENS[num // 10 - 2] + ("" if num % 10 == 0 else " " + UNDER_20[num % 10])
    # Recursive case for numbers 100 and above
    pivot = max([key for key in ABOVE_100.keys() if key <= num])
    p1 = num_to_word(num // pivot)
    p2 = ABOVE_100[pivot]
    p3 = "" if num % pivot == 0 else " " + num_to_word(num % pivot)
    return p1 + " " + p2 + p3
```

## Detailed Breakdown
**1. Handling Numbers Less Than 20**:
  * Check if the number is less than 20.
  * Return the corresponding name from the `UNDER_20` dictionary.

**2. Handling Numbers from 20 to 99**:
  * Check if the number is less than 100.
  * Find the word for the tens place from the `TENS` dictionary.
  * Find the word for the units place from the `UNDER_20` dictionary if the remainder is non-zero.
  * Concatenate the tens and unit names appropriately.

**3. Handling Numbers 100 and Above**:

  * Identify the largest pivot value from the `ABOVE_100` dictionary that is less than or equal to the number.
  * Divide the number by this pivot to find the multiplier for the significant number (e.g., "two" in "two hundred").
  * Recursively call `num_to_word` for the multiplier and the remainder of the division.
  * Concatenate the results to form the full word representation.
    
This function is designed to handle numbers of any size, as long as they are within the range of standard English numerals (up to the largest key in `ABOVE_100`). It uses recursion elegantly to handle the complexity of the English number system in a concise and readable manner.

## Getting Started:
This project includes the following main Python file:

* `main.py`: The main script handles user input and calls the `num_to_word function in the same script.
Other required modules and necessary constants are in a separate Python file:

* `constants.py`: This file contains all the constant lists and dictionaries that are necessary for the `number-to-word` conversion. These constants include `UNDER_20`, `TENS` and `ABOVE_100`.

To run the program, follow these steps:

1. Navigate to the project folder in your terminal.
2. Run the `main.py` script using the command `python main.py`.
3. When requested, enter a number to be converted into words.

## Functions and Definitions:
* `num_to_word: This function accepts an integer and converts it into equivalent English words. It checks the number length and based on the length, the number is converted into words.
* `main`: This function prompts the user to enter an integer number and checks if it's within the specified range (0 to 999999999999). If so, it calls the function `num_to_word` to convert the input number to words.

* Constants:

UNDER_20: This list stores values for numbers under 20.
TENS: This list stores values for every tenth number up until 100.
ABOVE_100: This dictionary stores values for numbers above 100 and places like 1_000, 1_000_000 and 1_000_000_000.
