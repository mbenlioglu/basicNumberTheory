"""
    Created by mbenlioglu on 10/18/2017
"""
import argparse

import time

from src.number_theory import factorization, quadratic_residues, util, chinese_remainder, linear_equations
from src.number_theory.linear_equations import MathError
from src.values import descriptions, example_params


def example_problem_solutions(args):
    # factorization example
    print 'Question 1: Factorization of n as (p x q) given all 4 roots of some y\n'
    print 'n:\n', example_params.factorization_input
    print 'y:\n', example_params.factorization_y
    print 'roots of y:\n', example_params.factorization_y_roots
    factors = factorization.get_factorization_from_known_roots(example_params.factorization_input,
                                                               example_params.factorization_y_roots)
    print 'Prime factorization of n is calculated as (pxq)'
    print 'p:\n', factors[0]
    print 'q:\n', factors[-1]

    # residues
    print '\nQuestion 2: Residues, quadratic residues & generators'
    z_star_46 = quadratic_residues.get_coprimes(46)
    print '2.a): the group Z*_46 = ', z_star_46
    print 'length of Z*_46:', len(z_star_46)
    print '2.b): generators in Z*_46:', util.get_generators(z_star_46, 46)
    q_star_46 = quadratic_residues.get_coprime_quadratic_residues(46)
    print '2.c): the group Q*_46: ', q_star_46
    print 'length of Q*_46:', len(q_star_46)
    print '2.d): generators of Q*_46: ', util.get_generators(q_star_46, 46)

    # exponentiation
    print '\nQuestion 3: Exponentiation & CRT'
    n = example_params.mexp_p * example_params.mexp_q
    c = pow(example_params.mexp_m, example_params.mexp_e, n)
    print '3.a): c = m ** e mod n:\n', c
    print '3.b): number d such that e * d = 1 mod fi(n), where e is', example_params.mexp_e, ':'
    fi_n = (example_params.mexp_p - 1) * (example_params.mexp_q - 1)
    d = util.multiplicative_inverse(example_params.mexp_e, fi_n)
    print d
    m_prime = pow(c, d, n)
    print "m' = c**d mod n:\n", m_prime
    print "Calculation of m' - m = 0 (should show 0 if true):", m_prime - example_params.mexp_m
    print '3.c): Calculating c**d mod n using CRT:'
    p_inverse_mod_q = util.multiplicative_inverse(example_params.mexp_p, example_params.mexp_q)
    q_inverse_mod_p = util.multiplicative_inverse(example_params.mexp_q, example_params.mexp_p)
    chinese_result = chinese_remainder.modular_exponentiation(c, d, [example_params.mexp_p, example_params.mexp_q],
                                                              [p_inverse_mod_q, q_inverse_mod_p], True)
    print 'p_inverse mod q :-->\n', p_inverse_mod_q
    print 'q_inverse mod p :-->\n', q_inverse_mod_p
    print 'c_p = c mod p :-->\n', chinese_result['bases'][0]
    print 'c_q = c mod q :-->\n', chinese_result['bases'][1]
    print 'd_p = d mod (p-1) :-->\n', chinese_result['exponents'][0]
    print 'd_q = d mod (q-1) :-->\n', chinese_result['exponents'][1]
    print 'c_p-d_p = c_p ** d_p mod p :-->\n', chinese_result['values'][0]
    print 'c_q-d_q = c_q ** d_q mod q :-->\n', chinese_result['values'][1]
    print 'Final result:\n', chinese_result['result']
    print '3.d): Time comparison with 100 iterations: '
    t1 = time.clock()
    for i in range(100):
        pow(c, d, n)
    t2 = time.clock()
    print 'Elapsed time for regular exponentiation:', t2 - t1
    t1 = time.clock()
    for i in range(100):
        chinese_remainder.modular_exponentiation(c, d, [example_params.mexp_p, example_params.mexp_q],
                                                 [p_inverse_mod_q, q_inverse_mod_p])
    t2 = time.clock()
    print 'Elapsed time for exponentiation using CRT:', t2 - t1

    # linear equations
    print '\n Question 4: Linear equation solutions:'
    print '4.a):'
    try:
        sols = linear_equations.solve(example_params.linear_a1, example_params.linear_b1, example_params.linear_n)
        print 'Solution(s) for ax = b mod n:'
        for i in sols:
            print i
    except MathError:
        print 'gcd of a, n:', util.gcd(example_params.linear_a1, example_params.linear_n), \
            'is not 1 and does\'t divide number b', example_params.linear_b1
    print '4.b):'
    try:
        sols = linear_equations.solve(example_params.linear_a2, example_params.linear_b2, example_params.linear_n)
        print 'Solution(s) for ax = b mod n:'
        for i in sols:
            print i
    except MathError:
        print 'gcd of a, n:', util.gcd(example_params.linear_a2, example_params.linear_n), \
            'is not 1 and does\'t divide number b', example_params.linear_b2
    print '4.c):'
    try:
        sols = linear_equations.solve(example_params.linear_a3, example_params.linear_b3, example_params.linear_n)
        print 'Solution(s) for ax = b mod n:'
        for i in sols:
            print i
    except MathError:
        print 'gcd of a, n:', util.gcd(example_params.linear_a3, example_params.linear_n), \
            'is not 1 and does\'t divide number b', example_params.linear_b3


def factor(args):
    factors = factorization.get_factorization_from_known_roots(args.toBeFactored,
                                                               args.roots)
    print 'Prime factorization of input is calculated as (pxq)'
    print 'p:\n', factors[0]
    print 'q:\n', factors[-1]


