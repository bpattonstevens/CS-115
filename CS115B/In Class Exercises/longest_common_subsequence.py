'''
Created on Sep 21, 2017

@author: bpatton
'''

def LCS(S1, S2):
    '''Returns the length of the longest common subsequence in strings S1 and S2.'''
    if S1 == '' or S2 == '':
        return 0
    if S1[0] == S2[0]:
        return 1 + LCS(S1[1:], S2[1:])
    return max(LCS(S1, S2[1:]), LCS(S1[1:], S2))

print(LCS('spam', 'sam'))


def LCS_with_values(S1, S2):
    if S1 == '' or S2 == '':
        return (0, '')
    if S1[0] == S2[0]:
        result = LCS_with_values(S1[1:], S2[1:])
        return (1 + result[0], S1[0] + result[1])
    useS1 = LCS_with_values(S1, S2[1:])
    useS2 = LCS_with_values(S1[1:], S2)
    if useS1[0] > useS2[0]:
        return useS1
    return useS2

    
        