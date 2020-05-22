'''
Created on 10/13/17
@author:   Brandon Patton
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

bpatton

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n % 2 != 0:
        return True
    else:
        return False
# The base 2 representation of the number 42 is 101010
#If you are given an odd base 10 number, the rightmost bit will be 1 in base 2. 
#If you are given an even base 10 number, the rightmost bit will be 0 in base 2.
#The original number is undergoing floor division when the rightmost bit is taken away.
#If N is odd, add a 1 at the rightmost bit of the binary version of Y
#If N is even, add a 0 at the rightmost bit of the binary version of Y.


def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    if n % 2 == 1:
        return numToBinary(n//2) + '1'
    return numToBinary(n//2) + '0' 


def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    def bToN_helper(s, accum):
        if s == '':
            return 0
        if int(s[-1]) == 1:
            return accum + bToN_helper(s[:-1], accum * 2)
        return bToN_helper(s[:-1], accum * 2)
    return bToN_helper(s, 1)
   

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if s == '':
        return 0
    s = numToBinary(binaryToNum(s) + 1)
    return ((8 - len(s)) * '0') + s[-8:]



def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    print(s)
    if s == '':
        return 
    if n == 0:
        return
    (count(increment(s), n-1))
    

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternar+y representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    if n % 3 == 1:
        return numToTernary(n//3) + '1'
    elif n % 3 == 0:
        return numToTernary(n//3) + '0' 
    elif n % 3 == 2:
        return numToTernary(n//3) + '2'

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    def tToN_helper(s, accum):
        if s == '':
            return 0
        return int(s[-1])*accum + tToN_helper(s[:-1], accum * 3)
    return tToN_helper(s, 1)

    
