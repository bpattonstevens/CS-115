'''
Created on Sep 13, 2017

@author: Brandon Patton

I pledge my honor that I have abided by the Stevens Honor System.

bpatton
'''

from cs115 import map

def dot(L, K):
    """This Function will output the dot product of the lists L and K."""
    if L == [] or K == []:
        return 0
    return L[0] * K[0] + dot(L[1:], K[1:])

def explode(S):
    """This Function takes string S as input and returns a list of the characters
    separated in that string."""
    if S == []:
        return []
    return map(lambda c : c, S)



def ind(e, L):
    """This Function takes in an element e and a sequence L and returns the index
    at which e is first found in sequence L."""
    def ind_help(e, L, accum):
        """This Function helps the function ind complete its task by using an 
        accumulator as the value of the index e is first found at."""
        if L == []:
            return accum
        if L == '':
            return accum
        if e == L[0]:
            accum+=1
        return ind_help(e, L[1:], accum + 1)
    return ind_help(e, L, 0)

def removeAll(e, L):
    """This Function takes in an element e and list L and returns list L with all
    instances of element e removed.  e must be a top level element for this function
    to work."""
    if L == []:
        return []
    if e == L[0]:
        return removeAll(e, L[1:])
    return [L[0]] + removeAll(e, L[1:])
        
def myFilter(f, lst):
    """This Function filters a list lst for the specifications listed from function
    f."""
    if lst == []:
        return[]
    if f(lst[0]) == True:
        return [lst[0]] + myFilter(f, lst[1:])
    return myFilter(f, lst[1:])

def deepReverse(L):
    """This Function takes elements of lists and elements that are lists for input,
    and returns the reversal of the list and the reversal of any element that is 
    also a list."""
    if L == []:
        return []
    if isinstance(L[0], list):
        L[0] = deepReverse(L[0])
    return deepReverse(L[1:]) + [L[0]]

    
