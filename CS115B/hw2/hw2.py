'''
Created on 9/20/17
@author:   bpatton
           lking
           
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

Brandon Patton
Liam King

CS115 - Hw 2
'''
import sys
from cs115 import map, reduce, filter

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.

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
    and add the scores up for the total score of the word'''
    if S == '':
        return 0
    return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

def list_of_words(Rack, Dictionary):
    """Returns the list of possible words from the Rack."""
    return filter(lambda word: is_word_possible(Rack, word), Dictionary)
 
def remove_letter(letter, Rack):
    """Removes all appearances of the letter in the Rack."""
    if Rack[0] == letter:
        return Rack[1:]
    return [Rack[0]] + remove_letter(letter, Rack[1:])
       
 
def is_word_possible(Rack, word):
    """Returns true if the word can be made from letters in the Rack."""
    if word == "":
        return True
    if word[0] in Rack:
        return is_word_possible(remove_letter(word[0], Rack), word[1:])
    return False
 
def scoreList(Rack):
    """Returns all the possible words and respective scores that can be made from the letters taken in."""
    return map(lambda word: [word, wordScore(word, scrabbleScores)], list_of_words(Rack, Dictionary))
       
def bestWord(Rack):
    """Returns the word with the highest possible score from the Rack."""
    def besterWord(x, y):
        """Compares the values of 2 words and returns the larger one."""
        if x[1] > y[1]:
            return x
        return y
    scorelist = scoreList(Rack)
    if scorelist == []:
        return ["", 0]
    return reduce(lambda x, y: besterWord(x, y), scorelist)


