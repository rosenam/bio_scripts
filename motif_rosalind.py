# -*- coding: utf-8 -*-
"""
Austin Rosen

Motif Finder (Rosalind Exercise)
"""

################################
def main():
    
    '''
    
    This function takes a file with a DNA sequence and a motif, and returns to the 
    user the beginning nucluetoide postion(s) on the sequence for which that motif
    is located
    
    '''
    
    
    
    # open input file
    try:
        in_handle = open('rosalind_subs.txt')
    except:

        return -1
    
    with in_handle: 
        
        # initialize variables
        seq = ''
        motif = ''
        matches = []
        
        # pull sequence and motif from file
        line_num = 1
        for line in in_handle:
            if line_num == 1:
                seq = line.rstrip()
                line_num += 1
            else:
                motif = line.rstrip()
                
        # compare motif to sequence and record where matches are
        for i in range(len(seq)-len(motif)+1):
            if seq[i:i+len(motif)] == motif:
                matches.append(i+1)

            else: 
                continue
    
    return matches

##################################
if __name__ == '__main__':
    
    print(main())

####################################