def residue(args):
    if args.quadratic:
        q_star = quadratic_residues.get_coprime_quadratic_residues(args.base)
        print 'The group of quadratic residues Q* on given base is: ', q_star
        print 'with', len(q_star), 'elements'
        if args.get_generators:
            print 'Generators of this group is:', util.get_generators(q_star, args.base)
    else:
        z_star = quadratic_residues.get_coprimes(args.base)
        print 'The group Z* of given base is:\n', z_star,
        print 'with', len(z_star), 'elements'
        if args.get_generators:
            print 'Generators of the given group is:\n', util.get_generators(z_star, args.base)


def exponentiation(args):
    n = args.params[0] * args.params[1]
    c = pow(args.params[2], args.params[3], n)

    print '3.a): c = m ** e mod n:\n', c
    print '3.b): number d such that e * d = 1 mod fi(n), where e is', args.params[3], ':'
    fi_n = (args.params[0] - 1) * (args.params[1] - 1)
    d = util.multiplicative_inverse(example_params.mexp_e, fi_n)
    print d

    p_inverse_mod_q = util.multiplicative_inverse(example_params.mexp_p, example_params.mexp_q)
    q_inverse_mod_p = util.multiplicative_inverse(example_params.mexp_q, example_params.mexp_p)

    if args.perf:
        print 'Running performance test over 200 repetitions with given inputs...'
        t1 = time.clock()
        for i in range(200):
            pow(c, d, n)
        t2 = time.clock()
        print 'Elapsed time for regular exponentiation:', t2 - t1
        t1 = time.clock()
        for i in range(200):
            chinese_remainder.modular_exponentiation(c, d, [args.params[0], args.params[1]],
                                                     [p_inverse_mod_q, q_inverse_mod_p])
        t2 = time.clock()
        print 'Elapsed time for exponentiation using CRT:', t2 - t1
    elif args.method == 'direct':
        print 'Result is:\n', pow(c, d, n)
    elif args.method == 'crt':
        chinese_result = chinese_remainder.modular_exponentiation(c, d, [args.params[0], args.params[1]],
                                                                  [p_inverse_mod_q, q_inverse_mod_p], True)
        if args.get_all_intermediate:
            print 'p_inverse mod q :-->\n', p_inverse_mod_q
            print 'q_inverse mod p :-->\n', q_inverse_mod_p
            print 'c_p = c mod p :-->\n', chinese_result['bases'][0]
            print 'c_q = c mod q :-->\n', chinese_result['bases'][1]
            print 'd_p = d mod (p-1) :-->\n', chinese_result['exponents'][0]
            print 'd_q = d mod (q-1) :-->\n', chinese_result['exponents'][1]
            print 'c_p-d_p = c_p ** d_p mod p :-->\n', chinese_result['values'][0]
            print 'c_q-d_q = c_q ** d_q mod q :-->\n', chinese_result['values'][1]

        print 'Final result:\n', chinese_result['result']


def linear_eq(args):
    try:
        sols = linear_equations.solve(args.params[0], args.params[1], args.params[2])
        print 'Solution(s) for x that satisfies ax = b mod n:'
        for i in sols:
            print i
    except MathError:
        print 'gcd of a, n:', util.gcd(args.params[0], args.params[2]), \
            'is not 1 and does\'t divide number b', args.params[1]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=descriptions.intro,
                                     epilog=descriptions.examples,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    subparsers = parser.add_subparsers(title=descriptions.subparser_title, description=descriptions.subparser_help)

    # parser for "solve-all"
    parser_solve = subparsers.add_parser('solve-all', help=descriptions.help_solve_all)
    parser_solve.set_defaults(func=example_problem_solutions)

    # parser for "factor"
    parser_fac = subparsers.add_parser('factor', help=descriptions.help_factor)
    parser_fac.add_argument('toBeFactored', type=long, nargs=1, metavar='N', help=descriptions.help_factor_n)
    parser_fac.add_argument('--roots', nargs=4, metavar=('R1', 'R2', 'R3', 'R4'), type=long,
                            help=descriptions.help_factor_roots)
    parser_fac.set_defaults(func=factor)

    # parser for "residue"
    parser_res = subparsers.add_parser('residue', help=descriptions.help_residue)
    parser_res.add_argument('--base', nargs=1, metavar='N', type=long, required=True,
                            help=descriptions.help_residue_base)
    parser_res.add_argument('--quadratic', action='store_true', help=descriptions.help_residue_quadratic)
    parser_res.add_argument('--get-generators', action='store_true', help=descriptions.help_residue_get_generators)
    parser_res.set_defaults(func=residue)

    # parser for "exponential"
    parser_exp = subparsers.add_parser('exponential', help=descriptions.help_exponential)
    parser_exp.add_argument('--params', type=long, nargs=4, metavar=('p', 'q', 'm', 'e'),
                            help=descriptions.help_exponential_nums)
    parser_exp.add_argument('--method', choices=['direct', 'crt'], default='crt',
                            help=descriptions.help_exponential_method)
    parser_exp.add_argument('--get-all-intermediate', action='store_true', help=descriptions.help_exponential_get_all)
    parser_exp.add_argument('--perf', action='store_true', help=descriptions.help_exponential_perf)
    parser_exp.set_defaults(func=exponentiation)

    # parser for "lineq"
    parser_lineq = subparsers.add_parser('lineq', help=descriptions.help_lineq)
    parser_lineq.add_argument('--params', type=long, nargs=3, metavar=('a', 'b', 'mod'),
                              help=descriptions.help_lineq_nums)
    parser_lineq.set_defaults(func=linear_eq)

    arguments = parser.parse_args()
    arguments.func(arguments)
