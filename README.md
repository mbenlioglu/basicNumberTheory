# Basic Number Theory functions
Implementation and performance measuring of some of the basic number theory functions.

**Implemented by:**
 * [M.Mucahid Benlioglu](https://github.com/mbenlioglu)

## Getting started
In order to use number theory functions implemented you need to run /basicNumberTheory.py with the following
instructions, while your current working directory is project root.

Note that this project is written and tested under [Python 2.7.x](https://docs.python.org/2/)

### Usage:

Below you can see the help texts for all the functionalities included this project

**General:**
    
    usage: basicNumberTheory.py [-h]
                                {solve-all,factor,residue,exponential,lineq} ...
    
    Implementation and performance measuring of some of the basic number theory functions.
    
    optional arguments:
      -h, --help            show this help message and exit
    
    Available operations:
      Execute "basicNumberTheory.py {subcommand} --help" for more information about each of these subcommands
    
      {solve-all,factor,residue,exponential,lineq}
        solve-all           Solve all example questions using provided example
                            parameters (CS411 hw answers)
        factor              Factorizes given number N to p*q where p and q are
                            primes, by using the provided 4 square roots
        residue             Calculates residues and quadratic residues and their
                            generators of the range 0-N
        exponential         Calculates c^d mod n where n = p*q, c = m^e mod n and
                            d = e^-1 mod n from given p, q, m, e
        lineq               Finds all solutions of x that satisfies a*x = b mod n
    
    Examples:
    -----------
    
    python basicNumberTheory.py solve-all
    python basicNumberTheory.py factor --base {some number} --roots {root1} {root2} {root3} {root4}
    python basicNumberTheory.py lineq {num1} {num2} {num2}

**Example question solutions:**

Solutions and testing with provided inputs under /src/values/example_params for functions implemented in this repository.
(which are related with CS411 questions)

To see the output of these example runs type the following command in the project root
    
    $ python basicNumberTheory.py solve-all

**Factorization:**

    usage: basicNumberTheory.py factor [-h] [--roots R1 R2 R3 R4] N
    
    positional arguments:
      N                    Number that will be factorized into p*q
    
    optional arguments:
      -h, --help           show this help message and exit
      --roots R1 R2 R3 R4  All 4 square roots of some number y, in mod n

**Calculating residues & quadratic residues:**

    usage: basicNumberTheory.py residue [-h] --base N [--quadratic]
                                        [--get-generators]
    
    optional arguments:
      -h, --help        show this help message and exit
      --base N          In which range residues should be searched (0-N)
      --quadratic       Get quadratic residues
      --get-generators  Add generators of the found group to the output

**Exponentiation using Chinese Remainder Theorem or directly:**

    

**Linear equation solving under given modulus:**

