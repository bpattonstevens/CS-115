'''
Created on Sep 5, 2017

@author: bpatton
'''
from cs115 import range, map, reduce

def div(k):
    """Checks whether 42 is evenly divisible by an integer k"""
    return 42 % k == 0

def divides(n):
    def div(k):
        return n % k == 0
    return div

print(divides(100)(5))

def increment(n):
    """Returns a function that takes in k and adds it to n."""
    def add_n_to(k):
        return k + n     
    return add_n_to

def inc_all(nums, n):
    """Add n to every number in a given list of numbers."""
    return map(increment(n), nums)

def test_inc_all():
    '''Tests for inc_all. Correct tests print True.'''
    print(inc_all([], 2) == [])
    print(inc_all([1, 3, 5], 2) == [3, 5, 7])
    print(inc_all([-2, -1, 0, 1, 2], 10) == [8, 9, 10, 11, 12])

def sqr(x):
    return x*x

def span(lst):
    return reduce(max, lst) - reduce(min, lst)


def add(a, b):
    return a + b

def mult(a, b):
    return a*b

def gauss(n):
    return reduce(add, range(1, n + 1))

def sum_of_squares(n):
    return reduce(map(sqr, range(1, n + 1)))

words = ['abate', 'abbey', 'abet', 'abhor', 'abide', 'able', 'ably',
         'about', 'above', 'abundant', 'abuse', 'abyss', 'ac', 'ace',
         'ache', 'achy', 'acid', 'acne', 'acorn', 'acre', 'acrid']

def make_len(n):
    '''Assume n is a non-negative integer. Return a function.
    That function applies to strings. It concatenates * characters
    to the given string, to make its length at least n.'''
    def pad_it(word):
        return word + '*' * (n - len(word))
    return pad_it

def pad(words):
    '''Assume words is a non-empty list of strings. Let n be the
    length of the longest. Return a list of the same strings except
    with enough * characters appended to make each one length n.'''
    return (make_len(reduce(max, map(len, words))), words)

def test_pad():
    '''Tests for pad. Correct tests print True.'''
    print(pad(['abate', 'abbey']) == ['abate', 'abbey'])  # no padding
    print(pad(['a', 'cat']) == ['a**', 'cat'])
    print(pad(['three', 'cats', 'asleep', 'now']) \
           == ['three*', 'cats**', 'asleep', 'now***'])
                  
list_of_strings = ['hello', 'my', 'name', 'is', 'brandon']
print(map(len, list_of_strings))

list_of_ints = [1, 2, 3, 4, 5]
print(reduce(mult, list_of_ints))


           
    
    

print(span([3, 1, 42, 7, -1]))
print(gauss(10))
