'''
Created on Oct 3, 2017

@author: bpatton
Pledge: I pledge my honor that I have abided by the Stevens Honor System.

Brandon Patton
'''

def pascal_row(n):
    def pascal_row_helper(n, lst, accum):
        if n < 0:
            return []
        if n == 0:
            return [1]
        if accum == n:
            return lst
        
        def pascal_row_helper2(lst2):
            if lst2 == []:
                return []
            if len(lst2) == 1:
                return []
            return [lst2[0] + lst2[1]] + pascal_row_helper2(lst2[1:])
        return pascal_row_helper(n, [1] + pascal_row_helper2(lst) + [1], accum + 1)
    
    return pascal_row_helper(n, [], 0)

def pascal_triangle(n):
    if n < 0:
        return [[]]
    if n == 0:
        return [[1]]  
    return pascal_triangle(n - 1) + [pascal_row(n)]



            
            
        
    