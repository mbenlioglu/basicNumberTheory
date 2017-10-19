"""
    Created by mbenlioglu on 10/18/2017
"""
from util import gcd


def get_factorization_from_known_roots(number, known_roots):
    """
    Factorizes number to (p x q), where p and q are primes by using known_roots.
    :param number: Number to be factorized
    :type number: int
    :param known_roots: 4 square roots of some x in modulo "number"
    :type known_roots: list[int]
    :return: prime factorization of the number as list
    """
    if len(known_roots) != 4:
        raise ValueError('Wrong number of known roots, expected 4')

    root1 = known_roots[0]
    root2 = None
    for i in known_roots:
        if root1 + i != number:
            root2 = i
            break

    if root2 is None:
        raise ValueError('Root values are wrong!')

    p = gcd(root1 - root2, number)
    q = number / p
    return p, q
