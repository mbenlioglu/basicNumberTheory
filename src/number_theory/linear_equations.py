"""
    Created by mbenlioglu on 10/19/2017
"""
from util import gcd, multiplicative_inverse


class MathError(Exception):
    pass


def solve(a, b, n):
    """
    Finds and returns all the solutions for x that satisfies ax = b mod n. If no solution exists MathError is raised
    :type a: int
    :type b: int
    :type n: int
    :return: All solutions of x
    :raises MathError if x no solution
    """
    d = gcd(a, n)

    if d == 1:
        return [(b * multiplicative_inverse(a, n)) % n]
    elif b % d == 0:  # d divides b
        x_tilda = (b/d * multiplicative_inverse(a/d, n/d) % n/d)
        return [x_tilda + i*n/d for i in range(d)]
    else:
        raise MathError('No x solves the equation!')
