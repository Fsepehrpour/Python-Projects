def sum_natural_number(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0

    return n + sum_natural_number(n - 1)
