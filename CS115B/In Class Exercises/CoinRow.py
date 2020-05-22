'''
Created on Sep 25, 2017

@author: bpatton
'''

def coin_row(lst):
    if lst == []:
        return 0
    return max(lst[0] + coin_row(lst[2:]), coin_row(lst[1:]))

def coin_row_with_values(lst):
    if lst == []:
        return [0, []]
    use_it = coin_row_with_values(lst[2:])
    new_sum = lst[0] + use_it[0]
    lose_it = coin_row_with_values(lst[1:])
    if new_sum > lose_it[0]:
        return [new_sum, [lst[0]] + use_it[1]]
    return lose_it

def distance(first, second):
    if first == '':
        return len(second)
    if second == '':
        return len(first)
    if first[0] == second[0]:
        return distance(first[1:], second[1:])
    substitution = distance(first[1:], second[1:])
    deletion = distance(first[1:], second)
    insertion = distance(first, second[1:])
    return 1 + min(substitution, deletion, insertion)