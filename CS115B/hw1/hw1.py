'''
Created on Sep 12, 2017

@author: Brandon Patton

I pledge my honor that I have abided by the Stevens Honor System.

bpatton
'''

from cs115 import reduce, map



def mult(x, y):
    """Returns the product of x and y"""
    return x * y

def factorial(n):
    """Returns the factorial of a number"""
    if n == 0:
        return 1
    k = range(1, n + 1)
    return reduce(mult, k)


def add_numerator(a, b):
    """Returns the sum of two numbers"""
    return a + b 


def mean(L):
    """Takes the mean of the numbers in a list"""
    if L == []:
        return []
    return (reduce(add_numerator, L))/len(L)


def divides(n):
    """Returns if n is divisible by any possible factors and returns True if there
    no remainder and False if there is a remainder."""
    def div(k):
        return n % k == 0
    return div
    
def prime(n):
    """Returns False if n is 0 or 1 because both 0 and 1 are neither prime nor 
    composite. Returns True if the number is prime by checking if it is divisible 
    by any numbers beneath it from 2 to n but not including n (This is the value of
    k which changes while the program checks to see if the number is prime)."""
    if n == 0 or n == 1:
        return False
    return sum(map(divides(n), range(2, n))) == 0




    









