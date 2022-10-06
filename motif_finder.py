# -*- coding: utf-8 -*-
"""
Austin Rosen 
Motif Finder

This module parses two command line arguments, an input file with sequence data and a sequence motif
input by the user, where N can be any nucleotide. The module then calls on a function to determine
the number of instances that the user specified motif is found within the designated sequence file,
and prints out the info to the user

"""

import argparse
import re

#######################################################

def main():
    
    '''
    This function calls arg_parse and motif_finder functions and prints the output to the user, including
    error message if necessary
    '''
    
    arg = arg_parse()
    
    motif_finder(arg[0], arg[1])
    
    num = motif_finder('c_elegans_chri.fa', arg[1].rstrip())
    
    if num == -1:
        print('Error opening file')
    else:   
        print(f'The motif "{arg[1]}" appeared {num} times in the sequence file {arg[0]}')
    
    
#######################################################
 
def arg_parse():
    
    '''
    This function parses the two command line arguments to be used later 
    '''
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-i', '--input_file', required=True, help="input file") 
    parser.add_argument('-m', '--motif', required=True, help="motif")
    
    args = parser.parse_args()
     
    print('args:', args)
    
    return args.input_file, args.motif
   
#######################################################
    
def motif_finder(input_file, motif):
    
    '''
    This function takes the motif and finds the number of instances the motif occurs in the sequence file
    '''
    
    #convert motif to lowercase and convert "n's" to wildcards
    translation_table = str.maketrans('ACTGN','actg.')
    
    final_motif = motif.translate(translation_table)
    
    # open files with try and except
    try:
        input_handle = open(input_file)
    except: 
        return -1
        
    with input_handle: 
        seq = ''
        matches = 0
        
        # strip sequence of new line characters
        for line in input_handle:
            if line[0] == '>':
                continue
            else:
                seq += line.rstrip()
                
        # compare motif to sequence and count matches
        for i in range(len(seq)-len(final_motif)+1):
            if re.search(final_motif, seq[i:i+len(final_motif)]):
                matches += 1
                
    return matches
    
    

   
#######################################################
    
if __name__ == '__main__':
    
    main()
    
        
########################################################
