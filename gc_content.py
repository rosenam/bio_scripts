# -*- coding: utf-8 -*-
"""
Austin Rosen

Compute GC Content (Rosalind Exercise)
"""
#################################################
def main(in_handle):
    
    '''
    
    This functions takes a set of "clean" DNA sequences and returns the name 
    of the sample with the greatst percent GC content and the associated value.
    
    '''
    
    # Initialize variables
    
    gc_percent = ''
    count = 0
    gc = 0
    name = ''
    my_dict = {}
    
    # Create a dictionary to store samples and their associated sequences
    for line in in_handle:
        if line[0] == ">":
            name = line[1:]
            my_dict[name] = ''
            
        else:
            my_dict[name] += line.rstrip()
    
    # Compute percent GC content for each sequence, and store that value in the dictionary
    for name in my_dict:
        for nt in my_dict[name]:
            if nt == 'G' or nt == 'C':
                gc += 1   
            count += 1
        gc_percent = round((gc/count) * 100, 6)
        my_dict[name] = gc_percent
                
        count = 0
        gc = 0
        
    # Find sample with maximum GC content, and print name and value
    maximum = max(my_dict, key = my_dict.get)
    print(maximum, my_dict[maximum])

    return
#####################################################
    
if __name__ == '__main__':
    
    in_handle = open('rosalind_gc.txt')
    
    main(in_handle)
    
######################################################