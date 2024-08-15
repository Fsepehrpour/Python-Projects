# Happy Number 
This GitHub repository contains a Python script that determines whether a given number is a happy number. A happy number is a number that eventually reaches 1 when you repeatedly replace it with the sum of the squares of its digits. If the process results in a cycle that does not include 1, the number is considered "unhappy" or "sad."

For example, 19 is a happy number. Here's why:
* 1² + 9² = 82
* 8² + 2² = 68
* 6² + 8² = 100
* 1² + 0² + 0² = 1

This script provides a simple function `is_happy(num: int) -> bool` that checks whether a given number is happy.

## Project Structure
.
├── src/
│    └── main.py
└── README.md

## Requirements
* Python 3.7+
* A basic understanding of Python and its core concepts

## Learning Outcomes
This project will help you practice:
* **Algorithmic Thinking**: Developing and refining an algorithm to solve a specific problem, including identifying edge cases and optimizing for efficiency.
* Using **Python's core functionality**, such as lists, loops, and sets, to solve a complex problem.
* Incorporating **mathematical concepts** in a programming environment.
* Writing and running **unit tests** to ensure that your code is working as intended.
* Improve your problem-solving abilities and **debugging skills**.
