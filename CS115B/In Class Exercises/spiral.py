'''
Created on Oct 5, 2017

@author: bpatton
'''

import turtle

def square_spiral(walls):
    def square_spiral_helper(distance, initial, count):
        if count == walls:
            turtle.done()
        else:
            turtle.left(90)
            turtle.forward(distance)
            square_spiral_helper(distance + initial * (count % 2), initial, count + 1) 
    square_spiral_helper(20, 20, 0)
    
def octogonal_spiral(walls):
    def octogonal_spiral_helper(distance, initial, count):
        if count == walls:
            turtle.done()
        else:
            turtle.left(45)
            turtle.forward(distance)
            octogonal_spiral_helper(distance + initial * (count % 2), initial, count + 1) 
    octogonal_spiral_helper(20, 5, 0)
    
octogonal_spiral(30)
