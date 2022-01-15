"""
Implement the function that returns the highest common factor
(or greatest common divisor) of two integers passed as arguments

Highest common factor of 'a' and 'b' is the largest number that
can divide both 'a' and 'b' in common. For example, hcf of 16 and
24 is 8 (though it is commonly divisible also by 2 and 4).

Example usage
-------------
    >>> hcf(20, 4)
    4

    >>> hcf(150, 8)
    2

    >>> hcf(16, 24)
    8

    >>> hcf(48, 6)
    6

"""
def hcf(a: int, b: int) -> int:
    """
    Returns the highest common factor of arguments 'a' and 'b'.

    Example
    -------
        >>> hcf(100, 2)
        2

        >>> hcf(5, 7)
        1

        >>> hcf(20, 8)
        4
    """
    while b:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    from doctest import testmod
    testmod()