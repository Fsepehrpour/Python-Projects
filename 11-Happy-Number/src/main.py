def is_happy(num: int) -> bool:
    """Check whether a given number is a happy number.

    A happy number is a number defined by a specific process involving the sum of the squares of its digits.
    How you determine whether a number is happy: Start with any positive integer. Replace the number by the sum of the squares of its digits. Repeat the process with the new number.
    Check if this process leads to the number 1. If it does, then the original number is considered a "happy number."
    If the process enters a cycle that does not include 1, the number is considered "unhappy" or "sad."

    :param n: The number to check.
    :type n: int
    :returns: True if the number is a happy number, False otherwise
    :rtype: bool

    :Example:

    >>> is_happy(19)
    True

    >>> is_happy(2)
    False
    """
    seen_numbers = set()
    while (num != 1) and (num not in seen_numbers):
        seen_numbers.add(num)
        num = sum([int(i) ** 2 for i in str(num)])

    return num == 1


if __name__ == "__main__":
    assert is_happy(19), 'Test Case 1 Failed'
    assert not is_happy(2), 'Test Case 2 Failed'
    assert is_happy(44), 'Test Case 3 Failed'
    assert is_happy(86), 'Test Case 4 Failed'
    assert is_happy(139), 'Test Case 5 Failed'

    print('All test cases pass')


