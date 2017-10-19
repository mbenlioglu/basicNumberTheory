"""
    Created by mbenlioglu on 10/19/2017
"""


def modular_exponentiation(base, exponent, primes, inverses, return_all=False):
    """
    Calculates pow(base, exponent, md), where md is the base we wish to make the computation using Chinese Remainder
    Theorem
    :type base: long
    :type exponent: long
    :param primes: List of relatively prime numbers such that multiplication of these numbers make the modulus we wish to
    make the calculation
    :type primes: list[long]
    :param inverses: For all m_i = (n/n_i)**-1 mod n_i, where n is the desired modulus, n_i is the ith element in N
    :type inverses: list[long]
    :param return_all: Flag that determines whether the intermediate variables are returned as well
    :return: pow(base,exponent,modulo) or this result and all intermediate values as dictionary
    """
    if len(primes) != len(inverses):
        raise ValueError('Length of primes and inverses do not match')

    bases = [0] * len(primes)
    exponents = [0] * len(primes)
    values = [0] * len(primes)

    for i, n in enumerate(primes):
        bases[i] = base % n
        exponents[i] = exponent % (n - 1)
        values[i] = pow(bases[i], exponents[i], n)

    result = 0
    for i in range(len(values)):
        result += values[i] * primes[i] * inverses[i]

    if return_all:
        return {'bases': bases, 'exponents': exponents, 'values': values, 'result': result}
    else:
        return result
