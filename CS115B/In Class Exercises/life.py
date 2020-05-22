#
# life.py - Game of Life lab
#
# Name:  Brandon Patton
# Pledge:  I pledge my honor that I have abided by the Stevens Honor System.
#bpatton

import random

def createOneRow(width):
    """ returns one row of zeros of width "width"...
         You might use this in your createBoard(width, height) function """
    row = []
    # print "width is", width
    for _ in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """ returns a 2d array of width and height """
    A = []
    for _ in range(height):
        A += [createOneRow(width)]
    return A

import sys
def printBoard( A ):
    """ this function prints the 2d list-of-lists
    A without spaces (using sys.stdout.write)"""
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )        

def diagonalize(width,height):
    """ creates an empty board and then modifies it
    so that it has a diagonal strip of "on" cells."""
    A = createBoard( width, height )
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(w, h):
    A = createBoard(w, h)
    for row in range(1,h - 1):
        for col in range(1, w - 1):
            if row >= col or row <= col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def randomCells(w, h): 
    A = createBoard( w, h )
    for row in range(1, h - 1):
        for col in range(1, w - 1):
            if row == col:
                A[row][col] = random.choice([0,1])
            else:
                A[row][col] = random.choice([0,1])
                
    return A

def copy( A ):
    new_list = []
    for x in A:
        if isinstance(x, list):
            new_list.append(copy(x))
        else:
            new_list.append(x)
    return new_list

def innerReverse( A ):
    for row in range(1, len(A) - 1):
        for col in range(1, len(A) - 1):
            if A[row][col] == 1:
                A[row][col] = 0
            else:
                A[row][col] = 1
    return A


def countNeighbors(row, col, A):
    count = 0
    if A[row - 1][col - 1] == 1:
        count += 1
    if A[row - 1][col] == 1:
        count += 1
    if A[row][col-1] == 1:
        count += 1
    if A[row + 1][col] == 1:
        count += 1
    if A[row][col + 1] == 1:
        count += 1
    if A[row + 1][col - 1] == 1:
        count += 1
    if A[row - 1][col + 1] == 1:
        count += 1
    if A[row + 1][col + 1] == 1:
        count += 1
    return count

def next_life_generation( A ):
    """ makes a copy of A and then advanced one 
    generation of Conway's game of life within
    the *inner cells* of that copy.
    The outer edge always stays 0.
    """                
    newA = copy(A)
    for row in range(1, len(A) - 1):
        for col in range(1, len(A) - 1):
            if countNeighbors(row, col, A) < 2:
                newA[row][col] = 0 
            if countNeighbors(row, col, A) > 3:
                newA[row][col] = 0
            if  A[row][col] == 0 and countNeighbors(row, col, A) == 3:
                newA[row][col] = 1
    return newA


                    
            
    



