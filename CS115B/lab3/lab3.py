'''
Created on Sep 22, 2017

@author: bpatton

I pledge my honor that I have abided by the Stevens Honor System

Brandon Patton
'''

def change(amount, coins):
    '''The function takes in a non-negative integer indicating the amount of money
    to be made (amount) and a list of coin values (coins).  This function returns 
    a non-negative integer indicating the minimum number of coins required to make
    up the given amount.'''
    if amount == 0:
        return 0
    elif coins == []:
        return float('inf')
    elif coins[0] > amount:
        return change(amount, coins[1:])
    else:
        lose_it = change(amount, coins[1:])
        use_it = 1 + change(amount - coins[0], coins)
        return min(use_it, lose_it)
print(change(6, [1, 2, 3, 4]))
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        