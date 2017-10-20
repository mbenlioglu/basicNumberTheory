"""
    Created by mbenlioglu on 10/19/2017
"""

# general explanations
intro = 'Implementation and performance measuring of some of the basic number theory functions.'
examples = '''\
Examples:
-----------

python %(prog)s solve-all
python %(prog)s factor --base {some number} --roots {root1} {root2} {root3} {root4}
python %(prog)s lineq {num1} {num2} {num2} 

'''

# subparsers general help
subparser_title = 'Available operations'
subparser_help = 'Execute "%(prog)s {subcommand} --help" for more information about each of these subcommands'

# common

# subcommand specific
help_solve_all = 'Solve all example questions using provided example parameters (CS411 hw answers)'
help_factor = 'Factorizes given number N to p*q where p and q are primes, by using the provided 4 square roots'
help_residue = "Calculates residues and quadratic residues and their generators of the range 0-N"
help_exponential = 'Calculates c^d mod n where n = p*q, c = m^e mod n and d = e^-1 mod n from given p, q, m, e'
help_lineq = 'Finds all solutions of x that satisfies a*x = b mod n'

# switches
help_lineq_nums = 'a, b and n in the equation a*x = b mod n. In that order'

help_factor_n = 'Number that will be factorized into p*q'
help_factor_roots = 'All 4 square roots of some number y, in mod n'

help_residue_base = 'In which range residues should be searched (0-N)'
help_residue_quadratic = 'Get quadratic residues'
help_residue_get_generators = 'Add generators of the found group to the output'

help_exponential_nums = 'p, q, m, e that are used to calculate c^d mod n where n = p*q, c = m^e mod n & d = e^-1 mod n'
help_exponential_method = 'Either direct or crt. Direct, directly takes power and reduces to mod n, CRT uses chinese' \
                          'remainder theorem to reduce the calculation'
help_exponential_get_all = 'Print all intermediate values during crt method (ignored in direct)'
help_exponential_perf = 'Does not produce output, just compares the elapsed time between direct and crt'
