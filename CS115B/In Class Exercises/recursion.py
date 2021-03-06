'''
Created on Sep 12, 2017

@author: bpatton
'''

from cs115 import map, reduce

import math


def tower(n):
    """Computes 2^(2^(2...)) with n twos, using recursion."""
    if n == 0:
        return 1
    else:
        return 2**(tower(n - 1))



def tower_reduce(n):
    def power(x, y):
        return y ** x
    if n == 0:
        return 1
    return reduce(power, [2] * n)


print(map(tower_reduce, range(5)))

def length(lst):
    """Returns the length of lst"""
    if lst == []:
        return 0
    return 1 + length(lst[1:])




def reverse(lst):
    """Takes as input a list of elements and returns the list in reverse order.
    """
    if lst == []:
        return []
    return reverse(lst[1:]) + [lst[0]]

def member(x, lst):
    """Returns True if x is contained in the list and False otherwise."""
    if lst == []:
        return False
    if x == lst[0]:
        return True
    return member(x, lst[1:])

def power(x, y):
    if y == 0:
        return 1
    return x * power(x, y - 1)

def power_tail(x, y):
    def power_tail_helper(x, y, accum):
        if y == 0:
            return accum
        return power_tail_helper(x, y - 1, x * accum)
    return power_tail_helper(x, y, 1)

def mystery(n):
    return m_help(n, 0)

def m_help(n, r):
    if n == 0:
        return r
    return m_help(n//10, r * 10 + n % 10)


def my_map(f, lst):
    if lst == []:
        return []
    return [f(lst[0])] + my_map(f, lst[1:])

def my_reduce(f, lst):
    def my_reduce_helper(f, lst, accum):
        if lst == []:
            return accum
        return my_reduce_helper(f, lst[1:], f(lst[0], accum))
    
    
    if lst == []:
        raise TypeError('my_reduce() of empty sequence with no initial value')
    return my_reduce_helper(f, lst[1:], lst[0])

def prime(n):
    """Returns whether or not an integer is prime."""
    possible_divisors = range(2, int(math.sqrt(n)) + 1)
    divisors = filter(lambda x: n % x == 0, possible_divisors)
    return len(divisors) == 0


def primes(n):
    """Returns a list of primes in the range [2, n] computed via the sieve of Eratosthenes."""
    def sieve(lst):
        if lst == []:
            return []
        return [lst[0]] + sieve(filter(lambda x: x % lst[0] != 0, lst[1:]))
    return sieve(range(2, n + 1))

def fib(n):
    """Tree Recursion: occurs when the pending operation for the recursive call is another recursive call"""
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def fun(n):
    if n <= 1:
        print('bye')
        return
    fun(n-1)
    print('hi')
    fun(n-1)
    

L = ['jack', 'and', 'jill', 'went', 'up', 'the', 'hill']















    
    
    

