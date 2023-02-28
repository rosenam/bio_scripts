# -*- coding: utf-8 -*-
"""
Austin Rosen

Rosalind Overlap Graphs Exercise
"""

##########################################
def main():

    """

    This function takes a collection of DNA strings in FASTA format having total length at most 10 kbp,
    and returns the adjacency list corresponding to O3.

    """
    
    # open file
    try:
        in_handle = open('rosalind_grph.txt')
    except:
        return -1
    
    # initialize variabls
    my_dict = {}
    name = ''
    
    # build dictionary to hold names and associated sequnces
    with in_handle:
        line_num = 1
        for line in in_handle:
            if line_num % 3 == 1:            # if 'name' line
                name = line[1:].rstrip()
                my_dict[name] = ''
            
            else:
                my_dict[name] += line.rstrip()
            line_num += 1
            
    # test sequnces for overlap and print results
    for key_1, value_1 in my_dict.items():
        for key_2, value_2 in my_dict.items():
            if key_1 != key_2 and value_1.endswith(value_2[:3]):
                print(key_1, key_2)
    
    return

###########################################
if __name__ == '__main__':
    
    main()
    
##########################################
