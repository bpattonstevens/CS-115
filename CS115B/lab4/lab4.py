'''
Created on Sep 29, 2017

@author: bpatton
Pledge: I pledge my honor that I have abided by the Stevens Honor System

Brandon Patton
'''
def knapsack(capacity, itemList):
    if capacity == 0:
        return [0, []]
    if itemList == []:
        return [0, []]
    if itemList[0][0] > capacity:
        return knapsack(capacity, itemList[1:])
    
    [use_it_capacity, use_it_list] = knapsack(capacity - itemList[0][0], itemList[1:])
    
    [lose_it_capacity, lose_it_list] = knapsack(capacity, itemList[1:])
    
    use_it_capacity2 = use_it_capacity + itemList[0][1]
    
    if use_it_capacity + itemList[0][1] > lose_it_capacity:
        
        use_it_list = [itemList[0]] + use_it_list

        return [use_it_capacity2, use_it_list]
    else:
        return [lose_it_capacity, lose_it_list]

    



        