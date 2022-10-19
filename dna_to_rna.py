# -*- coding: utf-8 -*-
"""
Austin Rosen

DNA to RNA Converter
"""
###############################################

def main(in_handle):
    
    '''
    This function uses a translation table to take a DNA sequence from a file
    and return the corresponding RNA sequence
    '''
    
    with in_handle:
        dna = in_handle.read()
        
    translation_table = str.maketrans('T', 'U')
       
    rna = dna.translate(translation_table)
    
    print(rna)
    
    return
    
#############################################

if __name__ == '__main__':
    
    in_handle = open('rosalind_rna.txt')
    
    main(in_handle)
    
#############################################