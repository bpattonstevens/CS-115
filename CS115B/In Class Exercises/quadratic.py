'''
Created on Nov 17, 2017

@author: bpatton

I pledge my honor that I have abided by the Stevens Honor System

Brandon Patton
'''

import math

class QuadraticEquation(object):
    def __init__(self, a, b, c):
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")
        self.__a = float(a)
        self.__b = float(b) 
        self.__c = float(c)
        
    @property
    def a(self):
        return self.__a
    @property
    def b(self):
        return self.__b
    @property
    def c(self):
        return self.__c 
    
    def discriminant(self):
        return self.__b**2 - 4*self.__a*self.__c
    
    def root1(self):
        if self.discriminant() < 0:
            return None
        else:
            return (-self.__b + math.sqrt(self.discriminant()))/(2*self.__a)
    
    def root2(self):
        if self.discriminant() < 0:
            return None
        else:
            return(-self.__b - math.sqrt(self.discriminant()))/(2*self.__a)
    
    def __str__(self):
        def newa():
            if self.a != 0:
                if abs(self.a) != 1:
                    if self.a < 0:
                        return '-'+ str(abs(self.a))+'x^2'
                    else:
                        return str(self.a)+'x^2'
                if self.a==1:
                    return 'x^2'
                else:
                    return '-x^2'


        def newb():
            if self.b != 0:
                if abs(self.b) != 1:
                    if self.b < 0:
                        return ' - '+ str(abs(self.b))+'x'
                    else:
                        return ' + '+ str(self.b)+'x'
                if self.b==1:
                    return ' + x'
                else:
                    return ' - x'
            else:
                return ''

        def newc():
            if self.c != 0:
                if self.c < 0:
                    return ' - '+ str(abs(self.c))
                else:
                    return ' + '+ str(self.__c)
            else:
                return ''
        return newa() + newb() + newc()+ ' = 0'   
        
        
        
        
