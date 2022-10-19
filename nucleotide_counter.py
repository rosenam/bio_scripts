# -*- coding: utf-8 -*-
"""
Austin Rosen

Nucleotide Counter
"""
##################################

def main(in_handle):

    '''
    This function reads sequence data from a file and returns the number of 
    occurences of A, C, G, and T (in that order) using a dictionary
    '''
    
    with in_handle:
        my_dict ={'A':0, 'C':0, 'G':0, 'T':0}
        seq = in_handle.read()
        for nuc in [*seq]:
            if nuc == 'A':
                my_dict['A'] += 1
            elif nuc == 'C':
                my_dict['C'] += 1
            elif nuc == 'G':
                my_dict['G'] += 1
            elif nuc == 'T':
                my_dict['T'] += 1 
            else:
                continue
        print(my_dict['A'], ' ', my_dict['C'], ' ', my_dict['G'], ' ', my_dict['T'])
    return

###################################
    
if __name__ == '__main__':
    
    in_handle = open('rosalind_dna.txt')
    
    main(in_handle)
    
#########################################