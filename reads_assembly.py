"""
Austin Rosen

Genome Assembly Using Reads -- Rosalind Exercise
"""

def main():

    # read in sequences
    in_handle = open('reads.txt')
    seqs = []
    for line in in_handle:
        seqs.append(line.strip())

    # find reverse complement for each sequence, and make a list of lists for each seq and its rev. comp.
    full = []
    for i in range(len(seqs)):
        tmp = [seqs[i],rev_comp(seqs[i])]
        full.append(tmp)
    print(full)

    # use first seq as starting point of sequence, and build on that using all other sequences
    results = str(full[0][0])
    print(results)
    tmp = full.copy()
    tmp.pop(0)
    print(tmp)

    # iterate through each sequence to figure out which one to append to currently growing assembly
    # stop once string is of maximum length assuming full coverage
    for seq in full:
        for t in tmp:
            if results[len(results) - len(seq) + 1:] == t[0:len(seq) - 1]:
                results += t[-1]
                if len(results) == len(seqs):
                    print(results)
                    return

    

def rev_comp(seq):

    ### Function for finding the reverse complement of a DNA sequence

    # find complement using translation table
    trans_table = str.maketrans('ACTG', 'TGAC')
    comp = seq.translate(trans_table)

    # reverse the string to give reverse complement sequence
    rc = comp[::-1]

    return rc

if __name__ == "__main__":

    main()