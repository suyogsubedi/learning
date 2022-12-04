def addition(*args):
    """Compute and return the sum of two numbers.

    Usage examples:
    >>> addition(4, 2)
    6
    >>> addition(4.2, 2)
    6.2
    """
    if len(args) == 0:
        return "Can't add empty things, can I ?"
    return (sum(args))
# python -m doctest -v doc_string_test.py