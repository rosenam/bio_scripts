# -*- coding: utf-8 -*-
"""
Austin Rosen

RNA to Protein Translation
"""
#####################################
def main(aa_dict, in_handle):
    
    '''
    
    This function takes an RNA sequence and stores the sequence as a list of codons. 
    The codons are then compared against a dictionary with key:value pairs as codon:amino acids,
    and the corresponding amino acid sequence is returned to the user.  
    
    '''
    
    # initialize variables
    cdn = []
    acids = ''
    
    
    # store sequencee as a list of codons
    with in_handle: 
        seq = in_handle.read()
        num = int(len(seq)/3)

        for i in range(0, num):
            cdn.insert(i, seq[:3])
            seq = seq[3:]
        
    # compare each codon to the amino acid dictionary
    for key in cdn:
        if aa_dict[key] != "Stop":
            acids += aa_dict[key]
    
    # print the amino acid sequence    
    print(acids)
    
    return

#####################################
if __name__ == '__main__':
    
    # open the requisite files
    table_handle = open('aa_table.txt')
    in_handle = open('rosalind_prot.txt')
    
    # initialize dictionary object for amino acid table
    aa_dict = {}
    
    # build amino acid dictionary from Rosalind table
    with table_handle: 
        for line in table_handle:
            chunks = line.split()

            aa_dict[chunks[0]] = chunks[1]
            aa_dict[chunks[2]] = chunks[3]
            aa_dict[chunks[4]] = chunks[5]
            aa_dict[chunks[6]] = chunks[7]
    
    # call algorithm
    main(aa_dict, in_handle)
    
######################################3