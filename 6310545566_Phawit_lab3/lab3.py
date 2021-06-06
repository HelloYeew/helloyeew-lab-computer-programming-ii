from operator import add, mul, mod


# We can transform multiple-argument functions into a chain of single-argument, higher order functions by taking
# advantage of lambda expressions. Your solution to this problem should fit entirely on the return line.

def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add, mul, mod
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    >>> curried_mul = lambda_curry2(mul)
    >>> mul_5 = curried_mul(5)
    >>> mul_5(42)
    210
    >>> lambda_curry2(mod)(123)(10)
    3
    """
    return lambda x: lambda y: func(x,y)


# Write a function that takes in a function cond and a number n and prints numbers from 1 to n where calling cond on
# that number returns True.

def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> keep_ints(is_even, 10)
    2
    4
    6
    8
    10
    """
    i = 1
    while i <= n:
        if cond(i):
            print(i)
        i += 1

    


# Write a function similar to keep_ints like before, but now it takes in a number n and returns a function that has
# one parameter cond. The returned function prints out numbers from 1 to n where calling cond on that number returns
# True.

def make_keeper(n):
    """Returns a function which takes one parameter cond and prints out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(15)(is_even)
    2
    4
    6
    8
    10
    12
    14
    """
    def print_function(condition):
        i = 1
        while i <= n:
            if condition(i):
                print(i)
            i += 1
    return print_function


# Consider the following implementations of count_factors and count_primes:

def count_factors(n):
    """Return the number of positive factors that n has.
    >>> count_factors(6)   # 1, 2, 3, 6
    4
    >>> count_factors(4)   # 1, 2, 4
    3
    """
    i, count = 1, 0
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    return count


def count_primes(n):
    """Return the number of prime numbers up to and including n.
    >>> count_primes(6)   # 2, 3, 5
    3
    >>> count_primes(13)  # 2, 3, 5, 7, 11, 13
    6
    """
    i, count = 1, 0
    while i <= n:
        if is_prime(i):
            count += 1
        i += 1
    return count


def is_prime(n):
    return count_factors(n) == 2  # only factors are 1 and n


# The above implementations look quite similar! Generalize this logic by writing a function count_cond, which takes
# in a two-argument predicate function condition(n, i). count_cond returns a one-argument function that takes in n,
# which counts all the numbers from 1 to n that satisfy condition when called.

def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function Condition, where
    the first argument for Condition is N and the second argument is the
    number from 1 to N.

    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2)   # 1, 2
    2
    >>> count_factors(4)   # 1, 2, 4
    3
    >>> count_factors(12)  # 1, 2, 3, 4, 6, 12
    6

    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    def count_function(n):
        count = 0
        i = 1
        while i <= n:
            if condition(n,i):
                count += 1
            i += 1
        return count
    return count_function
