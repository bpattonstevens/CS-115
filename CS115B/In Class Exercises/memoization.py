'''
Created on Oct 3, 2017

@author: bpatton
'''

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-1)

def fib_memo(n):
    def fib_helper(n, memo):
        if n in  memo:
            return memo[n]   
        
        if n <= 1:
            result = n
        else:
            result = fib_helper(n - 1, memo) + fib_helper(n - 2, memo)
            
        memo[n] = result
        
        return result
    return fib_helper(n, {})
print(fib_memo(15))

def LCS(S1, S2):
    '''Returns the length of the longest common subsequence in strings S1 and S2.'''
    if S1 == '' or S2 == '':
        return 0
    if S1[0] == S2[0]:
        return 1 + LCS(S1[1:], S2[1:])
    return max(LCS(S1, S2[1:]), LCS(S1[1:], S2))


def LCS_memo(S1, S2):
    def LCS_helper(S1, S2, memo):
        if (S1, S2) in memo:
            return memo[(S1, S2)]
        
        if S1 == '' or S2 == '':
            result = 0
            
        elif S1[0] == S2[0]:
            result = 1 + LCS_helper(S1[1:], S2[1:], memo)
        else: 
            result = max(LCS_helper(S1, S2[1:], memo), LCS_helper(S1[1:], S2, memo))
        memo [(S1, S2)] = result
        return result
    return LCS_helper(S1, S2, {})

print(LCS_memo('akjdfnsa;ldifj;sdlf', 'a;lsdkfjs;ldafj;lkdsf'))

        
       


