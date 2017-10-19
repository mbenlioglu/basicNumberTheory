"""
    Created by mbenlioglu on 10/18/2017
"""
from util import gcd


def get_quadratic_residues(num):
    """
    Returns a list of integers which have square roots in modulo num
    :param num: modulo
    :type num: int
    :return: list[int]
    """
    has_roots = [False] * num

    for i in range(1, num):
        has_roots[i**2 % num] = True

    return [x for x in range(num) if has_roots[x]]


def get_coprime_quadratic_residues(num):
    """
    Returns a list of integers which have square roots in modulo num and are relatively prime with num
    :param num: modulo
    :type num: int
    :return: list[int]
    """
    return [x for x in get_quadratic_residues(num) if gcd(x, num) == 1]
