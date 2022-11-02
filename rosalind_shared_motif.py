# -*- coding: utf-8 -*-
"""
Austin Rosen

Finding a Shared Motif -- Rosalind Exercise
"""

#############################################
def main():
    
    '''
    
    This function takes a collection of k (k≤100) DNA strings of length at most 
    1 kbp each in FASTA format and returns the longest common substring of the 
    collection. (If multiple solutions exist, only a single solution is returned.)
    
    '''
    
    # open file
    in_handle = open('rosalind_lcsm.txt')
    
    with in_handle:
    
        # initialize variables
        my_list = []
        i = 0
        shortest = 1000
        shared = []
        seqs = []
        index = 0
        tmp = ''
        
        # create list of sequences from file and identify shortest sequence
        for line in in_handle:
            if line[0] == '>':
                seqs.append(tmp)
                size = len(tmp)
                if size < shortest and size != 0:
                    shortest = size
                    index = i - 1
                i += 1
                tmp = ''
            else:
                tmp = tmp + line.rstrip()
                
        seqs.append(tmp)
        seqs.pop(0)

        # find all possible motifs from shortest sequence and look for them in all other sequences
        for i in range(0, shortest - 1):
            for j in range(i+2, shortest + 1):
                tmp_motif = seqs[index][i:j]
                
                shared.append(tmp_motif)
                
                # if motif found in all sequences, save the motif
                for seq in seqs:
                    if tmp_motif in seq:
                        continue
                    else:
                        shared.pop()
                        break
                    
    # find longest of all hared motifs and print to user
    longest = shared.index(max(shared, key=len))
    
    print(shared[longest])
        
    return

############################################
if __name__ == '__main__':
    
    main()
    
##############################################

