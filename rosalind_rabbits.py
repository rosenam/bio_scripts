# -*- coding: utf-8 -*-
"""
Austin Rosen

Rosalind - Rabbits and Recurrence Relations Exercise
"""
#######################################

def main(num,k):
    
    '''
    This function returns the total number of rabbit pairs that will be present
    after n months, if we begin with 1 pair and in each generation, every pair
    of reproduction-age rabbits produces a litter of k rabbit pairs
    (instead of only 1 pair)
    '''
    
    if num == 1:
        return 1
    elif num == 2:
        return 1
    else:
        return main(num-1,k) + k*main(num-2,k)
    
    return

########################################
    
if __name__ == '__main__':
    
    n = 34
    k = 3
    print(main(n,k))
    
########################################