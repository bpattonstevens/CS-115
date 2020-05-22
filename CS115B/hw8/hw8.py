'''
Created on Oct 31, 2017
@author: Brandon Patton
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

bpatton

CS115 - Lab 6
'''
FullAdder = { ('0','0','0') : ('0','0'), ('0','0','1') : ('1','0'), ('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1') }

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    def bToN_helper(s, accum):
        if s == '':
            return 0
        if int(s[-1]) == 1:
            return accum + bToN_helper(s[:-1], accum * 2)
        return bToN_helper(s[:-1], accum * 2)
    return bToN_helper(s, 1)

def addB(S, T):
    '''Takes two strings of binary numbers and adds them using binary addition
    rather than converting to numbers and adding from there'''
    if len(S) > len(T):
        T = (len(S) - len(T))*'0' + T 
    if len(T) > len(S):
        S = (len(T) - len(S))*'0' + S
    def addB_helper(S, T, carry):
        '''Uses the Dictionary FullAdder and a carry variable to achieve binary
        addition. The dictionary has every possible outcome stored to reference when
        needed.'''
        if S == '' or T == '':
            return carry
        result = FullAdder[(S[-1], T[-1], carry)]
        return addB_helper(S[:-1], T[:-1], result[1]) + result[0]
    def leading_zeros(S):
        '''Eliminates leading zeros from the final binary string.'''
        if S == '0':
            return '0'
        if S[0] == '0':
            return leading_zeros(S[1:])
        if S[0] != '0':
            return S
    return leading_zeros(addB_helper(S, T, '0'))
   

def TcToNum(s):
    '''Takes a string of 8 bits representing an integer in two's compliment as 
    input and returns the corresponding integer'''
    if s[0] != '1':
        return binaryToNum(s)  
    def TcToNum_helper(s):
        '''Handles the case for negative numbers'''
        if s == '':
            return ''
        if s[0] == '1':
            return '0' + TcToNum_helper(s[1:])
        else:
            return '1' + TcToNum_helper(s[1:])
    return -1 * binaryToNum(addB(TcToNum_helper(s), '1'))

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    if n % 2 == 1:
        return numToBinary(n//2) + '1'
    return numToBinary(n//2) + '0'


def NumToTc(N):
    '''Takes an integer N as input and returns a string representing the two's
    compliment representation of that integer'''
    if N > 127 or N < -128:
        return 'Error'
    def eight_bits(s):
        '''Makes sure each string is padded out to 8 bits'''
        return (8-len(s)) * '0' + s
    if N >= 0:
        return eight_bits(numToBinary(N))
    positive_binary = eight_bits(numToBinary(-1 * N))
    def NumToTc_helper(s):
        '''Handles the case for negative numbers'''
        if s == '':
            return ''
        if s[0] == '1':
            return '0' + NumToTc_helper(s[1:])
        else:
            return '1' + NumToTc_helper(s[1:])
    
    negative = eight_bits(addB(NumToTc_helper(positive_binary), '1'))
    negative = '1' + negative[1:]
    return negative

    
        
        
        
    
    
        
        
        
        
        
        
        