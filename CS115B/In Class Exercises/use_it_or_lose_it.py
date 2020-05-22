'''
Created on Sep 18, 2017

@author: bpatton
'''
from cs115 import map

def powerset(lst):
    """Returns the power set of the list, that is, the set of all subsets of the list."""
    if lst == []:
        return [[]]
    lose_it = powerset(lst[1:])
    use_it = map(lambda subset: [lst[0]] + subset, lose_it)
    return lose_it + use_it

def subset(target, lst):
    '''Determines whether or not it is possible to create target sum using the values in the list.
    Values in the list can be positive, negative, or zero.'''
    if target == 0:
        return True
    if lst == []:
        return False
    return subset(target - lst[0], lst[1:]) or subset(target, lst[1:])

def subset_with_values(target, lst):
    '''Determines whether or not it is possible to create the target sum
    using values in the list. Values in the list can be positive, negative, or zero. The function
    returns a tuple of exactly two items.  The first is a Boolean that indicates True if the sum is
    possible and False if it's not. The second element in the tuple is a list of all values that add up to 
    make the target sum.'''
    if target == 0:
        return (True, [])
    if lst == []:
        return (False, [])
    use_it = subset_with_values(target - lst[0], lst[1:])
    if use_it[0]:
        return (True, [lst[0]] + use_it[1])
    return subset_with_values(target, lst[1:])

print(subset_with_values(8, [7, 2, 2, 2, 2]))
    

print(powerset(['a', 'b', 'c']))