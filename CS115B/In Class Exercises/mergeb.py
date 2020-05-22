'''
Created on Nov 9, 2017

@author: bpatton
'''

def num_matches(list1, list2):
    '''Returns the number of elements that the two lists have in common.'''
    list1.sort()
    list2.sort()
    matches = i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches

list1 = ['b', 'd', 'e']
list2 = ['a', 'b', 'c', 'd']

def keep_matches(list1, list2):
    '''Returns a list of the elements that the two lists have in common.'''
    list1.sort()
    list2.sort()
    matches = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches

def drop_matches(list1, list2):
    '''Returns a list of the elements that are not in common in list1 and list2.'''
    list1.sort()
    list2.sort()
    result = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    while i < len(list1):
        result.append(list1[i])
        i += 1
    while j < len(list2):
        result.append(list2[j])
        j += 1
    return result

print(drop_matches(list1, list2))


        