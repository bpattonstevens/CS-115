'''
Created on Sep 6, 2017

@author: bpatton

Brandon Patton
CS115

I pledge my honor that I have abided by the Stevens Honor System.
'''
from cs115 import range, map 
import math

"""Inverse Function"""

n = float(input('Enter a number to be inversed: '))

def inverse(n):
    """Returns the reciprocal of the number n entered by the user"""
    
    return 1/n

print (inverse(n))



n = int(input('Enter a positive integer: '))

        
    
def e(n):
    """This function approximates the mathematical value of e using a Taylor 
    expansion"""
    return sum(map(inverse, (map(math.factorial, range(0, n+1)))))
    
    
print(e(n))    


def error(n):
    """This function calculates the error between our calculated value of e and
    the actual value of e"""
    return abs(math.e - e(n))

print('The difference between the values of e is: ', error(n))

    