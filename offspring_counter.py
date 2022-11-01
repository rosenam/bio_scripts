# -*- coding: utf-8 -*-
"""
Austin Rosen

Rosalind Exercise -- Calculate Expected Offspring 
"""
##################################################
def main():
    
    '''
    
    This function calculates the expected number of offspring displaying the dominant phenotype
    in the next generation, under the assumption that every couple has exactly two offspring.
    
    Input: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond
    to the number of couples in a population possessing each genotype pairing for a given factor. 
    In order, the six given integers represent the number of couples having the following genotypes:

        1. AA-AA
        2. AA-Aa
        3. AA-aa
        4. Aa-Aa
        5. Aa-aa
        6. aa-aa
    
    '''
    
    in_handle = open('rosalind_iev.txt')
    
    with in_handle:
        inputs = in_handle.read().split(" ")

        dom_off = 2*(int(inputs[0])) + 2*(int(inputs[1])) + 2*(int(inputs[2])) + 1.5*(int(inputs[3])) + 1*(int(inputs[4]))
        
        print(dom_off)
        
    return
##################################################
if __name__ == '__main__':
    
    main()

######################################################

