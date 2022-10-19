# -*- coding: utf-8 -*-
"""
Austin Rosen

Reverse Complement Creator
"""
###############################################

def main(in_handle):
    
    '''
    This function uses a translation table to take a DNA sequence from a file
    and return the reverse complement of that sequence
    '''
    
    with in_handle:
        dna = in_handle.read()
        
    translation_table = str.maketrans('ACGT', 'TGCA')
       
    rna = dna.translate(translation_table)
    
    print(rna[::-1])
    
    return
    
#############################################

if __name__ == '__main__':
    
    in_handle = open('rosalind_revc.txt')
    
    main(in_handle)
    
#############################################