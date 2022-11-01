# -*- coding: utf-8 -*-
"""
Austin Rosen

Rosalind Consensus
"""

################################
def main():
    
    '''
    
    This function takes a collection of at most 10 DNA strings of equal length (at most 1 kbp)
    in FASTA format and returns a consensus string and profile matrix for the collection. 
    (If several possible consensus strings exist, then any may be returned.)
    
    '''
    # open file
    try:
        in_handle = open('rosalind_cons.txt')
    except:
        return -1
    
    with in_handle:
        
        # initialize variables
        seq = []                                    
        size = 0
        my_dict = {'A':[], 'C':[], 'G':[], 'T':[]}
        consensus = ''
        
        # find length of sequence
        for line in in_handle:
            if line[0] != '>':
                size = len(line)
                in_handle.seek(0)
                break
            else:
                continue
            
        # pull sequences from file
        tmp = ''
        for line in in_handle:
            if line[0] == '>':
                seq.append(tmp)
                tmp = ''
            else:
                tmp = tmp + line.rstrip()
                
        seq.append(tmp)
        seq.pop(0)
        
        size = len(tmp)
        
        in_handle.seek(0)
        
        # initialize dictionary
        for i in range(size):
            my_dict['A'].append(0)
            my_dict['C'].append(0)
            my_dict['G'].append(0)
            my_dict['T'].append(0)
        
        
        # count nucleotides in each position for each sequence to build profile matrix
        for x in seq:
            i = 0
            for nt in x:
                if nt == 'A':
                    my_dict['A'][i] += 1
                elif nt == 'C':
                    my_dict['C'][i] += 1
                elif nt == 'G':
                    my_dict['G'][i] += 1
                else:
                    my_dict['T'][i] += 1 
                i += 1          
        
        # find max nt count at each sequence position to create consensus sequence
        for i in range(size):
            maximum = max(my_dict['A'][i], my_dict['C'][i], my_dict['G'][i], my_dict['T'][i])
            if my_dict['A'][i] == maximum:
                consensus = consensus + 'A'
            elif my_dict['C'][i] == maximum:
                consensus = consensus + 'C'  
            elif my_dict['G'][i] == maximum:
                consensus = consensus + 'G'
            else:
                consensus = consensus + 'T'
            
        # print consensus sequence and profile matrix    
        print(consensus)
        print('A:',*my_dict['A'], sep = ' ')
        print('C:',*my_dict['C'], sep = ' ')
        print('G:',*my_dict['G'], sep = ' ')
        print('T:',*my_dict['T'], sep = ' ')
    return 

##############################
if __name__ == '__main__':
    
    main()

#############################