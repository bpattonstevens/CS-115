'''
Created on 9/27/17
@author:   bpatton
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

Brandon Patton

CS115 - Hw 3
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



def giveChange(amount, change):
    '''Takes the same kind of input as the previous change function, but 
    instead returns a list whose first item is the minimum number of coins and
    whose second item is a list of the coins in that optimal solution.'''
    if amount == 0:
        return [0, []]
    if change == []:
        return [float("inf"), []]
    if change[0] > amount:
        return giveChange(amount, change[1:])
    [use_it_amount, use_it_list] = giveChange(amount-change[0], change)
    [lose_it_amount, lose_it_list] = giveChange(amount, change[1:])
    if use_it_amount + 1 < lose_it_amount:
        use_it_list.append(change[0])
        return [use_it_amount + 1, use_it_list]
    else:
        return [lose_it_amount, lose_it_list]


# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def letterScore(letter, scorelist):
    '''This function takes as input a single letter string of 'letter' and a list where
    each element in the list is of form [character, value] where character is a single letter
    and value is a number associated with that letter, or in other words its scrabble
    score.  This specific function returns the score of the letter inputed into the function.'''
    if scorelist == []:
        return 0
    first = scorelist[0]
    if first[0] == letter:
        return first[1]
    return letterScore(letter, scorelist[1:])

def wordScore(S, scorelist):
    '''Takes input in form of a string 'S' and a scorelist as described above in the
    docstring for letterScore. This function will return as output the scrabble score
    for the inputted word/string using letterScore to calculate the score of each letter
    and adds the scores up for the total score of the word'''
    if S == '':
        return 0
    return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)
    
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.
    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    if dct == []:
        return []
    if scores == []:
        return ['', 0]
    return [dct[0], wordScore(dct[0], scores)] + wordsWithScore(dct[1:], scores)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n].'''
    def take_helper(n, L, accum, lst):
        '''Helps the take function by using an accumulator to start and end the
        iterations the take function should complete'''
        if n == accum:
            return lst
        lst = lst + [L[0]]
        return take_helper(n, L[1:], accum + 1, lst)
    if n == 0:
        return L
    if L == []:
        return []
    return take_helper(n, L, 0, [])
 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    def drop_helper(n, L, accum):
        '''Helps the drop function by using an accumulator to start and end the
        iterations the take function should complete'''
        if n == accum:
            return L
        return drop_helper(n, L[1:], accum + 1)
    if n == 0:
        return 0
    if L == []:
        return []   
    return drop_helper(n, L, 0)
    


