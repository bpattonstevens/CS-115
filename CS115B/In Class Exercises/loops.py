'''
Created on Oct 31, 2017

@author: bpatton
'''

def mapSqr(L):
    result = []
    for x in L:
        result.append(x**2)        
    return result

def find_max(lst):
    if lst == []:
            return None
    max_val = lst[0]
    for x in lst:
        if x > max_val:
            max_val = x
    return max_val      

def find_min_max(lst):
    if lst == []:
        return None
    max_val = min_val = lst[0]
    for x in lst:
        if x > max_val:
            max_val = x 
        elif x < min_val:
            min_val = x 
    return min_val, max_val

    
def sequential_search(lst, key):
    for i in range(len(lst)):
        if lst[i] == key:
            return i
    return -1
    
def shallow_copy(L):
    new_list = []
    for x in L:
        new_list.append(x)
    return new_list

def deep_copy(L):
        new_list = []
        for x in L:
            if isinstance(x, list):
                new_list.append(deep_copy(x))
            else:
                new_list.append(x)
        return new_list
    
S = [[1, 2], [3, 4], [5, 6]]
T = deep_copy(S)
T[2][0] = 7
print(T)     

def create_board(r, c):
    board = []
    for _ in range(r):
        row = []
        for _ in range(c):
            row.append(' ')
        board.append(row)
    return board

def create_board_comp(r, c):
    return [ [' ' for _ in range(c)] for _ in range(r) ]

def display_board(board):
    num_rows = len(board)
    for row in range(num_rows):
        num_cols = len(board[row])
        for col in range(num_cols):
            print(' ' + board[row][col] + ' ', end = '')
            if col < num_cols - 1:
                print('|', end = '')
        print()
        if row < num_rows - 1:
            print('-' * (num_cols * 4 - 1))
        


#board = create_board_comp(3, 3)
#board[0][0] = 'X'
#board[2][2] = 'O'
#print(board)

#display_board(board)


ragged = [[1, 10, 9, 6], [3], [4, 12, 17, 1, 13], [8, 7]]

def find_max_2D(L):
    max_val = L[0][0]
    for row in L:
        for x in row:
            if x > max_val:
                max_val = x 
    return max_val
        








    
    