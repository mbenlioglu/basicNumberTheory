"""
    Created by mbenlioglu on 10/18/2017
"""


def multiplicative_inverse(num, modulo):
    """
    Return the multiplicative inverse of the given number in given modulo or raises a ValueError if no inverse exists.
    :param num: Number to be inverted
    :type num: int
    :param modulo:
    :type modulo: int
    :raises ValueError if num has no inverse
    :return: multiplicative inverse of the number in the given modulo
    """
    t = 0
    r = modulo
    newt = 1
    newr = num

    while newr != 0:
        quotient = r / newr
        t, newt = newt, t - quotient * newt
        r, newr = newr, r - quotient * newr
    if r > 1:
        raise ValueError('number does not have a multiplicative inverse in given modulo')
    return t if t > 0 else t + modulo


def gcd(num1, num2):
    """
    Calculates the greatest common divisor of given 2 numbers
    :param num1: First number
    :type num1: int
    :param num2: Second number
    :type num2
    :return: Greatest common divisor
    """
    big, small = (num1, num2) if num1 > num2 else (num2, num1)

    remainder = -1
    while remainder != 0:
        quotient = big / small
        remainder = big - quotient * small
        big, small = small, remainder
    return big


def get_prime_factorization(n):
    """
    Calculates the prime factorization of the given number
    :param n: number to be factorized
    :type n: int
    :return: Prime factors and how and their exponents in list[list] form
    e.g: get_prime_factorization(24) returns [[2, 3], [3, 1]]
    """
    fac = 2
    factors = []
    while fac * fac <= n:
        if n % fac:
            fac += 1
        else:
            exp = 0
            while not n % fac:
                n //= fac
                exp += 1
            factors.append([fac, exp])
    if n > 1:
        factors.append([n, 1])
    return factors


def get_relatively_primes(num):
    """
    Calculates a list of numbers that are in range 0 - num and are relatively prime to num
    :param num: number that determines the limit
    :type num: unsigned int
    :return: list of relatively prime numbers
    """
    if num < 1:
        raise ValueError('Invalid number, expected a positive integer')
    return [x for x in range(num) if gcd(x, num) == 1]


def get_generators(group, modulo):
    """
    Calculates all the generators in the given group
    :param group: List of integers, forming a group
    :type group: list[int]
    :param modulo: In which modulo we are performing this operation
    :type modulo: int
    :return: list of generators
    """
    is_generator = {x: False for x in group}
    for i in group:
        mult = i
        generated_dict = {x: False for x in group}
        while True:
            if mult in generated_dict:
                generated_dict[mult] = True
            else:
                raise ValueError('Supplied group is not a group')
            if mult == 1 or mult == 0:
                break
            mult = (i * mult) % modulo
        is_generator[i] = all(x is True for x in generated_dict.values())

    return sorted([key for key in is_generator if is_generator[key]])
