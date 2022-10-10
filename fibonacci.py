# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 09:08:50 2022

@author: austi
"""

######################################

def main():
    
    '''
    This function asks for the user to put an index for which the value should be found, and prints value
    '''
    
    num = int(input("For which index of the Fibonacci sequence would you like to compute the value?\n"))
    print(f'Index: {num} \nValue: {fib(num)}')
    
######################################
    
def fib(num):
    
    '''
    This function computes the value of the Fibonacci sequence at the specified index
    '''
    
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num-1) + fib(num-2)
        
######################################
    
if __name__ == '__main__':
    main()
    
######################################