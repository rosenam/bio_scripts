# -*- coding: utf-8 -*-
"""
Austin Rosen

Rosalind - Mortal Rabbits Exercise
"""
#######################################

def main(num,m):
    
    '''
    This function returns the total number of rabbit pairs that will be present
    after n months, if we begin with 1 pair and in each generation, every pair
    of reproduction-age rabbits produces a litter of 1 rabbit pairs, and all rabbits
    live for only m months
    '''

    fib = []
    child = [0,1,0]
    adult = [0,0,1]
    
    if num == 1:

        print(adult[1] + child[1])
    
    elif num == 2:
        
        print(adult[2] + child[2])


    else:
        for i in range(3,n+1):
            child.append(adult[i-1])
            if i-m < 0:
                adult.append(child[i-1] + adult[i-1])
            else:
                adult.append(child[i-1] + adult[i-1] - child[i-m])
        
        print(child[n] + adult[n])

    return

########################################
    
if __name__ == '__main__':
    
    n = 100
    m = 19
    main(n,m)
    
########################################